"""3. Consumo de API con interfaz y autenticación (Nivel Intermedio/Avanzado)
Enunciado: Crea una aplicación en Python que:
• Use algun módulo gráfico para mostrar una ventana de login.
• Utilice una base de datos SQLite para validar si el usuario está registrado.
• Si el usuario no existe, puede mostrar un mensaje de error (no se requiere registrar
usuarios).
• Al hacer login correctamente, se muestre información proveniente de una API
pública, por ejemplo: (Api del clima, Api de Rick and Morty o a su eleccion)
Requisitos técnicos:
• Base de datos SQLite con una tabla usuarios (username TEXT, password TEXT).
• Validación del usuario con consulta SQL.
• Si el login es exitoso, se muestra la lista de usuarios obtenidos desde la API.
• Interfaz simple con campo usuario, contraseña, botón login."""



import tkinter as tk
from tkinter import messagebox
import sqlite3
import requests
import os
from PIL import Image, ImageTk
import io

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login")
        self.root.geometry("350x200")
        self.root.resizable(False, False)

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.failed_attempts = 0

        self.create_widgets()
        self.init_database()

    def create_widgets(self):
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(main_frame, text="Usuario:").grid(row=0, column=0, sticky=tk.W, pady=10)
        tk.Label(main_frame, text="Contrase\u00f1a:").grid(row=1, column=0, sticky=tk.W, pady=10)

        tk.Entry(main_frame, textvariable=self.username_var).grid(row=0, column=1, padx=10, pady=10)
        tk.Entry(main_frame, textvariable=self.password_var, show="*").grid(row=1, column=1, padx=10, pady=10)

        login_button = tk.Button(main_frame, text="Iniciar Sesi\u00f3n", command=self.validate_login)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def init_database(self):
        if not os.path.exists("users.db"):
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL
                )
            ''')
            usuarios_prueba = [
                ("admin", "admin"),
                ("usuario", "password"),
                ("test", "test123")
            ]
            cursor.executemany("INSERT OR IGNORE INTO usuarios VALUES (?, ?)", usuarios_prueba)
            conn.commit()
            conn.close()

    def validate_login(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if not username or not password:
            messagebox.showerror("Error", "Por favor, complete todos los campos")
            return

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        with open("log.txt", "a") as f:
            f.write(f"{username} intent\u00f3 iniciar sesi\u00f3n. Resultado: {'Correcto' if user else 'Fallido'}\n")

        if user:
            self.failed_attempts = 0
            self.root.withdraw()
            self.open_api_window()
        else:
            self.failed_attempts += 1
            if self.failed_attempts >= 3:
                messagebox.showerror("Error", "Demasiados intentos fallidos. Cerrando aplicaci\u00f3n.")
                self.root.destroy()
            else:
                messagebox.showerror("Error", "Usuario o contrase\u00f1a incorrectos")

    def open_api_window(self):
        api_window = tk.Toplevel(self.root)
        api_window.title("Datos de Rick and Morty API")
        api_window.geometry("700x500")
        api_window.protocol("WM_DELETE_WINDOW", lambda: self.logout(api_window))

        logout_button = tk.Button(api_window, text="Cerrar Sesi\u00f3n", command=lambda: self.logout(api_window))
        logout_button.pack(pady=10)

        main_frame = tk.Frame(api_window)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        canvas = tk.Canvas(main_frame)
        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        try:
            response = requests.get("https://rickandmortyapi.com/api/character")
            if response.status_code == 200:
                data = response.json()
                characters = data.get("results", [])

                tk.Label(scrollable_frame, text="Personajes de Rick and Morty", font=("Arial", 14, "bold")).pack(pady=10)

                for character in characters:
                    frame = tk.Frame(scrollable_frame, relief=tk.RIDGE, bd=2)
                    frame.pack(fill=tk.X, padx=5, pady=5)

                    img_data = requests.get(character['image']).content
                    img = Image.open(io.BytesIO(img_data)).resize((100, 100))
                    photo = ImageTk.PhotoImage(img)

                    img_label = tk.Label(frame, image=photo)
                    img_label.image = photo
                    img_label.pack(side="left", padx=10)

                    info_frame = tk.Frame(frame)
                    info_frame.pack(side="left", fill=tk.X)

                    tk.Label(info_frame, text=f"Nombre: {character['name']}").pack(anchor="w")
                    tk.Label(info_frame, text=f"Estado: {character['status']}").pack(anchor="w")
                    tk.Label(info_frame, text=f"Especie: {character['species']}").pack(anchor="w")
                    tk.Label(info_frame, text=f"Origen: {character['origin']['name']}").pack(anchor="w")
            else:
                tk.Label(scrollable_frame, text=f"Error al obtener datos: {response.status_code}").pack()
        except Exception as e:
            tk.Label(scrollable_frame, text=f"Error: {str(e)}").pack()

    def logout(self, window):
        window.destroy()
        self.root.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
