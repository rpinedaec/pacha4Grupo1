from rest_framework import viewsets
from rest_framework import permissions
from .models import Cupon, Estado_pedido, Categoria, Cliente, Producto, Pedido, Detalle_pedido
from .serializers import CuponSerializer, Estado_pedidoSerializer, CategoriaSerializer, ClienteSerializer, ProductoSerializer, PedidoSerializer, Detalle_pedidoSerializer

# Create your views here.
class CuponViewSet(viewsets.ModelViewSet):
    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer

class Estado_pedidoViewSet(viewsets.ModelViewSet):
    queryset = Estado_pedido.objects.all()
    serializer_class = Estado_pedidoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class Detalle_pedidoViewSet(viewsets.ModelViewSet):
    queryset = Detalle_pedido.objects.all()
    serializer_class = Detalle_pedidoSerializer
<<<<<<< HEAD
    permission_classes = [permissions.IsAuthenticated]
>>>>>>> 6dd7b06b702c15db76cf193a7d185b9c1e73ff03
=======
>>>>>>> e9713e2ef3f8ca3d05da36a4ecdcac89f165eaff
