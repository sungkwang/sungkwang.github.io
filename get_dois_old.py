import urllib.request, urllib.parse, json, time

queries = [
    'Damage biomechanics for neuronal membrane mechanoporation',
    'Free volume and structural evolution during creep in amorphous polyethylene by atomistic molecular dynamic simulations',
    'A dispersion-corrected modified embedded-atom method bond order interatomic potential for sulfur',
    'Molecular dynamics simulations showing 1-palmitoyl-2-oleoyl-phosphatidylcholine (POPC) membrane mechanoporation damage under different strain paths',
    'Stress wave mitigation at suture interfaces',
    'Interatomic potential for hydrocarbons on the basis of the modified embedded-atom method with bond order (MEAM-BO)',
    'Uncertainty analysis of an irrigation scheduling model for water management in crop production'
]

results = []
for q in queries:
    url = 'https://api.crossref.org/works?query.title=' + urllib.parse.quote(q) + '&rows=1'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'mailto:test@example.com'})
        resp = urllib.request.urlopen(req)
        data = json.loads(resp.read())
        if data['message']['items']:
            item = data['message']['items'][0]
            doi = item.get('DOI', '')
            url_link = item.get('URL', 'https://doi.org/' + doi)
            results.append({'query': q, 'doi': doi, 'url': url_link})
        else:
            results.append({'query': q, 'doi': None, 'url': None})
    except Exception as e:
        results.append({'query': q, 'error': str(e)})
    time.sleep(0.5)

with open('dois_old.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)
