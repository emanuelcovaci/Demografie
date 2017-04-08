from django.shortcuts import render
from pythonic.utility import add_dash_entry, DASH_ENTRIES, generate_list
from django.urls.base import reverse_lazy
# Create your views here.

add_dash_entry("national", "Nivel National", '',icon='tune')
add_dash_entry("general", "Informatii Generale", 'general', parent='national',icon="subdirectory_arrow_right")
add_dash_entry("agegroup", "Varsta Poulatiei", 'agegroup', parent='national',icon="subdirectory_arrow_right")
add_dash_entry("phenomena", "Fenomene Demografice", '', parent='national',icon="subdirectory_arrow_right")
add_dash_entry("natality", "Natalitate", 'natality', parent='national/phenomena',icon='share')
add_dash_entry("fertility", "Fertilitate", 'fertility', parent='national/phenomena',icon='share')
add_dash_entry("aborts", "Avorturi", 'aborts', parent='national/phenomena',icon="share")
add_dash_entry("deaths", "Decese", '', parent='national/phenomena',icon='share')
add_dash_entry("mortality", "Mortalitatea", 'mortality', parent='national/phenomena/deaths',icon="description")
add_dash_entry("abortdeaths", "Decese prin avort", 'abortdeaths', parent='national/phenomena/deaths',icon="description")
add_dash_entry("infantdeaths", "Decese infantile", 'infantdeaths', parent='national/phenomena/deaths',icon="description")
add_dash_entry("borndead", "Nascuti morti", 'borndead', parent='national/phenomena/deaths',icon="description")
add_dash_entry("naturalincrease", "Sporul natural", 'naturalincrease', parent='national/phenomena',icon='share')
add_dash_entry("marriage", "Casatorii/Divorturi", 'marriage', parent='national/phenomena',icon='share')

def general(request):
    request.session['active_entry'] = "national/general"
    context = {
        'breadcrumbs': [
                {"name": "Informatii Generale", "url": reverse_lazy('general')},        
            ],
        'list': generate_list(request),
    }
    return render(request,'national/general.html', context)

def agegroup(request):
    request.session['active_entry'] = "national/agegroup"
    context = {
        'breadcrumbs': [
                {"name": "Varsta Populatiei", "url": reverse_lazy('agegroup')},        
            ],
        'list': generate_list(request),
    }
    return render(request,'national/agegroup.html', context)


def natality(request):
    request.session['active_entry'] = "national/phenomena/natality"
    context = {
        'breadcrumbs': [
                {"name": "Fenomene Demografice", "url": reverse_lazy('natality')},
                {"name": "Natalitate", "url": reverse_lazy('natality')},        
            ],
        'list': generate_list(request),
    }
    return render(request,'national/natality.html', context)


def fertility(request):
    request.session['active_entry'] = "national/phenomena/fertility"
    context = {
        'breadcrumbs': [
                {"name": "Fenomene Demografice", "url": reverse_lazy('natality')},
                {"name": "Fertilitate", "url": reverse_lazy('fertility')},        
            ],
        'list': generate_list(request),
    }
    return render(request,'national/fertility.html', context)

def aborts(request):
    print DASH_ENTRIES
    request.session['active_entry'] = "national/phenomena/aborts"
    context = {
        'breadcrumbs': [
                {"name": "Fenomene Demografice", "url": reverse_lazy('natality')}, 
                {"name": "Avorturi", "url": reverse_lazy('aborts')},        
            ],
        'list': generate_list(request),
    }
    return render(request,'national/aborts.html', context)

def mortality(request):
    print DASH_ENTRIES
    request.session['active_entry'] = "national/phenomena/deaths/mortality"
    context = {
        'breadcrumbs': [
                {"name": "Fenomene Demografice", "url": reverse_lazy('natality')}, 
                {"name": "Decese", "url": reverse_lazy('mortality')},    
                {"name": "Mortalitatea", "url": reverse_lazy('mortality')},        
            ],
        'list': generate_list(request),
    }
    return render(request,'national/mortality.html', context)

def abortdeaths(request):
    print DASH_ENTRIES
    request.session['active_entry'] = "national/phenomena/deaths/abortdeaths"
    context = {
        'breadcrumbs': [
                {"name": "Fenomene Demografice", "url": reverse_lazy('natality')}, 
                {"name": "Decese", "url": reverse_lazy('mortality')},    
                {"name": "Decese Prin Avort", "url": reverse_lazy('abortdeaths')},        
            ],
        'list': generate_list(request),
    }
    return render(request,'national/abortdeaths.html', context)

def infantdeaths(request):
    print DASH_ENTRIES
    request.session['active_entry'] = "national/phenomena/deaths/infantdeaths"
    context = {
        'breadcrumbs': [
                {"name": "Fenomene Demografice", "url": reverse_lazy('natality')}, 
                {"name": "Decese", "url": reverse_lazy('mortality')},    
                {"name": "Decese Copii Sub 1 An", "url": reverse_lazy('infantdeaths')},        
            ],
        'list': generate_list(request),
    }
    return render(request,'national/infantdeaths.html', context)

def borndead(request):
    print DASH_ENTRIES
    request.session['active_entry'] = "national/phenomena/deaths/borndead"
    context = {
        'breadcrumbs': [
                {"name": "Fenomene Demografice", "url": reverse_lazy('natality')}, 
                {"name": "Decese", "url": reverse_lazy('mortality')},    
                {"name": "Nascuti Morti", "url": reverse_lazy('borndead')},        
            ],
        'list': generate_list(request),
    }
    return render(request,'national/borndead.html', context)

def naturalincrease(request):
    print DASH_ENTRIES
    request.session['active_entry'] = "national/phenomena/naturalincrease"
    context = {
        'breadcrumbs': [
                {"name": "Fenomene Demografice", "url": reverse_lazy('natality')}, 
                {"name": "Sporul Natural", "url": reverse_lazy('naturalincrease')},        
            ],
        'list': generate_list(request),
    }
    return render(request,'national/naturalincrease.html', context)


def marriage(request):
    print DASH_ENTRIES
    request.session['active_entry'] = "national/phenomena/marriage"
    context = {
        'breadcrumbs': [
                {"name": "Fenomene Demografice", "url": reverse_lazy('natality')}, 
                {"name": "Casatorii/Divorturi", "url": reverse_lazy('marriage')},        
            ],
        'list': generate_list(request),
    }
    return render(request,'national/marriage.html', context)