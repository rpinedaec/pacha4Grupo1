from .models import Cupon, Estado_pedido, Categoria, Cliente, Producto, Pedido, Detalle_pedido
from rest_framework import serializers

class CuponSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cupon
        fields = ['url','id','codigo','descripcion','descuento','created','updated']

class Estado_pedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado_pedido
        fields = ['url','id','descripcion','created','updated']

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['url','id','nombre','descripcion','created','updated']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['url','id','username','nombre','email','password','created','updated']

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['url','id','nombre','descripcion','categoria','igv','imagen','precio','descuento','created','updated']

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = ['url','id','fecha','subtotal','igv','total','cliente','estado','cupon','created','updated']

class Detalle_pedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Detalle_pedido
        fields = ['url','id','pedido','producto','cantidad','subtotal','created','updated']