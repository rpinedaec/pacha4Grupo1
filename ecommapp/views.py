from rest_framework import viewsets
from rest_framework import permissions
from .models import Cupon, Estado_pedido, Categoria, Cliente, Producto, Pedido, Detalle_pedido
from .serializers import CuponSerializer, Estado_pedidoSerializer, CategoriaSerializer, ClienteSerializer, ProductoSerializer, PedidoSerializer, Detalle_pedidoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CuponViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer

class Estado_pedidoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    queryset = Estado_pedido.objects.all()
    serializer_class = Estado_pedidoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class Detalle_pedidoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    queryset = Detalle_pedido.objects.all()
    serializer_class = Detalle_pedidoSerializer