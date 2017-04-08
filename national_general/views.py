from django.shortcuts import render
from pythonic.utility import add_dash_entry, DASH_ENTRIES, generate_list
from django.urls.base import reverse_lazy
# Create your views here.

add_dash_entry("national", "Nivel National", '')
add_dash_entry("general", "Informatii Generale", 'general', parent='national')
add_dash_entry("agegroup", "Varsta Poulatiei", 'agegroup', parent='national')
add_dash_entry("phenomena", "Fenomene Demografice", '', parent='national')
add_dash_entry("natality", "Natalitate", 'natality', parent='national/phenomena')
add_dash_entry("fertility", "Fertilitate", 'fertility', parent='national/phenomena')
add_dash_entry("aborts", "Avorturi", 'aborts', parent='national/phenomena')

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
                {"name": "Varsta Populatiei", "url_name": 'agegroup'},        
            ],
        'list': generate_list(request),
    }
    return render(request,'national_general/agegroup.html', context)


def natality(request):
    print DASH_ENTRIES
    request.session['active_entry'] = "national/phenomena/natality"
    context = {
        'breadcrumbs': [
                {"name": "Natalitate", "url_name": 'natality'},        
            ],
        'list': generate_list(request),
    }
    return render(request,'national_general/natality.html', context)


def fertility(request):
    print DASH_ENTRIES
    request.session['active_entry'] = "national/phenomena/fertility"
    context = {
        'breadcrumbs': [
                {"name": "Fertilitate", "url_name": 'fertility'},        
            ],
        'list': generate_list(request),
    }
    return render(request,'national_general/fertility.html', context)

def aborts(request):
    print DASH_ENTRIES
    request.session['active_entry'] = "national/phenomena/aborts"
    context = {
        'breadcrumbs': [
                {"name": "Avorturi", "url_name": 'aborts'},        
            ],
        'list': generate_list(request),
    }
    return render(request,'national_general/aborts.html', context)