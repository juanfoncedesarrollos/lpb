from django.urls import path

from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear, name='crear'),
    path('guardar/', views.guardar, name='guardar'),
    path('detalle/<int:curso_id>/', views.detalle, name='detalle'),
    path('actualizar/<int:curso_id>', views.actualizar, name='actualizar'),
    path('eliminar/<int:curso_id>', views.eliminar, name='eliminar')
]