from django.db import models

# Create your models here.
class Cupon(models.Model):
    codigo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=2000)
    descuento = models.DecimalField(max_digits=10,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    class Meta():
        verbose_name= 'cupon'
        verbose_name_plural=  'cupones'

    def __str__(self):
        return self.codigo

class Estado_pedido(models.Model):
    descripcion = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    class Meta():
        verbose_name= 'estado_pedido'
        verbose_name_plural=  'estado_pedidos'

    def __str__(self):
        return self.descripcion

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    class Meta():
        verbose_name= 'categoria'
        verbose_name_plural=  'categorias'

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    username = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    class Meta():
        verbose_name= 'cliente'
        verbose_name_plural=  'clientes'

    def __str__(self):
        return self.username

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=2000)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    igv = models.BooleanField(default=True)
    imagen = models.ImageField()
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    descuento = models.DecimalField(max_digits=10,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    class Meta():
        verbose_name= 'producto'
        verbose_name_plural=  'productos'

    def __str__(self):
        return self.nombre
    
class Pedido(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    igv = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado_pedido, on_delete=models.CASCADE)
    cupon = models.ForeignKey(Cupon, on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    class Meta():
        verbose_name= 'pedido'
        verbose_name_plural=  'pedidos'

class Detalle_pedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta():
        verbose_name= 'detalle_pedido'
        verbose_name_plural=  'detalle_pedidos'