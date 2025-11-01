# Hestia

Asistente de escritorio construido con Flet para ayudarte con tareas comunes: descargar videos de YouTube, organizar archivos, y descomprimir comprimidos, entre otras utilidades.

## Características
- **Interfaz moderna (Flet Desktop)** con `NavigationRail` lateral.
- **Descarga de YouTube** con dos calidades: Alta y Baja.
- **Organizador de archivos** para ordenar tu carpeta de descargas.
- **Notificaciones UI**:
  - Snackbars para información.
  - Diálogos de error modales.

> Nota: El módulo de conversión de archivos (`controls/ControllerConvertFile.py`) está preparado para PDF <-> Word, pero no está expuesto en la UI actual. Su uso requiere dependencias opcionales (ver más abajo).

## Requisitos
- Python 3.10+ recomendado
- Windows (probado en Windows; el código usa rutas estilo Windows y base de datos local)
- Paquetes principales (ver `requirements.txt`):
  - `flet==0.28.3`
  - `flet-desktop==0.28.3`
  - `pillow==11.3.0`
  - `pytubefix==9.4.1`

Dependencias opcionales para conversión de archivos:
- `pdf2docx`
- `docx2pdf`

## Instalación
1. Clona o descarga este repositorio.
2. Crea y activa un entorno virtual (opcional, pero recomendado).
3. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
   Si usarás la conversión PDF <-> Word:
   ```bash
   pip install pdf2docx docx2pdf
   ```

## Ejecución (modo desarrollo)
```bash
python main.py
```

- La aplicación inicializa configuración en base de datos local si no existe y crea carpetas necesarias en `C:/Users/<tu_usuario>/Downloads` mediante `controls/ControllerBoot.py`.
- La UI se construye desde `view/view.py` con la clase `HestiaApp`.

## Ejecutable (Windows)
El repositorio incluye `dist/hestia.exe` y `main.spec`. Si necesitas reconstruir:
```bash
pyinstaller main.spec
```
El ejecutable resultante aparecerá en `dist/`.

## Estructura del proyecto
- `main.py`: Punto de entrada. Carga configuración, prepara carpetas y lanza Flet.
- `view/view.py`: UI principal (`HestiaApp`). Define vistas y navegación.
- `controls/`: Lógica de control por funcionalidad.
  - `ControllerYotube.py`: Descarga de YouTube (usa `pytubefix`).
  - `ControllerOrganizer.py`: Organización de archivos de la carpeta destino.
  - `ControllerBoot.py`: Creación de carpetas iniciales.
  - `ControllerSettings.py`: Acceso/config de base de datos.
- `Model/`: Lógica de datos y validaciones.
  - `ModelConfiguration.py`: Validaciones de rutas de configuración.
  - Otros modelos (p.ej., para YouTube, conversión, etc.).
- `db/Database.py`: Acceso a base de datos (SQLite).
- `hestia.db`: Base de datos de configuración en producción.
- `dist/hestia.exe`: Build ya generado.
- `requirements.txt`: Dependencias principales.

## Configuración y persistencia
- La configuración se guarda en `hestia.db` vía `controls/ControllerSettings.py` y `db/Database.py`.
- La ruta base por defecto apunta a `C:/Users/<usuario>/Downloads`.
- `Model/ModelConfiguration.py` valida rutas con regex para prevenir entradas inválidas.

## Vistas principales (UI)
- **Inicio**: Pantalla de bienvenida.
- **Organizador de archivos**: Ejecuta `ControllerOrganizer.oraganizer()` para ordenar la carpeta configurada.
- **YouTube**: Ingresa URL y descarga en Alta o Baja calidad hacia la carpeta configurada.
- **Descomprimir**: Selector de archivos comprimidos y acción de descompresión hacia `<ruta_configurada>/Descomprimidos`.

## Notificaciones y UX
- Los errores se muestran con `AlertDialog` modal.
- Mensajes de éxito/estado usan `SnackBar` agregado a `page.overlay`.
- Operaciones potencialmente largas (descargas, IO) deben notificar usando métodos async para integrarse con `page.run_task()` y no bloquear la UI.

## Solución de problemas
- **Snackbar/AlertDialog no visibles**: Asegúrate de agregar componentes a `page.overlay` antes de abrirlos.
- **AssertionError al usar `page.run_task`**: Debes pasar funciones `async`, no lambdas síncronas. Declara métodos `async` (por ejemplo, `_notify_success()` / `_notify_error()`) y pásalos a `run_task`.
- **Permisos de archivos**: Ejecuta como usuario con acceso a la carpeta de destino.
- **Dependencias de conversión**: En Windows, `docx2pdf` requiere Microsoft Word instalado para convertir `.docx` a `.pdf`.

## Desarrollo
- Mantén la lógica de UI en `view/` y la lógica de negocio en `controls/` y `Model/`.
- Usa `show_error_callback` y `show_info_callback` para reportar estado a la UI desde controladores.

## Licencia
MIT
