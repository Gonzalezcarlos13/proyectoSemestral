from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def articulosD(request):
    return render(request, 'app/articulosD.html')

def cancelarSuscripcion(request):
    return render(request, 'app/cancelarSuscripcion.html')

def carritoC(request):
    return render(request, 'app/carritoC.html')

def carritoC2(request):
    return render(request, 'app/carritoC2.html')

def compras(request):
    return render(request, 'app/compras.html')

def confirmacion(request):
    return render(request, 'app/confirmacion.html')

def ConfirmacionCancelacion(request):
    return render(request, 'app/ConfirmacionCancelacion.html')

def confirmacionS(request):
    return render(request, 'app/confirmacionS.html')

def error(request):
    return render(request, 'app/error.html')

def herramientas(request):
    return render(request, 'app/herramientas.html')

def historial(request):
    return render(request, 'app/historial.html')

def index2(request):
    return render(request, 'app/index2.html')

def nProducto(request):
    return render(request, 'app/nProducto.html')

def productoE(request):
    return render(request, 'app/productoE.html')

def registro(request):
    return render(request, 'app/registro.html')

def seguimiento(request):
    return render(request, 'app/seguimiento.html')

def Semillas(request):
    return render(request, 'app/Semillas.html')

def suscripcion(request):
    return render(request, 'app/suscripcion.html')

def Sustrato(request):
    return render(request, 'app/Sustrato.html')

def usuario(request):
    return render(request, 'app/usuario.html')

def ventas(request):
    return render(request, 'app/ventas.html')

