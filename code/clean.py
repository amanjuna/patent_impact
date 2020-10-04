"""
File: clean.py

Cleans non-patent-literature citation string by escaping HTML escape characters,
converting citations to titlecase, and correcting simple grammatical mistakes.
"""

from titlecase import titlecase
from html import unescape

def clean(elem):
    elem = remove_tags(unescape(elem))
    elem = re.sub("&Amp;", "&amp;", elem)
    elem = re.sub("&(?!amp;)", "&amp;", elem)
    elem = elem.replace("<", "&lt;")
    elem = elem.replace(">", "&gt;")
    elem = re.sub("XP[0-9]{9}", "", elem)
    elem = elem.replace("';", "'")
    elem = titlecase(elem)
    
    elem = " ".join([x.title() if x.isupper() else x for x in elem.split(" ")])
    
    
    elem = elem.replace("•","-")
    elem = elem.replace("Et Al", "et al")
    elem = elem.replace("Et. Al.", "et al")
    elem = elem.replace("Et. Al", "et al")
    
    elem = re.sub("et al.(?!,)", "et al.,", elem)
    
    elem = elem.replace("et al:", "et al.,")
    elem = elem.replace("et al.:", "et al.,")
    elem = elem.replace("et al.,:", "et al.,")
    elem = elem.replace('",', ',"')
    elem = elem.replace("',", ",'")
    elem = elem.replace("\"", "\'")
    elem = elem.replace(".:", ".,")
    elem = elem.replace("\"", "'")
    elem = elem.replace(".'", "'")
    elem = elem.replace("':", "'")
    elem = elem.replace("';", "'")
    
    elem = " ".join([x[0:-1] + ",'" if len(x) > 2 and x[-1] == "'" and x[-2] != "," else x for x in elem.split(" ")])
    
    elem = elem.replace("Pnas", "Proc. Natl. Acad. Sci. U S A")
    
    elem = elem.strip().strip(",")
    return elem