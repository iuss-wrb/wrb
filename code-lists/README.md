# WRB codelists

[World Reference Base](https://wrb.isric.org/) working group of IUSS maintains a set of code lists to describe soils, as part of the World Reference Base for Soil Resources (current: 4th edition 2022). This repository presents a home for identification of the concepts in those lists, as well as facilites maintenance of these lists in preparation of upcoming releases.

## csv2skos

The [code lists](./wrb-codelists.ttl) are described in RDF using the SKOS ontology. The RDF is generated from a [CSV](./wrb-codelists.csv) using a [conversion script](./csv2skos/csv2skos.py). MS Excel has been used to prepare the initial version of the CSV (Note that Excel uses ';' as a separator, where this initiative uses ',' as a separator).

## skos2html

[skos2html](./csv2skos/skos2html.py) is a small utility to generate html of the skos file for human readability.