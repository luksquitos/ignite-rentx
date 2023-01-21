from django.contrib import admin
from cars.models import Fabricante, Carro, ImagemCarro


class ImagemInline(admin.StackedInline):
    model = ImagemCarro
    extra = 0


@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']
    list_display_links = ['__str__']


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'fabricante', 'quant_disponivel']
    list_display_links = ['__str__']
    readonly_fields = ["quant_disponivel"]
    inlines = [ImagemInline]