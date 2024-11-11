from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, SolicitudProducto
from customerUser.models import CustomUser
from .forms import ProductoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#===========================================
#              SOLICITUDES
#===========================================
def index(request):
    if request.method == 'POST':
        print("Entrando a la solicitud")
        #print("Solicitud recibida:", request.POST)
        
        # Recibir los datos del formulario
        nombre_cliente = request.POST.get('nombre')
        cantidad = request.POST.get('cantidad')
        mensaje = request.POST.get('mensaje', '')
        producto = request.POST.get('producto')
        modelProducto = Producto.objects.get(id=producto)
        #print("Solicitud recibida: ID", producto)
        #return redirect('tienda')

        # Crear y guardar la solicitud
        solicitud = SolicitudProducto(
            nombre_cliente=nombre_cliente,
            cantidad=cantidad,
            mensaje=mensaje,
            producto=modelProducto
        )

        # Si el usuario está autenticado, asociar el usuario a la solicitud
        if request.user.is_authenticated:
            pass
             #request.user
        solicitud.user = CustomUser.objects.get(id=1)
        
        solicitud.save()  # Guardar la solicitud

        # Mostrar mensaje de éxito
        messages.success(request, 'Tu solicitud ha sido registrada exitosamente.')

        # Redirigir al usuario a la lista de solicitudes o alguna otra página
        return redirect('tienda')

    productos = Producto.objects.filter(status=True)
    return render(request, 'tienda/index.html',{'productos': productos})

@login_required
def solicitud_list(request):
    
    #solicitudes = SolicitudProducto.objects.filter(user=request.user)
    solicitudes = SolicitudProducto.objects.filter(user=request.user).order_by('status', 'created')
    #solicitudes = SolicitudProducto.objects.filter(user=request.user).order_by('status', '-created')


    return render(request, 'solicitudes/index.html', {'solicitudes': solicitudes})
@login_required
def entregar_solicitud(request, solicitud_id):
    # Obtener la solicitud por su ID
    solicitud = get_object_or_404(SolicitudProducto, id=solicitud_id)
    
    # Realiza las acciones necesarias para marcar la solicitud como entregada, por ejemplo:
    solicitud.status = False  # O lo que represente "entregada" en tu modelo
    solicitud.save()
    
    # Redirige a la lista de solicitudes
    return redirect('solicitud_list')  # O la URL que desees





#===========================================
#              PRODUCTOS
#===========================================
# Vista para listar productos
@login_required
def producto_list(request):
    
    
    # Si no es una solicitud POST, solo mostrar la página con el producto
    productos = Producto.objects.all()
    return render(request, 'productos/index.html', {'productos': productos})

# Vista para detalle de un producto
@login_required
def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/view.html', {'producto': producto})

# Vista para crear un producto
@login_required
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'productos/form.html', {'form': form})

# Vista para actualizar un producto
@login_required
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/form.html', {'form': form})

# Vista para eliminar un producto
@login_required
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'producto_confirm_delete.html', {'producto': producto})


    