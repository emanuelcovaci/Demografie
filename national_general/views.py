from django.shortcuts import render
from pythonic.utility import add_dash_entry, DASH_ENTRIES
from django.urls.base import reverse

# Create your views here.

add_dash_entry("general", reverse('general'))

def general(request):
    print DASH_ENTRIES
    context = {
        'breadcrumbs': [
                {"name": "General", "url": reverse('general')},        
            ],
        'entries': DASH_ENTRIES,
    }
    return render(request,'national_general/general.html', context)