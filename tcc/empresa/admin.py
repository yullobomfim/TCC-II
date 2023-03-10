from django.contrib import admin

from .models import Empresa, Usuario, Cargo, Inventario, AvaliacaoRisco, PlanoAcao, UsuarioInventario

admin.site.register(Empresa)
admin.site.register(Usuario)
admin.site.register(Cargo)
admin.site.register(Inventario)
admin.site.register(AvaliacaoRisco)
admin.site.register(PlanoAcao)
admin.site.register(UsuarioInventario)

