from rdflib import Graph
from rdflib.namespace import RDF, SKOS, DCTERMS, OWL

g = Graph()
g.parse("../wrb-codelists.ttl")

ttl = "Codelists" # default title
desc = "A series of codelists" # default description

for s, p, o in g.triples((None, RDF.type, OWL.Ontology)):
    ttl = g.value(s,DCTERMS.title)
    desc = g.value(s,DCTERMS.description) + "<br/>"
    for t in ["creator","rights","source"]:
        if g.value(s,DCTERMS[t]):
            desc += "<br/><b>"+t+"</b>: " + str(g.value(s,DCTERMS[t]))

html = "<h1>"+ttl+"</h1><p>"+desc+"</p>"

html += "<h2 id='#top'>Contents</h2><p><ul>"
for s, p, o in g.triples((None, RDF.type, SKOS.ConceptScheme)):    
    html += "<li><a href='#"+str(s)+"'>" + g.value(s,SKOS.prefLabel) + "</a></li>"
html += "</ul></p><hr/>\n"

for s, p, o in g.triples((None, RDF.type, SKOS.ConceptScheme)):    
    html += "<h2 id='"+str(s)+"'>" + g.value(s,SKOS.prefLabel) + "</h2>\n"
    html += "<table><tr><th>Code</th><th>Label</th><th>Definition</th></tr>\n"
    for s2, p2, o2 in g.triples((None, SKOS.inScheme, s)): 
        html += "<tr><td>"+g.value(s2,SKOS.notation)+"</td><td>"+ g.value(s2,SKOS.prefLabel) + "</td><td>" + g.value(s2,SKOS.definition) +"</td></tr>\n"
    html += "<br/><a href='#top'>&#8657; Index</a><hr/>"

f = open("../index.html", "w")
f.write("<html>\n<head><title>"+ttl+"</title></head>\n<body>"+html+"</body>\n<style> body {font-family: arial} td, th {border: 1px solid gray;padding:5px} th { background-color: #efefef } table{border-collapse: collapse}</style></html>")
f.close()