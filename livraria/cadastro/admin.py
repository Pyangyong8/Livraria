from django.contrib import admin
from .models import Livros


class LivrosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor',
                    'isbn', 'data_criacao')
    search_fields = ('autor',)


admin.site.register(Livros, LivrosAdmin)
