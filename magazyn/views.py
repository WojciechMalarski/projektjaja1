from django.shortcuts import render
from .models import Suma, Klient, KurnikProdukcja, Uwagi
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from .forms import ZamowienieForm, KlientForm, ProdukcjaForm,UwagiForm
from django.urls import reverse_lazy
from .utils import get_plot

# Create your views here.

class index(ListView):
    model = Suma
    template_name = 'home.html'
    ordering = ['-id']


class AddZamowienie(CreateView):
    model = Suma
    form_class = ZamowienieForm
    template_name = 'add_zamowienie.html'
    success_url = reverse_lazy('index')

class ZamowienieDetail(DetailView):
    model = Suma
    template_name = 'zamowienie_detail.html'


class AddKlient(CreateView):
    model = Klient
    form_class = KlientForm
    template_name = 'add_klient.html'
    success_url = reverse_lazy('index')

class Deletezamowienie(DeleteView):
    model = Suma
    template_name = 'delete_zamowienie.html'
    success_url = reverse_lazy('index')

class ProdukcjaK1(CreateView):
    model = KurnikProdukcja
    form_class = ProdukcjaForm
    template_name = 'Produkcjak1.html'
    success_url = reverse_lazy('cala_produkcja')

class ProdukcjaView(ListView):
    model = KurnikProdukcja
    template_name = 'cala_produkcja.html'
    ordering = ['-id']

class UwagiCreateView(CreateView):
    model = Uwagi
    form_class = UwagiForm
    template_name = 'Uwagi_upadki.html'
    success_url = reverse_lazy('index')

class UwagiView(ListView):
    model = Uwagi
    template_name = 'Uwagi_view.html'
    ordering = ['-id']

def Statystyka_View(request):
    qs = KurnikProdukcja.objects.all()

    x = [x.Dataprodukcji for x in qs]
    y =[y.Sumaprodukcji for y in qs]
    chart = get_plot(x,y)
    return render(request, 'statystyka.html', {'chart':chart})


