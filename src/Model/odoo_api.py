import xmlrpc.client
import re

OD_URL = 'https://analyzed-barn-ribbon-uni.trycloudflare.com' 
OD_DB = 'devel' 
OD_USER = 'admin' 
OD_PASSWORD = 'admin' 

LOCAL_TAG_ID = 8

def get_admin_connection():
    try:
        common = xmlrpc.client.ServerProxy(f'{OD_URL}/xmlrpc/2/common')
        uid = common.authenticate(OD_DB, OD_USER, OD_PASSWORD, {})
        
        if not uid:
            print("Error: Autenticación Admin Odoo fallida. Verifica las credenciales.")
            return None, None, None

        models = xmlrpc.client.ServerProxy(f'{OD_URL}/xmlrpc/2/object')
        
        return OD_DB, uid, models

    except Exception as e:
        print(f"Error al conectar con Odoo: {e}")
        return None, None, None

def strip_html(text):
    if not text:
        return ""
    
    text = text.replace('&nbsp;', ' ')
    
    text = re.sub(r'<\s*br\s*/?>|<\s*/\s*(?:p|div|h[1-6])\s*>', '\n\n', text, flags=re.IGNORECASE)
    
    clean = re.compile('<.*?>')
    text = re.sub(clean, '', text)
    
    text = re.sub(r'(\n\s*){2,}', '\n\n', text).strip()
    
    return text.strip()

def get_pos_config_name_map():
    db, uid, models = get_admin_connection()
    if not uid:
        return {}
    
    try:
        pos_configs = models.execute_kw(
            db, 
            uid, 
            OD_PASSWORD, 
            'pos.config', 
            'search_read', 
            [[]], 
            {'fields': ['id', 'name']}
        )
        
        pos_map = {
            config['name'].lower(): (config['id'], config['name']) 
            for config in pos_configs
        }
        return pos_map
    except Exception:
        print("Error: No se pudo obtener el mapeo de configuraciones TPV.")
        return {}

def get_venues_from_odoo():
    db, uid, models = get_admin_connection()
    locales_data = []

    if not uid:
        print("Error: No se pudo obtener conexión de administrador para locales.")
        return []

    pos_map = get_pos_config_name_map()

    try:
        fields_to_fetch = ['id', 'name', 'comment', 'email', 'phone', 'image_1920']
        
        odoo_locales = models.execute_kw(
            db, 
            uid, 
            OD_PASSWORD, 
            'res.partner', 
            'search_read', 
            [
                [
                    ('is_company', '=', True), 
                    ('category_id', 'in', [LOCAL_TAG_ID]) 
                ]
            ], 
            {'fields': fields_to_fetch}
        )
        
        for local in odoo_locales:
            
            image_b64 = local.get('image_1920')
            url_imagen = ""
            if image_b64:
                url_imagen = f"data:image/png;base64,{image_b64}" 

            descripcion_completa = local.get('comment')
            descripcion_limpia = strip_html(descripcion_completa)
            telefono = local.get('phone') or "Sin Teléfono"
            
            local_name_lower = local['name'].lower()
            pos_info = pos_map.get(local_name_lower) 
            
            pos_id = pos_info[0] if pos_info else None
            pos_name = pos_info[1] if pos_info else "NO ENCONTRADO"
            
            locales_data.append({
                "id_local": local['id'],
                "nombre": local['name'],
                "descripcion": descripcion_limpia or "Contacto Odoo sin descripción detallada.",
                "horario": telefono, 
                "url_imagen": url_imagen, 
                "pos_config_id": pos_id, 
                "pos_config_name": pos_name,
            })

    except xmlrpc.client.Fault as fault:
        print(f"Error Odoo: Error al acceder a 'res.partner'. Verifica permisos, modelo o que la Etiqueta exista. {fault.faultString}")
        return []
    except Exception as e:
        print(f"Error inesperado al obtener locales de Odoo: {e}")
        return []
    
    return locales_data

def get_products_by_category_name(category_name):
    from Model.reservation_model import Dish
    db, uid, models = get_admin_connection()
    dishes = []
    
    if not uid:
        return []

    try:
        category_ids = models.execute_kw(
            db, uid, OD_PASSWORD, 'product.category', 'search',
            [[('name', 'ilike', category_name)]]
        )
        
        if not category_ids:
            print(f"Advertencia: No se encontró la categoría '{category_name}' en Odoo.")
            return []

        category_id = category_ids[0]
        
        product_fields = ['id', 'name', 'list_price']
        odoo_products = models.execute_kw(
            db, uid, OD_PASSWORD, 'product.product', 'search_read',
            [[('categ_id', '=', category_id), ('sale_ok', '=', True)]], 
            {'fields': product_fields}
        )
        
        for prod in odoo_products:
            dishes.append(Dish(
                id=prod['id'], 
                name=prod['name'], 
                price=prod['list_price']
            ))
            
    except Exception as e:
        print(f"Error al obtener productos de Odoo: {e}")
        return []
    
    return dishes