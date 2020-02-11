from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bolsas/', views.listaBolsas, name='listaBolsas'),
    path('textiles/', views.listaTextiles, name='listaTextiles'),
    path('complementos/', views.listaComplementos, name='listaComplementos'),
    path('bolsas/<int:bolsa_id>/', views.detailBolsa, name='detailBolsas'),
    path('textilestiles/<int:textil_id>/', views.detailTextil, name='detailTextiles'),
    path('complementos/<int:complemento_id>/', views.detailComplemento, name='detailComplementos'),
]