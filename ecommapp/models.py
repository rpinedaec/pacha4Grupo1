from django.db import models

# Create your models here.
class cupon(models.Model):
    codigo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=2000)
    descuento = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.codigo

class estado_pedido(models.Model):
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.descripcion

class categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=2000)
    def __str__(self):
        return self.nombre

class cliente(models.Model):
    username = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.username

class producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    igv = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to = 'productos')
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    descuento = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.nombre
    
class pedido(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    igv = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    estado = models.ForeignKey(estado_pedido, on_delete=models.CASCADE)
    cupon = models.ForeignKey(cupon, on_delete=models.CASCADE, blank=True,
        null=True)

class detalle_pedido(models.Model):
    pedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)