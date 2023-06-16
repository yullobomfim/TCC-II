from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import( Empresa, Funcao, Empregado, Tiporisco, Descricaoperigo, Lesoes, Fonterisco, Medidasimplementadas,
Tempoexposicao, Nivelexposicao, Nivelprobabilidade, Nivelgravidade, Nivelrisco, Classificacaorisco, Avaliacaorisco,
Identificacaorisco, Inventario, Medidascontrole, Planoacao, Empregadoinventario, Empregadoplano)

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = '__all__'

class EmpresaForm(ModelForm):
    class Meta:
        model= Empresa
        fields = '__all__'

class FuncaoForm(ModelForm):
    class Meta:
        model= Funcao
        fields = '__all__'

class EmpregadoForm(ModelForm):
    class Meta:
        model= Empregado
        fields = '__all__'

class TiporiscoForm(ModelForm):
    class Meta:
        model= Tiporisco
        fields = '__all__'

class DescricaoperigoForm(ModelForm):
    class Meta:
        model= Descricaoperigo
        fields = '__all__'

class LesoesForm(ModelForm):
    class Meta:
        model= Lesoes
        fields = '__all__'

class FonteriscoForm(ModelForm):
    class Meta:
        model= Fonterisco
        fields = '__all__'

class MedidasimplementadasForm(ModelForm):
    class Meta:
        model= Medidasimplementadas
        fields = '__all__'

class TempoexposicaoForm(ModelForm):
    class Meta:
        model= Tempoexposicao
        fields = '__all__'

class InventarioForm(ModelForm):
    class Meta:
        model= Inventario
        fields = '__all__'

class IdentificacaoriscoForm(ModelForm):
    class Meta:
        model= Identificacaorisco
        fields = '__all__'

class MedidascontroleForm(ModelForm):
    class Meta:
        model= Medidascontrole
        fields = '__all__'

class NivelexposicaoForm(ModelForm):
    class Meta:
        model= Nivelexposicao
        fields = '__all__'

class NivelprobabilidadeForm(ModelForm):
    class Meta:
        model= Nivelprobabilidade
        fields = '__all__'

class NivelgravidadeForm(ModelForm):
    class Meta:
        model= Nivelgravidade
        fields = '__all__'

class NivelriscoForm(ModelForm):
    class Meta:
        model= Nivelrisco
        fields = '__all__'

class ClassificacaoriscoForm(ModelForm):
    class Meta:
        model= Classificacaorisco
        fields = '__all__'

class AvaliacaoriscoForm(ModelForm):
    class Meta:
        fields = '__all__'
        model= Avaliacaorisco

class PlanoacaoForm(ModelForm):
    class Meta:
        model= Planoacao
        fields = '__all__'
        
class EmpregadoinventarioForm(ModelForm):
    class Meta:
        model= Empregadoinventario
        fields = '__all__'        

class EmpregadoplanoForm(ModelForm):
    class Meta:
        model= Empregadoplano
        fields = '__all__'
