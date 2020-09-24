from .models import Cupon, Estado_pedido, Categoria, Cliente, Producto, Pedido, Detalle_pedido
from rest_framework import serializers

class CuponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupon
        fields = ['id','codigo','descripcion','descuento','created','updated']

class Estado_pedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado_pedido
        fields = ['id','descripcion','created','updated']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id','nombre','descripcion','created','updated']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','username','nombre','email','password','created','updated']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id','nombre','descripcion','categoria','igv','imagen','precio','descuento','created','updated']

class Detalle_pedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_pedido
        fields = ['id','pedido','producto','cantidad','subtotal','created','updated']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id','fecha','subtotal','igv','total','cliente','estado','cupon','created','updated']
