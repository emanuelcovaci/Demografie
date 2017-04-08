'''
Created on Apr 8, 2017

@author: roadd
'''
from django.urls.base import reverse_lazy
from captcha.client import request

DASH_ENTRIES = {}

def add_dash_entry(name, verbose_name, url, icon='label', parent=""):
    relation = parent.split("/")
    parent = DASH_ENTRIES
    if relation[0] is not "":
        for rel in relation:
            parent = parent[rel]["children"]  
    parent[name] = {
        "name": name,
        "verbose_name": verbose_name,
        "url_name": url,
        "icon": icon,
        "children" : {},
    }

def recursive_entry(entries, depth, active_entries=[], parent_active=False):
    text = ""
    print active_entries
    for entry in sorted( entries["children"].itervalues(), key=lambda k: k['verbose_name']):
        has_children = len(entry["children"]) > 0
        if entry_active(entry, active_entries) or (not has_children and parent_active and len(active_entries) is 0):
            text += '<li class="active">\
                        <ul class="collapsible collapsible-accordion">\
                            <li>\
                                <a style="padding-left: 16px;" href="' + (unicode(reverse_lazy(entry["url_name"]) if entry["url_name"] else "#") if not has_children else '#') + '" class="collapsible-header active"><i style="margin-left:' + str(depth * 2) + '0px" class="material-icons">' + entry["icon"] + '</i>' + entry["verbose_name"] + '</a>\
                                <div class="collapsible-body" style="display:block">\
                                    <ul>' + \
                                        recursive_entry(entry, depth + 1, active_entries[1:], True) + \
                                    '</ul>\
                                </div>\
                            </li>\
                        </ul>\
                    </li>'
        else:
            text += '<li>\
                        <ul class="collapsible collapsible-accordion">\
                            <li>\
                                <a style="padding-left: 16px;"  href="' + (unicode(reverse_lazy(entry["url_name"]) if entry["url_name"] else "#") if not has_children else '#') + '" class="collapsible-header"><i style="margin-left:' + str(depth * 2) + '0px" class="material-icons">' + entry["icon"] + '</i>' + entry["verbose_name"] + '</a>\
                                <div class="collapsible-body">\
                                    <ul>' + \
                                        recursive_entry(entry, depth + 1) + \
                                    '</ul>\
                                </div>\
                            </li>\
                        </ul>\
                    </li>'
    return text

def entry_active(entry, active_entries):
    if len(active_entries) == 0:
        return False
    if entry["name"] != active_entries[0]:
        return False
    if entry["name"] == active_entries[0] and len(active_entries) == 1:
        return True
    for e in entry["children"].itervalues():
        if entry_active(e, active_entries[1:]):
            return True
    return False
    

def generate_list(request):
    active_entries = request.session["active_entry"].split("/")
    text = ""
    for entry in DASH_ENTRIES.itervalues():
        has_children = len(entry["children"]) > 0
        if entry_active(entry, active_entries):
            text += '<li class="active">\
                        <a href="' + (unicode(reverse_lazy(entry["url_name"]) if entry["url_name"] else "#") if not has_children else '#') + '" class="collapsible-header active"><i class="material-icons">' + entry["icon"] + '</i>' + entry["verbose_name"] + '</a>\
                        <div class="collapsible-body" style="display:block">\
                            <ul>' + \
                                recursive_entry(entry, 1, active_entries[1:], True) + \
                            '</ul>\
                        </div>\
                    </li>'
        else:
            text += '<li>\
                        <a href="' + (unicode(reverse_lazy(entry["url_name"]) if entry["url_name"] else "#") if not has_children else '#') + '" class="collapsible-header"><i class="material-icons">' + entry["icon"] + '</i>' + entry["verbose_name"] + '</a>\
                        <div class="collapsible-body">\
                            <ul>' + \
                                recursive_entry(entry, 1) + \
                            '</ul>\
                        </div>\
                    </li>'
    return text
        