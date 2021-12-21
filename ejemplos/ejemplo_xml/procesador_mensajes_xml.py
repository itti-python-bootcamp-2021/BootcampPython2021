from xml.dom import minidom
"""
<?xml version="1.0" encoding="UTF-8"?>
<mensaje importancia="alta">
  <de>Raquel</de>
  <a>David</a>
  <asunto>Recogida</asunto>
  <texto>Te espero a las 8 en la puerta de la oficina</texto>
</mensaje>
"""
doc = minidom.parse("mensaje.xml")
de = doc.getElementsByTagName("de")[0].firstChild.data
a = doc.getElementsByTagName("a")[0].firstChild.data
asunto = doc.getElementsByTagName("asunto")[0].firstChild.data
texto = doc.getElementsByTagName("texto")[0].firstChild.data
importancia = doc.getElementsByTagName("mensaje")[0].getAttribute("importancia")

print(de, a, asunto, texto, importancia)