from xml.dom.minidom import parse


def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)


with parse("currency.xml") as dom:
    names_from_xml = []
    slides = dom.getElementsByTagName("Valute")
    for slide in slides:
        name = slide.getElementsByTagName("Name")[0]
        if getText(slide.getElementsByTagName('Nominal')[0].childNodes) == '1':
            names_from_xml.append(getText(name.childNodes))
    print(*names_from_xml, sep=', ')



