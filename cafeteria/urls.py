from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views 

urlpatterns = [
    
    #===========================================
    #              SOLICITUDES
    #===========================================
    path('',views.index, name='tienda'),
    path('solicitudes/', views.solicitud_list, name='solicitud_list'),
    path('solicitudes/entregar/<int:solicitud_id>/', views.entregar_solicitud, name='entregar_solicitud'),
    
    #===========================================
    #              PRODUCTOS
    #===========================================
    path('productos/', views.producto_list, name='producto_list'),
    path('productos/<int:pk>/', views.producto_detail, name='producto_detail'),
    path('productos/nuevo/', views.producto_create, name='producto_create'),
    path('productos/<int:pk>/editar/', views.producto_update, name='producto_update'),
    #path('productos/<int:pk>/eliminar/', views.producto_delete, name='producto_delete'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)