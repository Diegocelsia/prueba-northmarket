import instaloader
from config import IG_USERNAME
import pandas as pd
import re
from datetime import datetime
import time
import os


L = instaloader.Instaloader()


SESSION_FILE = f"{IG_USERNAME}.session"

try:
    if os.path.exists(SESSION_FILE):
        L.load_session_from_file(IG_USERNAME, SESSION_FILE)
        print("✅ Sesión cargada desde archivo.")
    else:
        IG_PASSWORD = input("🔐 Introduce tu contraseña de Instagram: ")
        L.login(IG_USERNAME, IG_PASSWORD)
        L.save_session_to_file(SESSION_FILE)
        print("✅ Sesión iniciada y guardada correctamente.")
except Exception as e:
    print("❌ Error al iniciar sesión:", e)
    exit()

targets = ["elcorteingles","mercadona","carrefoures"]
followers_data = []

def extract_contact_info(bio):
    email = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", bio)
    phone = re.findall(r"\+?\d[\d -]{7,}\d", bio)
    return email, phone

for account in targets:
    print(f"\nAnalizando seguidores de @{account}...")
    try:
        profile = instaloader.Profile.from_username(L.context, account)
    except Exception as e:
        print(f"No se pudo acceder a @{account}: {e}")
        continue

    count = 0
    try:
        followers = profile.get_followers()
    except Exception as e:
        print(f"Error al obtener seguidores de @{account}: {e}")
        continue

    for follower in followers:
        if count >= 30:
            break

        try:
            bio = follower.biography or ""
            full_name = follower.full_name
            username = follower.username
            email, phone = extract_contact_info(bio)

            try:
                date_joined = next(follower.get_posts()).date_utc
                fecha_actividad = date_joined.strftime("%Y-%m-%d")
            except Exception:
                fecha_actividad = "N/A"

            followers_data.append({
                "Cuenta Origen": account,
                "Nombre completo": full_name,
                "Usuario": username,
                "Biografía": bio,
                "Correo": ", ".join(email) if email else "",
                "Teléfono": ", ".join(phone) if phone else "",
                "Fecha actividad": fecha_actividad,
                "Privado": "Sí" if follower.is_private else "No",
                "Probabilidad contacto": int(bool(email)) + int(bool(phone)) + int(fecha_actividad != "N/D")
            })

            print(f"{username} revisado.")
            count += 1
            time.sleep(5)
        except Exception as e:
            print(f"⚠️ Error al analizar un seguidor: {e}")
            time.sleep(10)
            continue

if not followers_data:
    print("⚠️ No se extrajo ningún dato. Prueba con otras cuentas.")
else:
    df = pd.DataFrame(followers_data)
    df.to_excel("seguidores.xlsx", index=False)
    print("Archivo generado: seguidores.xlsx")
