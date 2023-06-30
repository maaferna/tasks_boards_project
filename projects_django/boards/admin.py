from django.contrib import admin, messages
from .models import BoardsModel
# Register your models here.

admin.site.site_header = 'Curso Django'
admin.site.index_title = 'Panel de control Proyecto Django'
admin.site.site_title = 'Administrador Django'

class BoardsAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')
    list_display = ('clasification','titulo', 'valor')
    search_fields = ('titulo',)
    ordering = ('valor',)
    list_filter = ('creado', 'valor')

    def actualizar_valor_a_8(modeladmin, request, queryset):
        queryset.update(valor=8.0)
        messages.success(request, "Valor actualizado a 8")

    def clasification(self, obj):
        return "Alto" if obj.valor >= 5 else "Bajo"

    admin.site.add_action(actualizar_valor_a_8, "Colocar Valor a 8")
admin.site.register(BoardsModel, BoardsAdmin)