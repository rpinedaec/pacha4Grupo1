from django.contrib import admin
from .models import Cupon, Estado_pedido, Categoria, Cliente, Producto, Pedido, Detalle_pedido

# Register your models here.
admin.site.register(Cupon)
admin.site.register(Estado_pedido)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Detalle_pedido)


