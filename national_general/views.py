from django.shortcuts import render
from pythonic.utility import add_dash_entry, DASH_ENTRIES, generate_list
from django.urls.base import reverse_lazy
# Create your views here.

add_dash_entry("national", "Nivel National", '')
add_dash_entry("general", "Informatii Generale", 'general', parent='national')
add_dash_entry("agegroup", "Varsta Poulatiei", 'agegroup', parent='national')

def general(request):
    print DASH_ENTRIES
    request.session['active_entry'] = "national/general"
    context = {
        'breadcrumbs': [
                {"name": "Informatii Generale", "url_name": 'general'},        
            ],
        'list': generate_list(request),
    }
    return render(request,'national_general/general.html', context)

def agegroup(request):
    print DASH_ENTRIES
    request.session['active_entry'] = "national/agegroup"
    context = {
        'breadcrumbs': [
                {"name": "Varsta Populatiei", "url_name": 'general'},        
            ],
        'list': generate_list(request),
    }
    return render(request,'national_general/agegroup.html', context)