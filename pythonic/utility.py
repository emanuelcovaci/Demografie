'''
Created on Apr 8, 2017

@author: roadd
'''

DASH_ENTRIES = {}

def add_dash_entry(name, verbose_name, url, icon, parent=""):
    relation = parent.split("/")
    parent = DASH_ENTRIES
    for rel in relation:
        parent = parent[rel]["children"]  
    parent[name] = {
        "verbose_name": verbose_name,
        "url": url,
        "icon": icon,
        "children" : {},
    }