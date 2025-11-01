from os import chdir
from pytubefix import YouTube
from Model.ModelYoutube import ModelYoutube
import threading # Necesario para ejecutar operaciones en segundo plano
class ControllerYotube():

    """
    Clase que gestiona la descarga de videos y audios de YouTube.
    """

    def __init__(self, page, show_error_callback, show_info_callback):

        """
        Constructor de la clase. Inicializa instancias de otras clases y variables.
        """
        self.page = page
        self.show_error = show_error_callback
        self.show_info = show_info_callback
        self.__youtube = None
        self.__modeloYoutube = ModelYoutube()


    def Download(self,link,button,address):

        if not link:
            # Usamos el callback para mostrar el error en la UI principal
            self.show_error("El enlace de YouTube no puede estar vacío.")
            return
        
        self.show_info(f"Iniciando descarga de {link} en calidad {button}...")
        """
        Método para descargar videos o audios de YouTube.

        Args:
            link (str): El enlace del video de YouTube.
            boton (str): El botón seleccionado para la calidad de descarga (Alta, Baja o None).
            ubicacion (str): La ubicación en la que se guardarán los archivos descargados.

        Returns:
            None
        """
        answer = self.__modeloYoutube.validarUrl(link)
        if answer:
            print("Enlace válido, iniciando descarga...")
            download_thread = threading.Thread(
            target=self._perform_download_threaded,
            args=(link, button, address)
        )
            download_thread.daemon = True # El hilo se cerrará si la app principal lo hace
            download_thread.start()
        else:
            self.show_error("El enlace de YouTube no es válido.")

    def _perform_download_threaded(self, link, button, address):
        try:
            print("Iniciando descarga en segundo plano...")
            self.__youtube = YouTube(link)
            if button == "High":
                chdir(address + "/Videos")
                print("Descargando video en alta calidad...")
                self.__youtube.streams.get_highest_resolution().download()
                print("Descarga completada - notificando...")
                # Usar page.run_task directamente con función async
                self.page.run_task(self._notify_success)

            elif button == "Low":
                chdir(address + "/Videos")
                print("Descargando video en baja calidad...")
                self.__youtube.streams.get_lowest_resolution().download()
                print("Descarga completada - notificando...")
                # Usar page.run_task directamente con función async
                self.page.run_task(self._notify_success)
        except Exception as e:
            print(f"Error en descarga: {e}")
            # Usar page.run_task directamente con función async
            self.page.run_task(self._notify_error)

    async def _notify_success(self):
        """Función async para notificar éxito en el hilo principal"""
        self.show_info("¡Descarga completada exitosamente!")

    async def _notify_error(self):
        """Función async para notificar error en el hilo principal"""
        self.show_error("Hubo un error al momento de hacer la descarga")