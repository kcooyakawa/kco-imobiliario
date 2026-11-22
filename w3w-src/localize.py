"""Baixa imagens externas do cadastro para w3w-img/<slug>/ (1400px) + t/ (760px) e troca as URLs."""
import json,re,hashlib,os,io,glob,urllib.request
from PIL import Image
try: import pillow_avif  # noqa
except Exception: pass
BASE='https://kcooyakawa.github.io/kco-imobiliario/w3w-img/'
ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','w3w-img')
ok=fail=0
def get(u,slug):
    global ok,fail
    name='x-'+hashlib.md5(u.encode()).hexdigest()[:10]+'.jpg'
    d=os.path.join(ROOT,slug);p=os.path.join(d,name)
    if not os.path.exists(p):
        try:
            r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0','Referer':'https://'+u.split('/')[2]+'/'}),timeout=40).read()
            im=Image.open(io.BytesIO(r)).convert('RGB')
            os.makedirs(os.path.join(d,'t'),exist_ok=True)
            a=im.copy();a.thumbnail((1400,1400));a.save(p,quality=72,optimize=True,progressive=True)
            im.thumbnail((760,760));im.save(os.path.join(d,'t',name),quality=68,optimize=True,progressive=True)
        except Exception as ex:
            print('FAIL',u,ex);fail+=1;return u
    ok+=1;return BASE+slug+'/'+name
def walk(o,slug):
    if isinstance(o,str):
        if o.startswith('http') and 'kcooyakawa.github.io' not in o and re.search(r'\.(jpe?g|png|webp|avif)(\?|$)',o,re.I): return get(o,slug)
        return o
    if isinstance(o,dict): return {k:walk(v,slug) for k,v in o.items()}
    if isinstance(o,list): return [walk(v,slug) for v in o]
    return o
E=[walk(e,e['slug']) for e in json.load(open('empreendimentos.json'))]
json.dump(E,open('empreendimentos.json','w'),ensure_ascii=False,indent=1)
for f in glob.glob('fichas/*.json'):
    s=os.path.basename(f)[:-5];json.dump(walk(json.load(open(f)),s),open(f,'w'),ensure_ascii=False)
print('ok',ok,'fail',fail)
