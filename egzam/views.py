# Create your views here.
from django.shortcuts import render_to_response, redirect
from egzam.models import Egzamin

def homepage(request):
    #seriale = Serial.objects.all().order_by('nazwa')
    #kategorie = Kategoria.objects.all().order_by('nazwa')
    #if request.user.is_authenticated():
    #    return render_to_response('index.html', {'user': request.user,'seriale' : seriale,'kategorie' : kategorie, 'msg' : msg, 'mode' : mode}, context_instance=RequestContext(request))
    return list_egzam(request,1)
    egzaminy = Egzamin.objects.all()
    return render_to_response('index.html', {'egzaminy' : egzaminy})
    
def list_egzam(request, pagenum):
    first = (int(pagenum)-1) * 5
    last = int(pagenum) + 4
    egzaminy = Egzamin.objects.all()[first:last]
    res_set = {}
    res_set['pagenum'] = int(pagenum)
    res_set['egzaminy'] = egzaminy
    if (Egzamin.objects.all().count() >  (first + 5)):
      res_set['nextpage'] = int(pagenum) + 1
    if (pagenum > 1):
      res_set['prevpage'] = int(pagenum) - 1
    return render_to_response('index.html', res_set)