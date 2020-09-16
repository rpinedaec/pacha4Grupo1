from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    text = {
        "nombre":"Prueba",
        "edad": 30,
        "telefono":"6567845",
        "amigo": ['antoni','beto','charlie']
    }
    return render(request,"index.html", text)

def Tienda(request):
    return render(request,"tienda.html")

def MiPedido(request):
    return render(request,"mipedido.html")