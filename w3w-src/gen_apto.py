import json
E=json.load(open('empreendimentos.json')); A=json.load(open('apto.json'))
M=['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
def nf(x): return f"{int(x):,}".replace(',','.')
for e in E:
    if e['slug'] not in A or e.get('ficha'): continue
    n,ad,ar,su,pk,tw,fl,lot,un,rd,st,ca,co,fp,rid,asl,ndi,nai,ct,mh=A[e['slug']]
    pronto=st.startswith('Pronto'); e['status']='Pronto' if pronto else 'Em obras'
    y,m,_=rd.split('-'); ent=f"{M[int(m)-1]}/{y}"
    img=lambda kind,i:f"https://api.apto.vc/images/realties/{rid}/{asl}-{kind}-{i}.jpg"
    cond=[img('condominio',i) for i in range(1,ndi+1)]; apt=[img('apartamento',i) for i in range(1,nai+1)]
    plantas=[]
    for f in fp:
        a,b,s,p=map(int,f.split('/'))
        plantas.append(["Studio" if b==0 else f"{b} dorm.", f"{a} m²", f"{s} suíte{'s' if s>1 else ''}" if s else "—", (f"{p} vaga{'s' if p>1 else ''}" if p else "Sem vaga")])
    ass=[[c.split(': ',1)[0],c.split(': ',1)[1]] for c in co][:4]
    des=[]
    if un: des.append([un,"residências"])
    if tw: des.append([tw,"torre" if tw=="1" else "torres"])
    if fl: des.append([fl,"pavimentos"])
    des.append([ar.split(' a ')[-1].split(' e ')[-1],"maior planta"])
    conc=ct or f"{'Torre única' if tw=='1' else (tw+' torres') if tw else 'Projeto'}{' com '+un+' residências' if un else ''}{' em terreno de '+nf(lot)+' m²' if lot else ''}, na {ad}, em Moema."
    tec=[]
    if lot: tec.append(["Terreno",nf(lot)+" m²"])
    if un: tec.append(["Unidades",un])
    tec.append(["Entrega",("Entregue em " if pronto else "Previsão: ")+ent])
    tec.append(["Status","Pronto para morar" if pronto else "Em obras"])
    if e['slug']!='villa-versace-home': e['nome']=n
    e['ficha']={"tagline":e.get('frase') or n,"conceito":conc,"endereco":f"{ad} · Moema","entrega":("Pronto para morar" if pronto else "Previsão: "+ent),"faixa":ar,"plantas_tit":"plantas disponíveis.",
      "assinaturas":ass,"destaques":des[:4],"plantas":plantas,"lazer":ca,"local":(mh[:3] if mh else [f"{ad}, Moema"]),"tecnica":tec,
      "img":{"capa":e['img'],"par":[[cond[0],"Áreas comuns"],[(apt[0] if apt else cond[1]),"Residência" if apt else "Áreas comuns"]],"lazer":[[u,"Lazer"] for u in cond[1:7]]}}
json.dump(E,open('empreendimentos.json','w'),ensure_ascii=False,indent=1)
print(sum(1 for e in E if e.get('ficha')), [e['slug'] for e in E if e['bairro_slug']=='moema' and not e.get('ficha')])
