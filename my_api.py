import os
from bs4 import BeautifulSoup
import random
import requests
from dotenv import load_dotenv

load_dotenv()

URL=os.getenv("url")
list_agent =os.getenv("list_Agent")
headers = {
    "User-Agent": random.choice(list_agent),
    "Accept-Language": "es-ES,es:q=0.9"
}

try:
    page = requests.get(URL, headers=headers)

    if page.status_code == 200:
        print("Conexion exitosa")


        with open("pagina.html", "w", encoding="utf-8") as f:
            f.write(page.text)


        soud = BeautifulSoup(page.content, 'html.parser')
        selector = "#items\[0\.base\]\[customerVisiblePrice\]\[displayString\]"
        # Busca cualquier input que tenga "customerVisiblePrice" en su ID
        precio_produc = soud.select_one(selector)
    
        if precio_produc:
            precio_sucio = precio_produc.get('value', "")
            print(f"Texto extraido: {precio_sucio}")

            precio_limpio = "".join(c for c in precio_sucio if c.isdigit() or c == '.')
            precio_final = float(precio_limpio)

            print(f"El precio final: {precio_final}")

            if precio_final < 700:
                print("¡BAJÓ DE PRECIO! Deberías comprarlo.")
            else:
                print("Sigue por encima del presupuesto.")

        else:
            print("No se encontró el elemento. Puede que el ID haya cambiado.")
    else:
        print(f"Error de acceso: Código {page.status_code}")


except Exception as e:
    print(f"Ocurrio un error inesperado: {e}")

#<input type="hidden" name="items[0.base][customerVisiblePrice][displayString]" value="US$714.00" id="items[0.base][customerVisiblePrice][displayString]">

##items\[0\.base\]\[customerVisiblePrice\]\[displayString\]