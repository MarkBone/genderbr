
<!-- README.md is generated from README.Rmd. Please edit that file -->
genderBR
========

`genderBR` predicts gender from Brazilian first names using data from
the Instituto Brasileiro de Geografia e Estatistica’s 2010 Census.

Fork do genderBR em R traduzido para Python


Data
----

The surveyed population in the Instituto Brasileiro de Geografia e
Estatistica’s (IBGE) 2010 Census includes 190,8 million Brazilians –
with more than 130,000 unique first names.

To extracts the numer of male or female uses of a given first name in
Brazil, the package employs the IBGE’s
[API](http://censo2010.ibge.gov.br/nomes/) and, from in 1.1.0 version,
also from an internal dataset containing all the names recorded in the
IBGE’s Census. In this service, different spelling (e.g., Ana and Anna,
or Marcos and Markos) implies different occurrences, and only names with
more than 20 occurrences, or more than 15 occurrences in a given state,
are included in the database.

For more information on the IBGE’s data, please check (in Portuguese):
<http://censo2010.ibge.gov.br/nomes/>

