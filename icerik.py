import requests
from bs4 import BeautifulSoup

def get_article_content(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features='html.parser')


    title_tag = soup.find('h1')
    title = title_tag.get_text(strip=True) if title_tag else 'Başlık bulunamadı'


    tarih_tag = soup.find('div', class_='article-date')
    tarih = tarih_tag.get_text(strip=True) if tarih_tag else 'Tarih bulunamadı'


    paragraphs = soup.find_all('p')
    içerik = '\n'.join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])

    sonuc = f"Başlık: {title}\nTarih: {tarih}\nİçerik:\n{içerik}"

    return sonuc

url = 'https://www.sabah.com.tr/spor/futbol/2025/04/06/hat-trick-yapan-taliscadan-galibiyet-yorumu'
print(get_article_content(url))
