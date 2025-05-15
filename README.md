# 🧾 Proceso ETL desde PDF con Flask

Este proyecto es una aplicación web sencilla desarrollada con Flask. Permite subir un archivo PDF, extraer su contenido textual usando Python y mostrarlo de forma ordenada en una página HTML.

## 📌 Objetivo

Implementar un proceso ETL (Extracción, Transformación y Carga) desde archivos PDF, utilizando herramientas de backend y una interfaz web amigable.

---

## 🧰 Tecnologías Utilizadas

- Python 3.8+
- Flask
- pdfplumber (para extracción de texto)
- HTML + CSS

---

## 🚀 Instrucciones para ejecutar el proyecto

### 1. Crear y activar un entorno virtual

```bash
python -m venv venv
# En Linux/macOS:
source venv/bin/activate
# En Windows:
venv\Scripts\activate
```

### 2. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar la aplicación

```bash
python run.py
```

Accede a la aplicación en tu navegador: [http://localhost:5000](http://localhost:5000)

---

## 📂 Estructura del Proyecto

```
flask-etl-pdf/
├── app/
│   ├── __init__.py          # Configuración de la aplicación Flask
│   ├── routes.py            # Rutas principales de la aplicación
│   ├── utils.py             # Funciones auxiliares (como extracción de texto del PDF)
│   ├── templates/
│   │   ├── base.html        # Plantilla base para HTML
│   │   ├── upload.html      # Página para cargar el archivo PDF
│   │   └── result.html      # Página para mostrar el contenido del PDF
│   ├── static/
│   │   └── styles.css       # Archivo CSS para estilos básicos
├── uploads/                 # Carpeta para almacenar los archivos PDF cargados
├── requirements.txt         # Dependencias del proyecto
├── run.py                   # Punto de entrada para ejecutar la aplicación
└── README.md                # Documentación del proyecto
```

---

## ✅ Funcionalidades

- Cargar archivos PDF desde la interfaz web.
- Extraer texto del PDF usando `pdfplumber`.
- Mostrar el contenido extraído de forma ordenada.
- Estilo básico con CSS personalizado.

---

## ✍️ Autor

Julian Marin  
[LinkedIn](https://www.linkedin.com/in/julian-camilo-marin-monsalve-6b4331221/) | [GitHub](https://github.com/camilomarin60)
