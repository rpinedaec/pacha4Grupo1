from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ecommapp import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'cupones', views.CuponViewSet)
router.register(r'estado_pedidos', views.Estado_pedidoViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'pedidos', views.PedidoViewSet)
router.register(r'detalle_pedidos', views.Detalle_pedidoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
