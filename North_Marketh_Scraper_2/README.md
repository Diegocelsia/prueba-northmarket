# 🚀 North_Marketh_Scraper_2

## 📌 Descripción del Proyecto

North_Marketh_Scraper_2 es una herramienta de scraping de Instagram 🕵️‍♂️ diseñada para extraer información de los seguidores de cuentas objetivo específicas. 

Su propósito principal es recopilar datos relevantes como:
- 👤 Nombres de usuario
- 📝 Biografías
- 📧 Información de contacto (correo y teléfono)
- 📅 Fecha de la última actividad del seguidor

Además, el proyecto incluye una aplicación web interactiva desarrollada con Streamlit 🌐 para visualizar y filtrar los datos de los seguidores recopilados.

Este proyecto resuelve la necesidad de obtener información de contacto potencialmente valiosa de los seguidores de cuentas de Instagram de interés.  
💼 Útil para estrategias de marketing, análisis de mercado o prospección de leads.

## ✨ Características Principales

🔍 **Extracción de Datos de Seguidores**:  
Scrapea nombres de usuario, nombres completos, biografías, correos electrónicos, números de teléfono y la fecha de la última publicación de los seguidores.

📩 **Identificación de Información de Contacto**:  
Utiliza expresiones regulares para identificar automáticamente correos electrónicos y números de teléfono dentro de las biografías de los usuarios.

🔐 **Gestión de Sesiones de Instagram**:  
Carga y guarda sesiones de Instaloader para evitar tener que iniciar sesión repetidamente.

🖥️ **Interfaz de Usuario Interactiva (Streamlit)**:  
Permite filtrar y visualizar los datos de los seguidores por cuenta de origen y probabilidad de contacto.

📤 **Exportación de Datos**:  
Facilita la descarga de los datos filtrados en formato CSV.

🎯 **Cuentas Objetivo Configurables**:  
Permite definir fácilmente las cuentas de Instagram de las que se desea extraer seguidores.

## 🛠️ Tecnologías Utilizadas

🐍 Python: Lenguaje de programación principal.  
📸 Instaloader: Biblioteca de Python para interactuar con Instagram.  
📊 Pandas: Para la manipulación y análisis de datos en formato de tabla.  
🌐 Streamlit: Para la creación de la aplicación web interactiva.  
🔐 python-dotenv: Para la gestión de variables de entorno (credenciales).  
📘 openpyxl: Para la lectura de archivos Excel.

______________________________

## ⚙️ Instalación y Configuración

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:

1. Clona el repositorio (si aplica):

```bash
git clone <URL_DEL_REPOSITORIO>
cd North_Marketh_Scraper_2
```

2. Crea un entorno virtual (recomendado):

```bash
python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate     # En Windows
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Crea el archivo de configuración de entorno:
Crea un archivo llamado ```.env``` en la raíz del proyecto y añade tus credenciales de Instagram. ⚠️ Nunca compartas este archivo ni lo subas a un repositorio público.

```bash
IG_USERNAME=tu_nombre_de_usuario_de_instagram
IG_PASSWORD=tu_contraseña_de_instagram
```


🔒  Nota: Si el archivo ```.env``` ya existe con tu nombre de usuario, la contraseña se solicitará por consola la primera vez que ejecutes ```scraper.py```


## ▶️ Uso
1. Ejecutar el Scraper
Para iniciar el proceso de extracción de datos de Instagram, ejecuta el script scraper.py:



```bash
  python scraper.py
```

Este script iniciará sesión en Instagram, cargará o guardará tu sesión, y comenzará a recopilar información de los seguidores de las cuentas definidas en la variable ```targets``` dentro de ```scraper.py``` (por defecto: ```"elcorteingles"```, ```"mercadona"```, ```"carrefoures"```). 
📁 Los datos se guardarán en un archivo llamado ```seguidores.xlsx```.


2. Ejecutar la Aplicación Web de Análisis
Una vez que tengas el archivo ```seguidores.xlsx``` generado, puedes iniciar la aplicación Streamlit para visualizar y filtrar los datos:


```bash
streamlit run app.py
```



Esto abrirá la aplicación en tu navegador web 🌍. Podrás filtrar los datos por "Cuenta Origen" y por "Probabilidad de contacto", y descargar los resultados filtrados como un archivo CSV.

## 🗂️ Estructura del Proyecto

```.env```: Almacena de forma segura las credenciales de Instagram.

```Explicacion.mp4```: Un video explicativo del proyecto.

```app.py```: El script de la aplicación web interactiva construida con Streamlit.

```config.py```: Maneja la carga de las variables de entorno para las credenciales.

```diegoenrisu02.session```: Archivo de sesión de Instaloader que guarda los datos de inicio de sesión para evitar reconexiones.

```requirements.txt```: Lista de todas las dependencias necesarias del proyecto.

```scraper.py```: El script principal encargado de la extracción de datos de Instagram.

```seguidores.xlsx```: El archivo de salida generado por ```scraper.py``` que contiene los datos de los seguidores.




