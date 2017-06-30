#Parsing SBML Files
from xml.dom.minidom import parse
document = parse('sbml_example.xml')
species_list = document.getElementsByTagName("species")
for species in species_list:
   species_id = species.getAttribute('id')
   name = species.getAttribute('name')
   p_list = species.getElementsByTagName("p")
   p = p_list[0]
   text = p.childNodes[0]
   formula = text.nodeValue
   print("%-20s\t%5s\t%s"%(name, species_id, formula))