
"""2. Automatización con scraping (Nivel Intermedio)
Enunciado: Crea un script en Python que, haga lo siguiente:
• Tome una palabra clave de búsqueda (puede ser una variable palabra = "laptop").
• Ingrese a la tienda virtual (Puede ser Mercado libre o Amazon)
• Extraiga los títulos y precios de los primeros 5 productos que coincidan.
• Permite cambiar la palabra clave fácilmente.
Consideraciones:
• Solo impresión en consola.
• El script debe permitir cambiar fácilmente el término de búsqueda."""

import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox, scrolledtext

def buscar_productos():
    palabra_clave = entrada.get().strip()
    
    if palabra_clave == "":
        messagebox.showwarning("Atención", "Por favor escribe algo para buscar.")
        return
    
    url = "https://listado.mercadolibre.com.co/" + palabra_clave
    
    #Esto ayuda que MercadoLibre no me bloquee la búsqueda ni me tome como un bot
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    try:
        #Pedir la página web
        respuesta = requests.get(url, headers=headers)
        respuesta.raise_for_status()  #verifica que no haya error
        
        #Leer contenido de la página
        pagina = BeautifulSoup(respuesta.text, "html.parser")
        
        #Busca productos en la página
        productos = pagina.find_all("div", class_="poly-card__content")
        
        #Limpiarla caja de resultados
        resultados.delete("1.0", tk.END)
        
        resultados.insert(tk.END, f"Resultados para: {palabra_clave}\n\n")
        
        #mostrar 5 productos
        count = 0
        for producto in productos:
            if count == 5:
                break
            
            #título del producto
            titulo = producto.find("a", class_="poly-component__title")
            if titulo:
                titulo_texto = titulo.text.strip()
            else:
                titulo_texto = "Sin título"
            
            #precio del producto
            precio_div = producto.find("div", class_="poly-price__current")
            if precio_div:
                moneda = precio_div.find("span", class_="andes-money-amount__currency-symbol")
                valor = precio_div.find("span", class_="andes-money-amount__fraction")
                if moneda and valor:
                    precio_texto = moneda.text.strip() + valor.text.strip()
                else:
                    precio_texto = "Precio no disponible"
            else:
                precio_texto = "Precio no disponible"
            
            # Mostrar el producto en el cuadro de resultados
            resultados.insert(tk.END, f"Producto {count + 1}:\n")
            resultados.insert(tk.END, f"Título: {titulo_texto}\n")
            resultados.insert(tk.END, f"Precio: {precio_texto}\n")
            resultados.insert(tk.END, "-"*40 + "\n")
            
            count += 1
        
        if count == 0:
            resultados.insert(tk.END, "No se encontraron productos.")
    
    except:
        # Por si pasa algun error se muestra.
        messagebox.showerror("Error", "No se pudo conectar o cargar los datos.")

#Ventana principal
ventana = tk.Tk()
ventana.title("Buscador Mercado Libre")
ventana.geometry("600x400")

#Texto palabra clave
tk.Label(ventana, text="Palabra clave:").pack(pady=5)
entrada = tk.Entry(ventana, width=40)
entrada.pack()

#Botón para buscar
boton = tk.Button(ventana, text="Buscar", command=buscar_productos)
boton.pack(pady=10)

#mostrar resultados
resultados = scrolledtext.ScrolledText(ventana, width=70, height=20)
resultados.pack(pady=5)

#Mostrar la ventana
ventana.mainloop()

