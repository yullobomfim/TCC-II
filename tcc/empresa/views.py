from django.shortcuts import render
from .models import Empresa,Tiporisco

# Create your views here.
def home(request):
    empresas = Empresa.objects.all()
    tipos_risco = Tiporisco.objects.all()

    return render(request, 'empresa/home.html',{"empresas": empresas, "tipos_risco": tipos_risco } )
