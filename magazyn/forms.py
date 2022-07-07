from django import forms
from .models import Suma, Klient, KurnikProdukcja, Uwagi

class ZamowienieForm(forms.ModelForm):
    class Meta:
        model = Suma
        fields = ('klient','IloscSS', 'CenaSS','IloscS','CenaS','Ilosc1A','Cena1A','Ilosc1B','Cena1B','Ilosc2A','Cena2A')

        widgets = {
            'klient': forms.Select(attrs={'class':'form-control'}),
            'IloscSS': forms.TextInput(attrs={'class':'form-control'}),
            'CenaSS': forms.TextInput(attrs={'class':'form-control'}),
            'IloscS': forms.TextInput(attrs={'class':'form-control'}),
            'CenaS': forms.TextInput(attrs={'class':'form-control'}),
            'Ilosc1A': forms.TextInput(attrs={'class':'form-control'}),
            'Cena1A': forms.TextInput(attrs={'class':'form-control'}),
            'Ilosc1B': forms.TextInput(attrs={'class':'form-control'}),
            'Cena1B': forms.TextInput(attrs={'class':'form-control'}),
            'Ilosc2A': forms.TextInput(attrs={'class':'form-control'}),
            'Cena2A': forms.TextInput(attrs={'class':'form-control'}),
        }

class KlientForm(forms.ModelForm):
    class Meta:
        model =Klient
        fields = ('Imie','Nazwisko')

    widgets = {
            'Imie': forms.TextInput(attrs={'class':'form-control'}),
            'Nazwisko': forms.TextInput(attrs={'class':'form-control'})
    }
class ProdukcjaForm(forms.ModelForm):
    class Meta:
        model = KurnikProdukcja
        fields = ('Kurnik','IloscSS', 'IloscS','Ilosc1A','Ilosc1B','Ilosc2A','Ilosc2B','Stloczki')

        widgets = {
            'Kurnik': forms.Select(attrs={'class':'form-control'}),
            'IloscSS': forms.TextInput(attrs={'class':'form-control'}),
            'IloscS': forms.TextInput(attrs={'class':'form-control'}),
            'Ilosc1A': forms.TextInput(attrs={'class':'form-control'}),
            'Ilosc1B': forms.TextInput(attrs={'class':'form-control'}),
            'Ilosc2A': forms.TextInput(attrs={'class':'form-control'}),
            'Ilosc2B': forms.TextInput(attrs={'class':'form-control'}),
            'Stloczki': forms.TextInput(attrs={'class':'form-control'}),
        }
class UwagiForm(forms.ModelForm):
    class Meta:
        model =Uwagi
        fields = ('kurnik','Uwagi','upadki')
        widgets = {
            'kurnik': forms.Select(attrs={'class':'form-control'}),
            'Uwagi': forms.TextInput(attrs={'class':'form-control'}),
            'upadki': forms.TextInput(attrs={'class':'form-control'}),
        }
