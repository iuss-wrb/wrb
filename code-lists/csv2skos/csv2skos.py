import csv
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import DC, DCTERMS, FOAF, OWL, RDF, RDFS, SKOS, XMLNS, XSD

def valuri(data):
    return "".join(x for x in data.replace(' ','-') if (x.isalnum() or x =='-'))

g = Graph()
WRB = Namespace("http://iuss-wrb.github.io/wrb#")

ont = URIRef("http://iuss-wrb.github.io/wrb#")
g.add((ont, RDF.type, OWL.Ontology))
g.add((ont, DCTERMS.description, Literal("Code lists to describe soil properties as defined by the IUSS WRB working group")))
g.add((ont, DCTERMS.creator, URIRef("https://orcid.org/0000-0003-1499-618X")))
g.add((ont, DCTERMS.rights, Literal("This ontology is distributed under Creative Commons Attribution 4.0 License - https://creativecommons.org/licenses/by/4.0")))
g.add((ont, DCTERMS.source, URIRef("https://wrb.isric.org/files/WRB_fourth_edition_2022-12-18.pdf")))
g.add((ont, DCTERMS.title, Literal("WRB code lists")))
g.add((ont, FOAF.logo, URIRef("https://wrb.isric.org/images/logo.png")))

with open('../wrb-codelists.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    cs = ""
    for row in reader:
        if cs != valuri(row['attribute']):
            cs = valuri(row['attribute'])
            cs2 = URIRef(WRB[valuri(row['attribute'])])
            g.add((cs2, RDF.type, SKOS.ConceptScheme))
            g.add((cs2, SKOS.prefLabel, Literal(row['attribute'])))

        concept = URIRef(WRB[valuri(row['attribute'])+'/'+valuri(row['id'])])
        g.add((concept, RDF.type, SKOS.Concept))
        g.add((concept, SKOS.prefLabel, Literal(row['label'])))
        g.add((concept, SKOS.inScheme, cs2))
        g.add((concept, SKOS.notation, Literal(row['notation'])))
        g.add((concept, SKOS.definition, Literal(row['definition'])))

g.bind("skos", SKOS) 
g.bind("dcterms", DCTERMS) 
g.bind("owl", OWL) 
g.bind("wrb", WRB)
g.serialize(destination="../wrb-codelists.ttl")

