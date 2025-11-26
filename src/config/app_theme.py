import flet as ft

class ColorPalette:

    success = ft.Colors.GREEN_700
    error = ft.Colors.RED_700

    light_background = "#F5F5F5"
    light_surface = ft.Colors.WHITE
    light_appbar = ft.Colors.LIGHT_BLUE_100
    light_primary = ft.Colors.INDIGO_600
    light_on_primary = ft.Colors.WHITE
    light_text = "#000000"

    dark_background = "#121212"
    dark_appbar = ft.Colors.INDIGO_900
    dark_surface = "#1E1E1E"
    dark_primary = ft.Colors.INDIGO_200
    dark_on_primary = ft.Colors.BLACK
    dark_text = "#FFFFFF"

theme_light = ft.Theme(
    color_scheme= ft.ColorScheme(
        background=ColorPalette.light_background,
        surface=ColorPalette.light_surface,
        primary=ColorPalette.light_primary,
        on_primary=ColorPalette.light_on_primary,
        on_surface=ColorPalette.light_text,
        error=ColorPalette.error,

        tertiary=ColorPalette.success,
    ),
    appbar_theme=ft.AppBarTheme(
        bgcolor=ColorPalette.light_appbar,
        foreground_color=ft.Colors.BLACK,
    ),
    visual_density=ft.VisualDensity.ADAPTIVE_PLATFORM_DENSITY,
)

theme_dark = ft.Theme(
    color_scheme=ft.ColorScheme(
        background=ColorPalette.dark_background,
        surface=ColorPalette.dark_surface,
        primary=ColorPalette.dark_primary,
        on_primary=ColorPalette.dark_on_primary,
        on_surface=ColorPalette.dark_text,
        error=ColorPalette.error,

        tertiary=ColorPalette.success,
    ),

    appbar_theme=ft.AppBarTheme(
        bgcolor=ColorPalette.dark_appbar,
        foreground_color=ft.Colors.WHITE,
    ),

    visual_density=ft.VisualDensity.ADAPTIVE_PLATFORM_DENSITY,
)