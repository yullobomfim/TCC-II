from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import EmpresaForm, EmpregadoForm, FuncaoForm, TiporiscoForm, DescricaoperigoForm, LesoesForm,FonteriscoForm, MedidasimplementadasForm, TempoexposicaoForm, InventarioForm, AvaliacaoriscoForm, PlanoacaoForm, EmpregadoinventarioForm, EmpregadoplanoForm, MedidascontroleForm, NivelexposicaoForm, NivelprobabilidadeForm, NivelgravidadeForm,  NivelriscoForm, ClassificacaoriscoForm, IdentificacaoriscoForm
from .models import Empresa, Funcao, Tiporisco, Empregado, Inventario, Identificacaorisco, Planoacao

# Create your views here.
@login_required
def home(request):
    return render (request,'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
 
# Views para o CRUD Empregado
class EmpregadoListView(ListView):
    model = Empregado
    template_name = 'empregado_list.html'
    context_object_name = 'empregados'
class EmpregadoCreateView(CreateView):
    model = Empregado
    form_class = EmpregadoForm
    template_name = 'empregado_create.html'
    success_url = reverse_lazy('empregado_list')
class EmpregadoUpdateView(UpdateView):
    model = Empregado
    form_class = EmpregadoForm
    template_name = 'empregado_update.html'
    success_url = reverse_lazy('empregado_list')
class EmpregadoDeleteView(DeleteView):
    model = Empregado
    template_name = 'empregado_delete.html'
    success_url = reverse_lazy('empregado_list')

# Views para o CRUD Empresa
class EmpresaListView(ListView):
    model = Empresa
    template_name = 'empresa_list.html'
    context_object_name = 'empresas'
class EmpresaCreateView(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa_create.html'
    success_url = reverse_lazy('empresa_list')
class EmpresaUpdateView(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa_update.html'
    success_url = reverse_lazy('empresa_list')
class EmpresaDeleteView(DeleteView):
    model = Empresa
    template_name = 'empresa_delete.html'
    success_url = reverse_lazy('empresa_list')

# Views para o CRUD Função
class FuncaoListView(ListView):
    model = Funcao
    template_name = 'funcao_list.html'
    context_object_name = 'funcoes'
class FuncaoCreateView(CreateView):
    model = Funcao
    form_class = FuncaoForm
    template_name = 'funcao_create.html'
    success_url = reverse_lazy('funcao_list')
class FuncaoUpdateView(UpdateView):
    model = Funcao
    form_class = FuncaoForm
    template_name = 'funcao_update.html'
    success_url = reverse_lazy('funcao_list')
class FuncaoDeleteView(DeleteView):
    model = Funcao
    template_name = 'funcao_delete.html'
    success_url = reverse_lazy('funcao_list')

# Views para o CRUD Tipo Risco
class TiporiscoListView(ListView):
    model = Tiporisco
    template_name = 'tiporisco_list.html'
    context_object_name = 'tiporiscos'
class TiporiscoCreateView(CreateView):
    model = Tiporisco
    form_class = TiporiscoForm
    template_name = 'tiporisco_create.html'
    success_url = reverse_lazy('tiporisco_list')
class TiporiscoUpdateView(UpdateView):
    model = Tiporisco
    form_class = TiporiscoForm
    template_name = 'tiporisco_update.html'
    success_url = reverse_lazy('tiporisco_list')
class TiporiscoDeleteView(DeleteView):
    model = Tiporisco
    template_name = 'tiporisco_delete.html'
    success_url = reverse_lazy('tiporisco_list')

# Views para o CRUD Plano de Ação
class PlanoacaoListView(ListView):
    model = Planoacao
    template_name = 'planoacao_list.html'
    context_object_name = 'planoacao'

class PlanoacaoCreateView(CreateView):
    model = Planoacao
    form_class = PlanoacaoForm
    template_name = 'planoacao_create.html'
    success_url = reverse_lazy('planoacao_list')

class PlanoacaoUpdateView(UpdateView):
    model = Planoacao
    form_class = PlanoacaoForm
    template_name = 'planoacao_update.html'
    success_url = reverse_lazy('planoacao_list')

class PlanoacaoDeleteView(DeleteView):
    model = Planoacao
    template_name = 'planoacao_delete.html'
    success_url = reverse_lazy('planoacao_list')


# Views para o CRUD Identificação de Riscos
class IdentificacaoriscoListView(ListView):
    model = Identificacaorisco
    template_name = 'identificacaorisco_list.html'
    context_object_name = 'identificacaorisco'

class IdentificacaoriscoCreateView(CreateView):
    model = Identificacaorisco
    form_class = IdentificacaoriscoForm
    template_name = 'identificacaorisco_create.html'
    success_url = reverse_lazy('identificacaorisco_list')

class IdentificacaoriscoUpdateView(UpdateView):
    model = Identificacaorisco
    form_class = IdentificacaoriscoForm
    template_name = 'identificacaorisco_update.html'
    success_url = reverse_lazy('identificacaorisco_list')

class IdentificacaoriscoDeleteView(DeleteView):
    model = Identificacaorisco
    template_name = 'identificacaorisco_delete.html'
    success_url = reverse_lazy('identificacaorisco_list')



# Views para o CRUD Inventário
class InventarioListView(ListView):
    model = Inventario
    template_name = 'inventario_list.html'
    context_object_name = 'inventario'

class InventarioCreateView(CreateView):
    model = Inventario
    form_class = InventarioForm
    template_name = 'inventario_create.html'
    success_url = reverse_lazy('inventario_list')

class InventarioUpdateView(UpdateView):
    model = Inventario
    form_class = InventarioForm
    template_name = 'inventario_update.html'
    success_url = reverse_lazy('inventario_list')

class InventarioDeleteView(DeleteView):
    model = Inventario
    template_name = 'inventario_delete.html'
    success_url = reverse_lazy('inventario_list')






def Descricaoperigo(request):
    pass
def Lesoes(request):
    pass
def Fonterisco(request):
    pass
def Medidasimplementadas(request):
    pass
def Tempoexposicao(request):
    pass
def Avaliacaorisco(request):
    pass
def Medidascontrole(request):
    pass
def Nivelexposicao(request):
    pass
def Nivelprobabilidade(request):
    pass
def Nivelgravidade(request):
    pass
def Nivelrisco(request):
    pass
def Classificacaorisco(request):
    pass
def Empregadoinventario(request):
    pass
def Empregadoplano(request):
    pass
