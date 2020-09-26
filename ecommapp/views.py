from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from .models import Cupon, Estado_pedido, Categoria, Cliente, Producto, Pedido, Detalle_pedido
from .serializers import CuponSerializer, Estado_pedidoSerializer, CategoriaSerializer, ClienteSerializer, ProductoSerializer, PedidoSerializer, Detalle_pedidoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.views.decorators.csrf import csrf_exempt
import requests
from django.http import JsonResponse
from .template import payment
from django.shortcuts import render
#from rest_framework.permissions import IsAuthenticated


# Create your views here.
class CuponViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication, SessionAuthentication)
    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer
    filter_backends = [filters.SearchFilter]
    search_fields=['codigo']

class Estado_pedidoViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication, SessionAuthentication)
    queryset = Estado_pedido.objects.all()
    serializer_class = Estado_pedidoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields=['descripcion']

class CategoriaViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication, SessionAuthentication)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields=['nombre']

class ClienteViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication, SessionAuthentication)
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields=['nombre']

class ProductoViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields=['nombre']

class PedidoViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication, SessionAuthentication)
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields=['cliente']


class Detalle_pedidoViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication, SessionAuthentication)
    queryset = Detalle_pedido.objects.all()
    serializer_class = Detalle_pedidoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields=['pedido']

def payment(request):
    return render(request, 'payment/index.html')

@csrf_exempt
def charges(request):
    if request.method == 'POST':
        token = request.POST['token']
        installments = request.POST['installments']
        pedido = int(request.POST['idPedido'])
        email = request.POST['email']
        monto = int(request.POST['monto'])
        descrpcion = 'Pago pachaqtec curso online'
        moneda = request.POST['moneda']
        auth_token='sk_test_9dda9590d5943420'
        hed = {'Authorization': 'Bearer ' + auth_token}
        data = {
                    'amount': monto,
                    'currency_code': moneda,
                    'email': email,
                    'source_id':token,
                    'installments':installments,
                    'metadata':{'Descripcion': descrpcion}
                }
        url = 'https://api.culqi.com/v2/charges'
        charge = requests.post(url, json=data, headers=hed)

        print(charge)
        dicRes = {'message':'EXITO'}
        return JsonResponse(charge.json(), safe=False)

    return JsonResponse("only POST method", safe=False)