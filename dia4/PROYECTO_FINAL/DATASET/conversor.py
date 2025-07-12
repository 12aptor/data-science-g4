import os
from PIL import Image

# Directorios de entrada y salida
input_dirs = ['train', 'test', 'validation']
base_input = './'
base_output = './comprimidos'

# Parámetros de redimensionamiento
size = (128, 128)
output_ext = '.jpeg'

# Crear estructura de carpetas en el directorio de salida
for dir_name in input_dirs:
    for subfolder in ['NORMAL', 'PNEUMONIA']:
        out_path = os.path.join(base_output, dir_name, subfolder)
        os.makedirs(out_path, exist_ok=True)

# Procesar imágenes
for dir_name in input_dirs:
    for subfolder in ['NORMAL', 'PNEUMONIA']:
        in_path = os.path.join(base_input, dir_name, subfolder)
        out_path = os.path.join(base_output, dir_name, subfolder)
        if not os.path.exists(in_path):
            continue
        for filename in os.listdir(in_path):
            file_path = os.path.join(in_path, filename)
            if not os.path.isfile(file_path):
                continue
            try:
                with Image.open(file_path) as img:
                    img = img.convert('RGB')
                    img = img.resize(size, Image.LANCZOS)
                    out_file = os.path.splitext(filename)[0] + output_ext
                    out_file_path = os.path.join(out_path, out_file)
                    img.save(out_file_path, 'JPEG', quality=85)
                    print(f'Imagen comprimida: {out_file_path}')
            except Exception as e:
                print(f'Error procesando {file_path}: {e}')