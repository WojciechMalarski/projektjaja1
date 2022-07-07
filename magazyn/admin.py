from django.contrib import admin

# Register your models here.
from .models import Suma, Klient, KurnikProdukcja,Uwagi

admin.site.register(Suma)
admin.site.register(Klient)
admin.site.register(KurnikProdukcja)
admin.site.register(Uwagi)
