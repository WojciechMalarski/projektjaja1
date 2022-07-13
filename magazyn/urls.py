from django.urls import path
from .views import AddZamowienie,index, AddKlient, ZamowienieDetail,Deletezamowienie,ProdukcjaK1, ProdukcjaView, UwagiCreateView,UwagiView, Statystyka_View
urlpatterns = [
    # ex: /polls/
    path('', index.as_view(), name='index'),
    path('add_zamowienie/',AddZamowienie.as_view(), name='add_zamowienie'),
    path('add_klient/',AddKlient.as_view(), name='add_klient'),
    path('zamowienie_detail/<int:pk>',ZamowienieDetail.as_view(), name='zamowienie_detail'),
    path('delete_zamowienie/<int:pk>',Deletezamowienie.as_view(), name='delete_zamowienie'),
    path('Produkcjak1/',ProdukcjaK1.as_view(), name='produkcja_k1'),
    path('calaprodukcja/',ProdukcjaView.as_view(), name='cala_produkcja'),
    path('uwagi_upadki/',UwagiCreateView.as_view(), name='uwagi_upadki'),
    path('uwagi_view/',UwagiView.as_view(), name='uwagi_view'),
    path('statystyka/',Statystyka_View, name='statystyka_view'),
    ]
