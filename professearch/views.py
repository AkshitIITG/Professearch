from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from profs.models import Prof

def hello_world(request):
    return render(request, 'home.html')


def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match= Prof.objects.filter(Q(name__icontains=srch)|Q(institute__icontains=srch)|Q(dept__icontains=srch)|Q(aor__icontains=srch))
            if match:
                return render(request, 'search.html', {'sr':match,'srch': request.POST['srh']})
            else:

                return render(request, 'search.html', {'sr': match, 'srch': request.POST['srh'],'messages':1})
        else:
            return HttpResponseRedirect('/search/')
    return render(request, 'search.html')