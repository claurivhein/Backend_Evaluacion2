from django.contrib import admin
from django.urls import path
from reservas_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('listar_reservas', views.listadoReserva, name="listar_re"),
    path('agregar_reservas', views.agregarReserva, name="agregar_re"),
    path('eliminar_reservas/<int:id>', views.eliminarReserva, name="eliminar_re"),
    path('modificar_reservas/<int:id>', views.modificarReserva, name="modificar_re")
]
