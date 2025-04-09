import requests
from bs4 import BeautifulSoup

url = 'https://www.sabah.com.tr/spor/futbol/2025/04/06/hat-trick-yapan-taliscadan-galibiyet-yorumu'

def abc(sayfa_url):
    r = requests.get(sayfa_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    title = soup.find("title").get_text(strip=True)
    meta_date = soup.find("meta", attrs={"name": "datePublished"})
    tarih = meta_date["content"]

 
    content_div = soup.find("article")
    if content_div is None:
        content_div = soup.find("div", class_="newsBox")
        if content_div is None:
            print("Article content not found. Check HTML structure.")
            return title, tarih, "" 

    paragraf = content_div.find_all("p")
    icerik = "\n".join(p.get_text(strip=True) for p in paragraf)

    return title, tarih, icerik

title, tarih, icerik = abc(url)
print("baslık:", title)
print("Tarih:", tarih)
print("İçerik:",icerik)
