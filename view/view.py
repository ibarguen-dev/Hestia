import flet as ft
from controls.ControllerYotube import ControllerYotube
from controls.ControllerOrganizer import ControllerOrganizer
from controls.Controllerdecompress import Controllerdecompress
class HestiaApp:
    def __init__(self, page: ft.Page,adress: str):
        self.page = page
        self.adress = adress
        self.page.title = "Hestia - Tu Asistente Digital"
        self.page.theme_mode = ft.ThemeMode.SYSTEM
        self.page.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.window_width = 1000
        self.page.window_height = 700
        self.page.window_min_width = 800
        self.page.window_min_height = 600
        
        self.error_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Row([ft.Icon(ft.Icons.ERROR_OUTLINED, color=ft.Colors.RED_500), ft.Text("¡Error!", color=ft.Colors.RED_500)]),
            content=ft.Text(""), # El contenido se establecerá dinámicamente
            actions=[ft.ElevatedButton("Entendido", on_click=self._close_error_dialog)],
            actions_alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.info_snackbar = ft.SnackBar(
            ft.Text("", color=ft.Colors.WHITE), # El texto se establecerá dinámicamente
            bgcolor=ft.Colors.GREEN_700,
            duration=3000,
            action="OK"
        )
        
        self.file_picker = ft.FilePicker(on_result=self._on_decompress_file_selected)
        self.page.overlay.append(self.file_picker)
        
        self.file_picker_image = ft.FilePicker(on_result=self._on_image_file_selected)
        self.page.overlay.append(self.file_picker_image)
        
        self.file_picker_file = ft.FilePicker(on_result=self._on_file_file_selected)
        self.page.overlay.append(self.file_picker_file)
        
        # Agregar el snackbar al overlay de la página
        self.page.overlay.append(self.info_snackbar)

        self.page.overlay.append(self.error_dialog)
        
        self.__controllerYotube= ControllerYotube(
            page=self.page, # Pasamos la página completa
            show_error_callback=self._show_error_dialog, # Le pasamos el método de HestiaApp para errores
            show_info_callback=self._show_info_snackbar 
        )
        
        self.__controllerOrganizer = ControllerOrganizer(
            adress,
            page = self.page,
            show_error_callback = self._show_error_dialog,
            show_info_callback = self._show_info_snackbar)
        
        self.compressed_file_path_input = ft.TextField(
            label="Ruta del archivo comprimido",
            width=400,
            hint_text="Usa el botón para seleccionar un archivo...",
            read_only=True # Es un TextField
        )
        self.youtube_link_input = ft.TextField(
            label="Enlace de YouTube",
            width=400,
            hint_text="Pega aquí el enlace del video...",
            can_reveal_password=True
        )
        
        self.imagen_link_input = ft.TextField(
            label="Enlace de de la imagen",
            width=400,
            hint_text="Pega aquí el enlace del la imagen...",
            can_reveal_password=True
        )

        
        
        
        self.__controllerDecompress = Controllerdecompress()
        
        # --- Definición de Vistas ---
        self.welcome_view = self._create_welcome_view()
        self.youtube_view = self._create_youtube_view()
        self.organizer_view = self._create_organizer_view()
        # self.images_view = self._create_images_view()
        # self.decompress_view = self._create_decompress_view()
        # self.convert_file_view = self._create_convert_file_view()

        # --- Contenedor principal que mostrará las diferentes vistas ---
        self.main_content_area = ft.Container(
            content=self.welcome_view, # Inicia con la vista de bienvenida
            expand=True,
            alignment=ft.alignment.center,
        )
        
        # --- Componentes principales de la UI (Botón de Ajustes y Menú) ---
        # self.settings_button = self._create_settings_button()
        self.nav_rail = self._create_navigation_rail()

        # --- Construcción del layout final de la página ---
        self.page.add(
            ft.Row(
                [
                    self.nav_rail,
                    ft.VerticalDivider(width=1),
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Container(expand=True),
                                    # self.settings_button,
                                ],
                                alignment=ft.MainAxisAlignment.END,
                                spacing=0,
                            ),
                            self.main_content_area, # Aquí se mostrará el contenido dinámico
                        ],
                        expand=True,
                    ),
                ],
                expand=True,
            )
        )
        self.page.update() # Actualiza la página inicial
        
        self.__controllerOrganizer.oraganizer()
    def _show_error_dialog(self, message: str):
        self.error_dialog.content.value = message
        self.page.dialog = self.error_dialog  # <-- Esto es necesario
        self.error_dialog.open = True
        self.page.update()

    def _close_error_dialog(self, e):
        self.error_dialog.open = False
        self.page.update()

    def _show_info_snackbar(self, message: str):
        print(f"Mostrando snackbar: {message}")  # Debug
        self.info_snackbar.content.value = message
        self.info_snackbar.open = True
        self.page.update()
        print("Snackbar actualizado")  # Debug

    # --- Métodos para crear las vistas individuales ---
    def _create_welcome_view(self):
        return ft.Column(
            [
                ft.Text("¡Bienvenido a tu aplicación!", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("Selecciona una opción del menú lateral para comenzar.", size=16),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        )

    def _create_youtube_view(self):

        return ft.Column(
            [
                ft.Text("Descargar de YouTube", size=24, weight=ft.FontWeight.BOLD),
                self.youtube_link_input,
                ft.Row(
                    [
                        ft.ElevatedButton("Descargar Alta Calidad", on_click=lambda e: self.__controllerYotube.Download(self.youtube_link_input.value,"High",self.adress)),
                        ft.ElevatedButton("Descargar Baja Calidad", on_click=lambda e: self.__controllerYotube.Download(self.youtube_link_input.value,"Low",self.adress)),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        )
        


    def _create_organizer_view(self):
        return ft.Column(
            [
                ft.Text("Organizador de Archivos", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Contenido para organizar archivos irá aquí.", size=16),
                ft.ElevatedButton("Organizar archivo", on_click=lambda e: self.__controllerOrganizer.oraganizer()),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        )

    def _create_decompress_view(self):
        return ft.Column(
            [
                ft.Text("Descomprimir Archivos", size=24, weight=ft.FontWeight.BOLD),
                ft.Row(
                    [
                        
                        ft.IconButton(
                            icon=ft.Icons.FOLDER_OPEN,
                            tooltip="Seleccionar archivo comprimido",
                            on_click=lambda _: self.file_picker.pick_files(
                                dialog_title="Seleccionar archivo para descomprimir",
                                allow_multiple=False,
                                allowed_extensions=["zip", "rar", "7z", "tar", "gz"]
                            )
                        ),
                    self.compressed_file_path_input,
                ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.ElevatedButton("Descomprimir", on_click=lambda e: self.__controllerDecompress.decompress(self.compressed_file_path_input.value,self.adress+"/Descomprimidos")),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        )
        
    def _on_decompress_file_selected(self, e: ft.FilePickerResultEvent):
        if e.files:
            selected_path = e.files[0].path
            self.compressed_file_path_input.value = selected_path
            print(f"Archivo seleccionado para descomprimir: {selected_path}")
            self.page.update()
            
    def _on_image_file_selected(self, e: ft.FilePickerResultEvent):
        if e.files:
            selected_path = e.files[0].path
            self.imagen_link_input.value = selected_path
            print(f"Archivo seleccionado para descomprimir: {selected_path}")
            self.page.update()

    def _on_file_file_selected(self, e: ft.FilePickerResultEvent):
        if e.files:
            selected_path = e.files[0].path
            self.imagen_link_input.value = selected_path
            print(f"Archivo seleccionado para descomprimir: {selected_path}")
            self.page.update()

    # --- Métodos para crear los componentes principales de la UI ---
    # def _create_settings_button(self):
    #     return ft.IconButton(
    #         icon=ft.Icons.SETTINGS,
    #         icon_size=25,
    #         tooltip="Ajustes",
    #         on_click=lambda e: print("Botón de ajustes clickeado!"),
    #     )

    def _create_navigation_rail(self):
        """
        Crea el menú lateral de navegación principal de la aplicación.

        Permite al usuario cambiar entre las diferentes vistas:
        - Inicio
        - Organizador de archivos
        - YouTube
        - Descomprimir
        Returns:
            ft.NavigationRail: Componente de menú lateral de Flet.
        """
        return ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            extended=True,
            min_width=150,
            min_extended_width=250,
            leading=ft.Column(
                [
                    ft.Image(
                        src="https://flet.dev/img/flet-logo.svg",
                        width=60,
                        height=60,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text("Menú", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.Icon(ft.Icons.HOME),
                    label="Inicio",
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icon(ft.Icons.FOLDER),
                    label="Organizador de archivos",
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icon(ft.Icons.DOWNLOAD),
                    label="YouTube",
                ),
                # ft.NavigationRailDestination(
                #     icon=ft.Icon(ft.Icons.DATA_USAGE), # Cambié a un icono más genérico para "Descomprimido"
                #     label="Descomprimir",
                # ),
            ],
            on_change=self._change_main_content, # Referencia al método de la instancia
        )

    # --- Función para cambiar el contenido principal (ahora un método de la clase) ---
    def _change_main_content(self, e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            self.main_content_area.content = self.welcome_view
        elif selected_index == 1:
            self.main_content_area.content = self.organizer_view
        elif selected_index == 2:
            self.main_content_area.content = self.youtube_view
        
        
        self.page.update()

# --- Función principal que inicia la aplicación Flet ---
