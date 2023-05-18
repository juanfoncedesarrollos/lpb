from django.shortcuts import render
from django.http import HttpResponse
from .models import Estudiante

def index(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/index.html', {"estudiantes_list":estudiantes})

def crear(request):
    # al_identificacion = request.POST['txt_identificacion']
    return render(request, 'estudiantes/crear.html')
# Create your views here.

def guardar(request):
    est_identificacion = request.POST['txt_identificacion']
    est_nombre = request.POST['txt_nombre']
    est_apellido_1 = request.POST['txt_apellido_1']
    est_apellido_2 = request.POST['txt_apellido_2']
    estudiante = Estudiante()
    estudiante.identificacion = est_identificacion
    estudiante.nombre = est_nombre
    estudiante.apellido_1 = est_apellido_1
    estudiante.apellido_2 = est_apellido_2
    estudiante.save()

    # return render(request, 'estudiantes/index.html', {})
    return index(request)

def detalle(request, estudiante_id):
    estudiante = Estudiante.objects.get(pk=estudiante_id)
    return render(request, 'estudiantes/detalle.html', {'estudiante_data': estudiante}) 
    # return HttpResponse('estoy con el estudiante ', estudiante.nombre)

def actualizar(request, estudiante_id):
    estudiante = Estudiante.objects.get(pk=estudiante_id)
    estudiante.nombre = request.POST['txt_nombre']
    estudiante.apellido_1 = request.POST['txt_apellido_1']
    estudiante.apellido_2 = request.POST['txt_apellido_2']
    estudiante.save()
    return render(request, 'estudiantes/detalle.html', {'estudiante_data': estudiante})

def eliminar(request, estudiante_id):
    estudiante = Estudiante.objects.get(pk=estudiante_id)
    estudiante.delete()
    return index(request)
