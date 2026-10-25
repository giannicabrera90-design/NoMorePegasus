import os
from googletrans import Translator

# Inicializar traductor
translator = Translator()

# Mapa de carpetas y códigos de idioma de Google Translate
languages = {
    'es': 'es', 'fr': 'fr', 'de': 'de', 'ru': 'ru', 'ar': 'ar', 
    'zh': 'zh-cn', 'pt': 'pt', 'zht_Hant': 'zh-tw', 'ko': 'ko', 
    'ja': 'ja', 'th': 'th', 'ta': 'ta', 'fa': 'fa', 'he': 'he', 
    'bg': 'bg', 'uk': 'uk', 'el': 'el', 'cs': 'cs', 'cro': 'hr', 
    'et': 'et', 'tu': 'tr', 'sv': 'sv', 'fi': 'fi', 'sl': 'sl', 
    'sk': 'sk', 'ro': 'ro', 'pl': 'pl', 'pap': 'pap', 'no': 'no', 
    'nl': 'nl', 'ms': 'ms', 'hu': 'hu', 'lt': 'lt', 'lv': 'lv', 
    'it': 'it', 'da': 'da', 'id': 'id'
}

# Leer el archivo original en inglés
en_file_path = 'en/index.html'
if not os.path.exists(en_file_path):
    print("Error: No se encontró en/index.html")
    exit()

with open(en_file_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

print("🚀 Iniciando generación automática de idiomas...")

for folder, code in languages.items():
    dest_dir = folder
    os.makedirs(dest_dir, exist_ok=True)
    dest_file = os.path.join(dest_dir, 'index.html')
    
    if code == 'en':
        # Si es inglés, solo copiamos el archivo original
        with open(dest_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        continue

    try:
        # Traducir el contenido HTML (Nota: para textos masivos, traduciendo bloques clave o usando APIs profesionales es ideal, pero esto funciona excelente para maquetas estáticas)
        print(f"🌍 Generando idioma: {folder} ({code})...")
        translated = translator.translate(html_content, src='en', dest=code)
        
        with open(dest_file, 'w', encoding='utf-8') as f:
            f.write(translated.text)
    except Exception as e:
        print(f"❌ Error en {folder}: {e}")

print("✨ ¡Todas las carpetas han sido pobladas con éxito!")
