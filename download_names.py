#pip install sparqlwrapper
#https://rdflib.github.io/sparqlwrapper/

from SPARQLWrapper import SPARQLWrapper, JSON

print("Querying for data")
offset = 0
total = 0
final = []
#out = open('glossary_names.txt', 'w')
def clean(string: str):
    string = ' '.join(string.split()).strip()
    return string


while total < 4699170:
    try:
        sparql = SPARQLWrapper("http://sitaware.isi.edu:8080/bigdata/namespace/wdq/sparql")
        sparql.setQuery("""SELECT ?Human ?HumanLabel WHERE {
          SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
          ?Human wdt:P31 wd:Q5.
        }
        LIMIT 10000
        OFFSET """+str(offset))
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        #print("Query complete, writing results , offset was - {}".format(offset))
        final.extend(results['results']['bindings'])
        total+=len(results['results']['bindings'])
        print("Query complete, writing results , offset was - {}, total - {}".format(offset, total))
        offset+=10000
    except Exception as e:
        print("Error while fetching from wikidata {}".format(e)) 
print("Writing")
with open('glossary_names.txt', 'w') as out:
    for r in final:
        out.write(clean(r['HumanLabel']['value'])+'\n') 
