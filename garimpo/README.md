# Garimpo W3W Select

Curadoria diária de imóveis de leilão em São Paulo para o **W3W Select Club** (W3W Imóveis, Moema).

Todo dia uma rotina automática varre os leiloeiros e bancos, tria os apartamentos, lê em detalhe os mais promissores e grava o resultado num painel: fotos, mapa, concorrência, a conta do investimento e a nota de cada lote.

> Esta pasta é uma **versão de demonstração** do painel, com os dados reais da rodada de 12/11/2026. Abra o `index.html` no navegador; não precisa de servidor nem de internet (só para as fontes).

## Como ver

1. Baixe ou clone o repositório.
2. Abra `index.html` no Chrome, Safari ou Edge.
3. Clique em qualquer imóvel para abrir a ficha completa (Resumo, Localização, Concorrência, Riscos e documentos).

## O que a máquina faz

| Etapa | O que acontece |
|---|---|
| 1. Fontes | Caixa (lista completa de SP + fichas), Portal Zuk, Mega Leilões, Grupo Lance, Sodré Santoro, Frazão, Sato, Biasi, Freitas, Superbid, portais de bancos e tribunais (TJSP/TRF3/TRT2). |
| 2. Triagem | Descarta o que não fica pelo menos 30% abaixo do **mercado real** (não da avaliação do edital), frações, direitos, usufruto, invasão, edital ausente, leilão encerrado. Faixa: R$ 60 mil a R$ 500 mil de capital do investidor. |
| 3. Due diligence | Edital lido inteiro, matrícula ato por ato, débitos de condomínio e IPTU, ocupação (1 a 5), concorrência em círculos (condomínio, rua, bairro, outros leilões), fotos do imóvel e do prédio, mapa com metrô e entorno. |
| 4. Conta | Custo total = 1,09 × lance + dívidas + reforma + giro + jurídico. Lucro após corretagem (6%) e IR (15%). Lance máximo e ROI comparado ao CDI. |
| 5. Nota | 100 pontos: potencial econômico 35, liquidez 20, risco 25, aderência 10, confiabilidade 10. |
| 6. Status | **Selo Select** só quando tudo está verificado. **Em análise** quando passou na triagem mas falta algo. **Descartado** com o motivo. |

Detalhes em [`docs/metodologia.md`](docs/metodologia.md).

## Rodada de 12/11/2026 em números

- 2.527 apartamentos triados (Caixa, Zuk, Mega)
- 15 lidos em detalhe nesta rodada (29 no painel, somando a rodada parcial da manhã)
- 15 em análise, 14 descartados, 0 com selo Select
- Destaque: apto de 41 m² + vaga na Rua Frei Caneca, 219 (Consolação), 2ª praça a R$ 293,7 mil, cerca de 48% abaixo dos anúncios do mesmo prédio. Pendências: embargos de terceiro e leitura da matrícula.

## Estrutura

```
index.html          painel (versão demonstração, dados embutidos)
data/lotes.json     os 29 lotes da rodada, com análise completa
data/rodadas.json   o resumo da rodada
assets/fotos/       fotos dos anúncios de leilão e dos prédios
assets/mapas/       mapas de entorno (© OpenStreetMap)
docs/metodologia.md regras de triagem, conta e nota
```

## Como funciona em produção

- **Rotina diária:** uma tarefa agendada no Claude roda vinculada ao Mac do escritório e usa o navegador do app para acessar os leiloeiros.
- **Painel ao vivo:** o mesmo `index.html` publicado como página no Claude, lendo os lotes de um banco de dados embutido, que a rotina atualiza todo dia.
- **Imagens:** capturadas no navegador e guardadas junto com o painel.

---

Pré-análise. A validação jurídica final é feita por advogado antes de qualquer lance. Mapas © OpenStreetMap contributors. Fotos: anúncios públicos dos leiloeiros e portais citados em cada lote.
