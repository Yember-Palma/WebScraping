import requests
from urllib.parse import urlparse

def es_link_valido(url, dominio_esperado):
    try:
        # 1. Analizar la estructura
        parsed = urlparse(url)
        if parsed.scheme != "https":
            return False, "No es una conexión segura (HTTPS)"
        
        if dominio_esperado not in parsed.netloc:
            return False, f"El dominio no coincide con {dominio_esperado}"

        # 2. Hacer una petición rápida (HEAD es más rápido que GET)
        # Solo pedimos los encabezados, no descargamos toda la página
        response = requests.head(url, timeout=5, allow_redirects=True)
        
        if response.status_code == 200:
            return True, "Link verificado y activo"
        else:
            return False, f"El link existe pero devolvió error {response.status_code}"

    except Exception as e:
        return False, f"Error al conectar: {e}"

# Ejemplo de uso:
es_real, mensaje = es_link_valido("https://forms.gle/rBnj5D4dH2UC3XPA6", "forms.gle")
print(mensaje)