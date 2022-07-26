from django.contrib import admin
from .models import Pessoa

class ListandoNomes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome', 'email')
    search_fields = ('nome',)
    list_filter = ('nome',)
    list_per_page = 2

admin.site.register(Pessoa, ListandoNomes)