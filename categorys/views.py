from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, response
from django.template.loader import render_to_string

# Create your views here.

dicts = {
    "name":"Dires Aman",
    "Age":12,
    "Sex":"Male",
    "Department":"Software"
}

def index(request):
            
    return render(request, "categorys/index.html",{"lists" :dicts.keys()})
    
def detail(request,key):
    try:
        return render(request, "categorys/keys.html",{"value": dicts[key]})
    except:
        raise response.Http404()   
def detailIn(request, key):
    try:
        key = list(dicts.keys())[key-1]
        return  HttpResponseRedirect(reverse("detail",args=[key]) )   
    except:
        raise response.Http404()
# def ind