import os
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from pythonic.settings import BASE_DIR
from pythonic.utility import get_dash_urls


def sw(request, js):
    static_path = os.path.join(BASE_DIR, "staticcollected")
    print static_path
    paths = [os.path.join("/static", os.path.relpath(dp, static_path), f) for
            dp, dn, filenames in os.walk(static_path) for f in filenames]

    paths += get_dash_urls()
    template = get_template('sw.js')
    html = template.render(Context({
        'static': paths
    }))
    return HttpResponse(html, content_type="application/x-javascript")

def manifest(request, *args, **kwargs):
    template = get_template('manifest.json')
    html = template.render()
    return HttpResponse(html, content_type="application/json")