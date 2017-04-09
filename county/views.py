from django.shortcuts import render
from django.urls.base import reverse_lazy
from pythonic.utility import generate_list, DASH_ENTRIES, add_dash_entry

# Create your views here.

counties = ["alba", "arad", "arges", "bacau", "bihor", "bistria-nasaud", "botosani", "brasov", "braila", "buzau", "caras-severin", "calarasi", "cluj", "constanta", "covasna", "dambovita", "dolj", "galati", "giurgiu", "gorj", "harghita", "hunedoara", "ialomita", "iasi", "ilfov", "maramures", "mehedinti", "mures", "neamt", "olt", "prahova", "satu-mare", "salaj", "sibiu", "suceava", "teleorman", "timis", "tulcea", "vaslui", "valcea", "vrancea", "bucuresti"]
add_dash_entry("county", "Nivel Judetean", '',icon='tune')

for cnty in counties:
    f_l = cnty[0]
    if not DASH_ENTRIES["county"]["children"].get(f_l, False):
        add_dash_entry(f_l, f_l.title(), '', parent='county', icon="subdirectory_arrow_right")
    add_dash_entry(cnty, cnty.title(), "county", parent='county/' + f_l, kwargs={"cnty" : cnty})

print DASH_ENTRIES

def county(request, cnty):
    request.session['active_entry'] = "county/" + cnty[0] + "/" + cnty
    context = {
        'breadcrumbs': [
                {"name": cnty.title(), "url": unicode(reverse_lazy('county', kwargs={"cnty" : cnty}))},        
            ],
        'list': generate_list(request),
        'county': cnty,
    }
    return render(request,'county/county.html', context)