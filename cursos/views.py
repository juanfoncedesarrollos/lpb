from django.shortcuts import render
from django.http import HttpResponse

from .models import Curso

def index(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/index.html', {'cursos_data':cursos})
    # return HttpResponse('cursos index')

def crear(request):
    return render(request, 'cursos/crear.html')

def guardar(request):
    curso = Curso()
    curso.codigo = request.POST['txt_codigo']
    curso.nombre = request.POST['txt_nombre']
    curso.creditos = int(request.POST['txt_creditos'])
    curso.save()
    return index(request)

def detalle(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    return render(request, 'cursos/detalle.html', {'curso_data':curso})
    # return HttpResponse('detalle')

def actualizar(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    curso.nombre = request.POST['txt_nombre']
    curso.creditos = int(request.POST['txt_creditos'])
    curso.save()
    return detalle(request, curso_id)

def eliminar(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    curso.delete()
    return index(request)