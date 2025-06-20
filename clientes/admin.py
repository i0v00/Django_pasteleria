from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cicli', 'nombrecli', 'direccioncli', 'telefonocli', 'estadocli')
    search_fields = ('cicli', 'nombrecli')
    list_filter = ('estadocli',)
