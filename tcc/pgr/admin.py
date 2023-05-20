from django.contrib import admin
from .models import Empresa, Empregado, Funcao, Identificacaorisco, Tiporisco, Descricaoperigo, Lesoes,Fonterisco, Medidasimplementadas, Tempoexposicao, Inventario, Avaliacaorisco, Planoacao, Empregadoinventario, Empregadoplano, Medidascontrole, Nivelexposicao, Nivelprobabilidade, Nivelgravidade,  Nivelrisco, Classificacaorisco

admin.site.register(Empresa)
admin.site.register(Funcao)
admin.site.register(Empregado)

admin.site.register(Tiporisco)
admin.site.register(Descricaoperigo)
admin.site.register(Lesoes)
admin.site.register(Fonterisco)
admin.site.register(Tempoexposicao)
admin.site.register(Medidasimplementadas)

admin.site.register(Nivelexposicao)
admin.site.register(Nivelprobabilidade)
admin.site.register(Nivelgravidade)
admin.site.register(Nivelrisco)
admin.site.register(Classificacaorisco)

admin.site.register(Inventario)
admin.site.register(Identificacaorisco)
admin.site.register(Avaliacaorisco)
admin.site.register(Medidascontrole)

admin.site.register(Planoacao)

admin.site.register(Empregadoinventario)
admin.site.register(Empregadoplano)