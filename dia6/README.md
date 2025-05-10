# Entornos virtuales

## Crear un entorno virtual

```bash
python -m venv nombre_del_entorno
```

## Activar un entorno virtual

```bash
nombre_del_entorno\Scripts\activate # Windows
source nombre_del_entorno/Scripts/activate # Git Bash
source nombre_del_entorno/bin/activate # Linux y Mac
```

## Desactivar un entorno virtual

```bash
deactivate
```

## Instalar paquetes en un entorno virtual

```bash
pip install nombre_del_paquete
```

## Crear un archivo con todas los paquetes necesarios: `requirements.txt`

```bash
pip freeze > requirements.txt
```

## Instalar paquetes del archivo `requirements.txt`

```bash
pip install -r requirements.txt
```