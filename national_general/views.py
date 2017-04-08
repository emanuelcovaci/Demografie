from django.shortcuts import render
from pythonic.utility import add_dash_entry, DASH_ENTRIES, generate_list
from django.urls.base import reverse_lazy
# Create your views here.

add_dash_entry("general", "General", 'general')
def general(request):
    print DASH_ENTRIES
    request.session['active_entry'] = "general"
    context = {
        'breadcrumbs': [
                {"name": "General", "url_name": 'general'},        
            ],
        'list': generate_list(request),
    }
    return render(request,'national_general/general.html', context)