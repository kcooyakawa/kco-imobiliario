"""Fotos de capa das categorias do Guia Moema sem foto própria (Unsplash, licença livre).
Baixa para w3w-img/moema/<categoria>.jpg (4:5, 1200x1500). Roda no GitHub Actions (w3w-localize.yml)."""
import os, io, urllib.request
from PIL import Image
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'w3w-img', 'moema')
CAPAS = {  # categoria: id da foto no Unsplash
 'academias': 'GNWUPn44-eg', 'hoteis': 'vEO-8ck28fY', 'mercados': 'JqSMv9pxPrE', 'farmacias': 'tvP6pCnq9iI',
 'cabeleireiros': 'dU6eE_j2My8', 'pet': '-p3TjyQULhU', 'escolas': 'RTFX0TQHXko', 'concessionarias': 'OZPoquurg68',
 'estetica': 'Xa8fX8bQCgs', 'faculdades': 'bz4vI87iRQc', 'oficinas': 'rU_bvNfr8pQ', 'postos': 'fV09F4rQS-o',
 'saude': 'g0PTp89dumc',
}
def baixar():
    for cat, pid in CAPAS.items():
        p = os.path.join(ROOT, cat + '.jpg')
        if os.path.exists(p): continue
        try:
            d = urllib.request.urlopen(urllib.request.Request(f'https://unsplash.com/photos/{pid}/download?force=true', headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read()
            im = Image.open(io.BytesIO(d)).convert('RGB'); w, h = im.size; r = 4 / 5
            if w / h > r: nw = int(h * r); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
            else: nh = int(w / r); im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
            im = im.resize((1200, 1500), Image.LANCZOS); im.save(p, quality=78, optimize=True, progressive=True)
            print('ok', cat)
        except Exception as e:
            print('FAIL', cat, e)
if __name__ == '__main__': baixar()
