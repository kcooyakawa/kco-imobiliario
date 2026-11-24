"""Baixa vídeos e fotos do site antigo (w3wlp.netlify.app) para w3w-img/site/."""
import os, urllib.request
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'w3w-img', 'site')
FILES = ['v/cidade.mp4', 'v/cidade.jpg', 'v/territorio.mp4', 'v/territorio.jpg', 'v/torre.mp4', 'v/torre.jpg',
         'img/socio-kco.jpg', 'img/socio-wilson.jpg', 'img/socio-yoko.jpg']
for f in FILES:
    p = os.path.join(ROOT, f)
    if os.path.exists(p):
        continue
    os.makedirs(os.path.dirname(p), exist_ok=True)
    try:
        d = urllib.request.urlopen(urllib.request.Request('https://w3wlp.netlify.app/' + f, headers={'User-Agent': 'Mozilla/5.0'}), timeout=120).read()
        open(p, 'wb').write(d)
        print('ok', f, len(d))
    except Exception as e:
        print('FAIL', f, e)
