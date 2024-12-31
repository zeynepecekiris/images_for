import os
import requests
from bs4 import BeautifulSoup

# HTML dosyasını oku
with open('file.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# BeautifulSoup ile HTML'yi analiz et
soup = BeautifulSoup(html_content, 'html.parser')

# Resim kaynaklarını topla
image_sources = []
for img in soup.find_all('img'):
    src = img.get('src')
    if src:
        # Unicode kaçış karakterlerini düzelt
        decoded_src = src.encode('utf-8').decode('unicode-escape')
        image_sources.append(decoded_src)

# Resimlerin kaydedileceği klasör
output_folder = "images"
os.makedirs(output_folder, exist_ok=True)

# Resimleri indir ve kaydet
for i, src in enumerate(image_sources):
    # URL tam değilse tamamla (örnek: yemeksepeti.com ekle)
    if not src.startswith('http'):
        src = 'https://www.yemeksepeti.com' + src

    try:
        response = requests.get(src)
        response.raise_for_status()  # Hata kontrolü

        # Resmi dosyaya kaydet
        image_path = os.path.join(output_folder, f'image_{i + 1}.jpg')
        with open(image_path, 'wb') as image_file:
            image_file.write(response.content)
        print(f"Kaydedildi: {image_path}")
    except Exception as e:
        print(f"Resim indirilemedi: {src}, Hata: {e}")
