from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Bolsa, Textil, Complemento
from django.views.generic import TemplateView


#devuelve la portada de bookStore
def index(request):
	bolsas = get_list_or_404(Bolsa.objects.order_by('nombre'))
	textiles = get_list_or_404(Textil.objects.order_by('nombre'))
	complementos = get_list_or_404(Complemento.objects.order_by('nombre'))
	cuenta = 1
	ultimosProductos = []
	for b in bolsas:
		if cuenta<4:
		 ultimosProductos.append(b)
		 cuenta= cuenta +1
		else:
		 break
	for t in textiles:
		if cuenta<7:
		 ultimosProductos.append(t)
		 cuenta= cuenta +1
		else:
		 break
	for c in complementos:
		if cuenta<10:
		 ultimosProductos.append(c)
		 cuenta= cuenta +1
		else:
		 break
	context = {'ultimosProductos': ultimosProductos, 'bolsas': bolsas, 'textiles': textiles, 'complementos': complementos}
	return render(request, 'index.html', context)

#devuelve los datos de un departamento
def listaBolsas(request):
	bolsas = get_list_or_404(Bolsa.objects.order_by('nombre'))
	context = {'bolsas': bolsas}
	return render(request, 'listaBolsas.html', context)

def listaTextiles(request):
	textiles = get_list_or_404(Textil.objects.order_by('nombre'))
	context = {'textiles': textiles}
	return render(request, 'listaTextiles.html', context)

def listaComplementos(request):
	complementos = get_list_or_404(Complemento.objects.order_by('nombre'))
	context = {'complementos': complementos}
	return render(request, 'listaComplementos.html', context)

#devuelve los datos de un departamento
def detailBolsa(request, bolsa_id):
	bolsa = get_object_or_404(Bolsa, pk=bolsa_id)
	context = {'bolsa': bolsa}
	return render(request, 'detailBolsa.html', context)

#devuelve los empelados de un departamento
def detailTextil(request, textil_id):
	textil = get_object_or_404(Textil, pk=textil_id)
	context = {'textil': textil}
	return render(request, 'detailTextil.html', context)

	#devuelve los empelados de un departamento
def detailComplemento(request, complemento_id):
	complemento = get_object_or_404(Complemento, pk=complemento_id)
	context = {'complemento': complemento}
	return render(request, 'detailComplemento.html', context)
# Create your views here.
