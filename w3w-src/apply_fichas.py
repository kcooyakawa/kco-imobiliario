import json,glob,os
E=json.load(open('empreendimentos.json'))
by={e['slug']:e for e in E}
for f in sorted(glob.glob('fichas/*.json')):
    s=os.path.basename(f)[:-5]; o=json.load(open(f))
    if s not in by: print('??',s); continue
    by[s].update(o)
json.dump(E,open('empreendimentos.json','w'),ensure_ascii=False,indent=1)
print(len(glob.glob('fichas/*.json')),'fichas aplicadas')
