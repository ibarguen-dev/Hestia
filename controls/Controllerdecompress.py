import zipfile
import tarfile
import rarfile
import Model.Modeldecompress as Modeldecompress


class Controllerdecompress:
    
    def __init__(self):
        pass

    def decompress(self,file_path, output_dir):
        model = Modeldecompress.ModelDecompress()
        file_type = model.verfyFile(file_path)
        
        if not self.is_supported_format(file_path):
            print(f"Error: El formato del archivo '{file_path}' no es compatible para descompresión.")
            return
        
        if file_type == 'zip':
            self.zip(file_path, output_dir)
        elif file_type == 'tar.gz':
            self.tar(file_path, output_dir)
        elif file_type == 'rar':
            self.rar(file_path, output_dir)
        else:
            print(f"Error: El formato del archivo '{file_path}' no es compatible para descompresión.")
        
    def is_supported_format(self,type_file):
        supported_formats = ('.zip', '.tar.gz', '.tgz', '.tar', '.rar')
        return type_file.endswith(supported_formats)
    
    
    def tar(self, tar_path, extract_to_path):
        try:
            with tarfile.open(tar_path, 'r:*') as tar_ref:
                tar_ref.extractall(extract_to_path)
                print(f"'{tar_path}' descomprimido exitosamente en '{extract_to_path}'")
        except tarfile.ReadError:
            print(f"Error: '{tar_path}' no es un archivo TAR válido o está corrupto.")
        except FileNotFoundError:
            print(f"Error: El archivo TAR '{tar_path}' no fue encontrado.")
        except Exception as e:
            print(f"Ocurrió un error inesperado al descomprimir el archivo: {e}")
    
    
    def zip(self, zip_path, extract_to_path):
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to_path)
                print(f"'{zip_path}' descomprimido exitosamente en '{extract_to_path}'")
        except zipfile.BadZipFile:
            print(f"Error: '{zip_path}' no es un archivo ZIP válido o está corrupto.")
        except FileNotFoundError:
            print(f"Error: El archivo ZIP '{zip_path}' no fue encontrado.")
        except Exception as e:
            print(f"Ocurrió un error inesperado al descomprimir el archivo: {e}")
    
    def rar(self,rar_path, extract_to_path):
        try:
            with rarfile.RarFile(rar_path, 'r') as rf:
                rf.extractall(extract_to_path)
                print(f"'{rar_path}' descomprimido exitosamente en '{extract_to_path}'")
        except rarfile.RarCannotExec as e:
            print(f"Error: La utilidad 'unrar' no fue encontrada o no es ejecutable. Asegúrate de instalarla y de que esté en tu PATH. Detalles: {e}")
        except rarfile.BadRarFile:
            print(f"Error: '{rar_path}' no es un archivo RAR válido o está corrupto.")
        except FileNotFoundError:
            print(f"Error: El archivo RAR '{rar_path}' no fue encontrado.")
        except Exception as e:
            print(f"Ocurrió un error inesperado al descomprimir el archivo: {e}")
