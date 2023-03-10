from django.db import models

# Modelos
class Empresa(models.Model):
    nomeEmpresa = models.CharField(max_length=200, blank=True, null=True)    
    responsavelEmpresa = models.CharField(max_length=200, blank=True, null=True)    
    numeroFuncionarios = models.CharField(max_length=200, blank=True, null=True)    
    setor = models.CharField(max_length=200, blank=True, null=True)    
    
class Cargo(models.Model):
    cargo = models.CharField(max_length=200, blank=True, null=True)
    funcao = models.CharField(max_length=200, blank=True, null=True)
    cboFuncao = models.CharField(max_length=200, blank=True, null=True)
    
    
class Usuario(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    idEmpresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    idCargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

        
class Inventario(models.Model):
    fatoresRisco = models.CharField(max_length=200, blank=True, null=True)
    tipoRisco = models.CharField(max_length=200, blank=True, null=True)
    descricaoPerigos = models.CharField(max_length=200, blank=True, null=True)
    descricaoRisco = models.CharField(max_length=200, blank=True, null=True)
    possiveisLesoes = models.CharField(max_length=200, blank=True, null=True)
    fonteCircunstancias = models.CharField(max_length=200, blank=True, null=True)
    medidasImplementadas = models.CharField(max_length=200, blank=True, null=True)
    tempoExposicao = models.CharField(max_length=200, blank=True, null=True)
    
    
class PlanoAcao(models.Model):
    oque = models.CharField(max_length=200, blank=True, null=True)
    porque = models.CharField(max_length=200, blank=True, null=True)
    quando = models.CharField(max_length=200, blank=True, null=True)
    quem = models.CharField(max_length=200, blank=True, null=True)
    onde = models.CharField(max_length=200, blank=True, null=True)
    como = models.CharField(max_length=200, blank=True, null=True)
    quanto = models.CharField(max_length=200, blank=True, null=True)


class AvaliacaoRisco(models.Model):
    medidasControle = models.CharField(max_length=200, blank=True, null=True)
    nivelExposicao = models.CharField(max_length=200, blank=True, null=True)
    nivelProbabilidade = models.CharField(max_length=200, blank=True, null=True)
    nivelGravidade = models.CharField(max_length=200, blank=True, null=True)
    nivelRisco = models.CharField(max_length=200, blank=True, null=True)
    classificacaoRisco = models.CharField(max_length=200, blank=True, null=True)


    
# Gravação dos registros    
class UsuarioInventario(models.Model):
    idUsuario = models.ForeignKey(Usuario, verbose_name=("usuario"), on_delete=models.CASCADE)
    idInventario = models.ForeignKey(Inventario, verbose_name=("inventario"), on_delete=models.CASCADE)
    idPlanoAcao = models.ForeignKey(PlanoAcao, verbose_name=("planoacao"), on_delete=models.CASCADE)
    idAvaliacaoRiscos = models.ForeignKey(AvaliacaoRisco, verbose_name=("avaliacaoriscos"), on_delete=models.CASCADE)