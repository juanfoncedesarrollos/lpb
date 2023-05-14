from django.urls import path

from . import views

app_name = 'estudiantes'

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear, name='crear'),
    path('guardar/', views.guardar, name='guardar'),
    path('detalle/<int:estudiante_id>/', views.detalle, name='detalle'),
    path('actualizar/<int:estudiante_id>', views.actualizar, name='actualizar'),
    path('eliminar/<int:estudiante_id>', views.eliminar, name='eliminar')
]