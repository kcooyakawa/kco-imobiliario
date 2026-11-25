"""Tira nomes de ruas e esquinas dos textos públicos do site (pedido Kco, nov/2026)."""
import re
W=r"[A-ZÁ-Ú][\wÀ-ú\-]+"
ST=rf"(?:(?:Av\.|Avenida|Rua|R\.|Alameda|Al\.|ruas)\s+(?:dos |das |do |da |de |Min\. )?{W}(?: (?:de |do |da |dos )?{W})*|República do Líbano|(?:a |da )?(?:Sabiá|Cotovia|Pintassilgo|Gaivota|Arapanés|Agami|Açocê|Aicás|Inhambu|Jauaperi|Anapurus|Indianópolis|Macuco|Rubem Berta)(?: e (?:dos )?Aicás)?)"
OV={
"Perto da Av. Ibirapuera e do metrô Moema":"Perto do metrô Moema",
"Comércio da Av. Ibirapuera":"Comércio e serviços de Moema",
"Acesso fácil a Congonhas e à Av. Rubem Berta":"Acesso fácil a Congonhas",
"Esquina da Av. Cotovia com a Rua Pintassilgo":"Numa esquina de Moema",
"Design biofílico e uma calçada nova para a Rua Arapapi.":"Design biofílico e calçada revitalizada no entorno.",
"Rua Arapapi revitalizada":"Calçada revitalizada",
"A esquina da Sabiá com a Gaivota, a 850 m do Ibirapuera.":"Uma esquina de Moema, a 850 m do Ibirapuera.",
"Esquina da Av. Sabiá, comércio de bairro e restaurantes":"Comércio de bairro e restaurantes",
"Frentes para a Av. Ibirapuera e a Av. Macuco":"",
"Na Av. República do Líbano, entre Moema e Ibirapuera":"Entre Moema e o Ibirapuera",
"Esquina da Av. Pavão com a Rua Inhambu, Moema Pássaros":"Moema Pássaros",
"Alameda Jauaperi, Moema":"Moema",
"Entre a Av. Agami e a Av. Min. Gabriel de Rezende Passos":"",
"Alameda Jauaperi, rua residencial":"Rua residencial de Moema",
"Comércio da Av. Ibirapuera e de Moema Pássaros":"Comércio de Moema Pássaros",
"Atravessa a quadra entre a Av. Sabiá e a Alameda dos Arapanés":"Terreno que atravessa a quadra",
"Frentes para as ruas Açocê e dos Aicás":"",
"Acesso rápido à Av. Ibirapuera e à Av. Rubem Berta":"Acesso rápido às principais avenidas de Moema",
"Avenida Sabiá, Moema Pássaros":"Moema Pássaros",
"Av. Moema":"",
"Arquitetura nórdica e piscina no rooftop, na Alameda dos Arapanés.":"Arquitetura nórdica e piscina no rooftop.",
"Na Av. República do Líbano, vizinho ao Parque Ibirapuera":"Vizinho ao Parque Ibirapuera",
"Na Av. República do Líbano, perto do Parque Ibirapuera":"Perto do Parque Ibirapuera",
"Esquina da Av. República do Líbano com a Al. Jauaperi":"",
"Esquina da Av. Indianópolis com a Al. dos Anapurus":"",
"na Al. dos Jurupis":"em Moema",
}
SUB=[("pela esquina: Av. Sabiá com Rua Gaivota, a 850","pela localização: a 850"),("no topo da torre da Av. Ibirapuera.","no topo da torre."),("gerações, na Avenida República do Líbano.","gerações."),("Königsberger Vannucchi na Alameda Jauaperi,","Königsberger Vannucchi,")]
rules=[
 (rf",?\s*(?:na |numa )?esquina d[ae] {ST} com (?:a )?{ST}", " numa esquina de Moema"),
 (rf"\s*(?:entre|atravessando a quadra,? da|da) {ST} (?:e|à) (?:a )?{ST}", ""),
 (rf",?\s*(?:com )?(?:acesso|frentes?) (?:pela|para as?|para a) {ST}(?: e (?:a )?{ST})?", ""),
 (rf"\s*(?:na|pela|da|à|perto da|em|e da|e a) {ST}", ""),
 (rf"\s*\b{ST}\b", ""),
]
def clean(t):
    if t in OV: return OV[t]
    for a,b in SUB: t=t.replace(a,b)
    o=t
    for a,b in rules: t=re.sub(a,b,t)
    t=re.sub(r"\s+([,.:])",r"\1",t); t=re.sub(r"\s{2,}"," ",t); t=re.sub(r",\s*,",",",t)
    t=re.sub(r"^\s*[,·\-]\s*","",t).strip()
    t=re.sub(r"^(Esquina|Miolo de Moema),?\s*$","Moema",t)
    t=re.sub(r"^, ?","",t)
    if t and o and o[0].isupper() and t[0].islower(): t=t[0].upper()+t[1:]
    return t
def aplicar(E):
    """Remove ruas/esquinas dos textos (só para o site; o hub usa o JSON completo)."""
    FIELDS=['frase']
    ch=[]
    for e in E:
        f=e.get('ficha') or {}
        def fx(obj,key):
            v=obj.get(key)
            if isinstance(v,str):
                n=clean(v)
                if n!=v: ch.append((e['slug'],key,v,n)); obj[key]=n
        fx(e,'frase')
        for k in ('tagline','conceito','plantas_tit'): fx(f,k)
        if f.get('local'):
            nl=[]
            for x in f['local']:
                n=clean(x)
                if n!=x: ch.append((e['slug'],'local',x,n))
                if n and len(n)>3 and n.lower() not in ('moema','moema pássaros','moema índios') and n not in nl: nl.append(n)
            f['local']=nl
        for lst in ('destaques','tecnica'):
            for r in f.get(lst,[]):
                n=clean(r[1]) if lst=='destaques' else r[1]
                if lst=='tecnica' and re.search(ST,r[1]): n='Moema'
                if n!=r[1]: ch.append((e['slug'],lst,r[1],n)); r[1]=n
        for k in ('lazer','par'):
            for r in (f.get('img') or {}).get(k) or []:
                n=clean(r[1])
                if n!=r[1]: ch.append((e['slug'],'img',r[1],n)); r[1]=n
    return E
