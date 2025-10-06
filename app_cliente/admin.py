from django.contrib import admin

# Register your models here.
from .models import Clientes
# registrear el modelo clientes en el admin
admin.site.register(Clientes)