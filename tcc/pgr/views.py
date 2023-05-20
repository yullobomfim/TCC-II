from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import EmpresaForm, EmpregadoForm, FuncaoForm, TiporiscoForm, Descricaoperigo, DescricaoperigoForm, LesoesForm,FonteriscoForm, MedidasimplementadasForm, TempoexposicaoForm, InventarioForm, AvaliacaoriscoForm, PlanoacaoForm, EmpregadoinventarioForm, EmpregadoplanoForm, MedidascontroleForm, NivelexposicaoForm, NivelprobabilidadeForm, NivelgravidadeForm,  NivelriscoForm, ClassificacaoriscoForm, IdentificacaoriscoForm
from .models import Empresa, Funcao, Tiporisco, Empregado, Inventario, Identificacaorisco, Planoacao , Empregadoinventario, Empregadoplano, Avaliacaorisco 
from django.urls import reverse_lazy

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
    context_object_name = 'tiposderiscos'
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

# Views para o CRUD Tipo Risco
class DescricaoperigoListView(ListView):
    model = Descricaoperigo
    template_name = 'descricaoperigo_list.html'
    context_object_name = 'descricao_perigos'
class DescricaoperigoCreateView(CreateView):
    model = Descricaoperigo
    form_class = DescricaoperigoForm
    template_name = 'descricaoperigo_create.html'
    success_url = reverse_lazy('descricaoperigo_list')
class DescricaoperigoUpdateView(UpdateView):
    model = Descricaoperigo
    form_class = DescricaoperigoForm
    template_name = 'descricaoperigo_update.html'
    success_url = reverse_lazy('descricaoperigo_list')
class DescricaoperigoDeleteView(DeleteView):
    model = Descricaoperigo
    template_name = 'descricaoperigo_delete.html'
    success_url = reverse_lazy('descricaoperigo_list')


# Views para o CRUD Identificação de Riscos
class IdentificacaoriscoListView(ListView):
    model = Identificacaorisco
    template_name = 'identificacaorisco_list.html'
    context_object_name = 'identificacao_riscos'
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

# Views para o CRUD Avaliação de Riscos
class AvaliacaoriscoListView(ListView):
    model = Avaliacaorisco
    template_name = 'avaliacaorisco_list.html'
    context_object_name = 'avaliacao_riscos'
class AvaliacaoriscoCreateView(CreateView):
    model = Avaliacaorisco
    form_class = AvaliacaoriscoForm
    template_name = 'avaliacaorisco_create.html'
    success_url = reverse_lazy('avaliacaorisco_list')
class AvaliacaoriscoUpdateView(UpdateView):
    model = Avaliacaorisco
    form_class = AvaliacaoriscoForm
    template_name = 'avaliacaorisco_update.html'
    success_url = reverse_lazy('avaliacaorisco_list')
class AvaliacaoriscoDeleteView(DeleteView):
    model = Avaliacaorisco
    template_name = 'avaliacaorisco_delete.html'
    success_url = reverse_lazy('avaliacaorisco_list')


# Views para o CRUD Inventário
class InventarioListView(ListView):
    model = Inventario
    template_name = 'inventario_list.html'
    context_object_name = 'inventarios'
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


# Views para o CRUD Plano de Ação
class PlanoacaoListView(ListView):
    model = Planoacao
    template_name = 'planoacao_list.html'
    context_object_name = 'planos_acao'
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


# Views para o CRUD  Empregado x Inventário
class EmpregadoinventarioListView(ListView):
    model = Empregadoinventario
    template_name = 'empregadoinventario_list.html'
    context_object_name = 'empregadosinventarios'
class EmpregadoinventarioCreateView(CreateView):
    model = Empregadoinventario
    form_class = EmpregadoinventarioForm
    template_name = 'empregadoinventario_create.html'
    success_url = reverse_lazy('empregadoinventario_list')
class EmpregadoinventarioUpdateView(UpdateView):
    model = Empregadoinventario
    form_class = EmpregadoinventarioForm
    template_name = 'empregadoinventario_update.html'
    success_url = reverse_lazy('empregadoinventario_list')
class EmpregadoinventarioDeleteView(DeleteView):
    model = Empregadoinventario
    template_name = 'empregadoinventario_delete.html'
    success_url = reverse_lazy('empregadoinventario_list')


# Views para o CRUD  Empregado x Plano de Ação
class EmpregadoplanoListView(ListView):
    model = Empregadoplano
    template_name = 'empregadoplano_list.html'
    context_object_name = 'empregadosplanos'
class EmpregadoplanoCreateView(CreateView):
    model = Empregadoplano
    form_class = EmpregadoplanoForm
    template_name = 'empregadoplano_create.html'
    success_url = reverse_lazy('empregadoplano_list')
class EmpregadoplanoUpdateView(UpdateView):
    model = Empregadoplano
    form_class = EmpregadoplanoForm
    template_name = 'empregadoplano_update.html'
    success_url = reverse_lazy('empregadoplano_list')
class EmpregadoplanoDeleteView(DeleteView):
    model = Empregadoplano
    template_name = 'empregadoplano_delete.html'
    success_url = reverse_lazy('empregadoplano_list')


