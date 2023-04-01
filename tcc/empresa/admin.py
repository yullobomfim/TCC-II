from django.contrib import admin

from .models import Empresa, Usuario, Funcao, Tiporisco, Descricaoperigo, Lesoes,Fonterisco, Medidasimplementadas, Tempoexposicao, Inventario, Avaliacaorisco, PlanoAcao, UsuarioInventario, UsuarioPlano, Medidascontrole, Nivelexposicao, Nivelprobabilidade, Nivelgravidade,  Nivelrisco, Classificacaorisco

admin.site.register(Empresa)
admin.site.register(Usuario)

admin.site.register(Funcao)

admin.site.register(Tiporisco)
admin.site.register(Descricaoperigo)
admin.site.register(Lesoes)
admin.site.register(Fonterisco)
admin.site.register(Medidasimplementadas)
admin.site.register(Tempoexposicao)
admin.site.register(Inventario)

admin.site.register(Medidascontrole)
admin.site.register(Nivelexposicao)
admin.site.register(Nivelprobabilidade)
admin.site.register(Nivelgravidade)
admin.site.register(Nivelrisco)
admin.site.register(Classificacaorisco)
admin.site.register(Avaliacaorisco)

admin.site.register(PlanoAcao)

admin.site.register(UsuarioInventario)
admin.site.register(UsuarioPlano)