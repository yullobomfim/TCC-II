from django.urls import path, include
from . import views
from .views import (
    home,
    cadastro,
    EmpresaListView,
    EmpresaCreateView,
    EmpresaUpdateView,
    EmpresaDeleteView,
    
    FuncaoListView,
    FuncaoCreateView,
    FuncaoUpdateView,
    FuncaoDeleteView,

    IdentificacaoriscoListView,
    IdentificacaoriscoCreateView,
    IdentificacaoriscoUpdateView,
    IdentificacaoriscoDeleteView,
    
    AvaliacaoriscoListView,
    AvaliacaoriscoCreateView,
    AvaliacaoriscoUpdateView,
    AvaliacaoriscoDeleteView,

    EmpregadoListView,
    EmpregadoCreateView,
    EmpregadoUpdateView,
    EmpregadoDeleteView,

    TiporiscoListView,
    TiporiscoCreateView,
    TiporiscoUpdateView,
    TiporiscoDeleteView,

    DescricaoperigoListView,
    DescricaoperigoCreateView,
    DescricaoperigoUpdateView,
    DescricaoperigoDeleteView,

    InventarioListView,
    InventarioCreateView,
    InventarioUpdateView,
    InventarioDeleteView,

    EmpregadoinventarioListView,
    EmpregadoinventarioCreateView,
    EmpregadoinventarioUpdateView,
    EmpregadoinventarioDeleteView,

    EmpregadoplanoListView,
    EmpregadoplanoCreateView,
    EmpregadoplanoUpdateView,
    EmpregadoplanoDeleteView,

    PlanoacaoListView,
    PlanoacaoCreateView,
    PlanoacaoUpdateView,
    PlanoacaoDeleteView,
)
    # urls.py
urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),

    path('empresa/', EmpresaListView.as_view(), name='empresa_list'),
    path('empresa/create/', EmpresaCreateView.as_view(), name='empresa_create'),
    path('empresa/update/<int:pk>/', EmpresaUpdateView.as_view(), name='empresa_update'),
    path('empresa/delete/<int:pk>/', EmpresaDeleteView.as_view(), name='empresa_delete'),

    path('funcao/', FuncaoListView.as_view(), name='funcao_list'),
    path('funcao/create/', FuncaoCreateView.as_view(), name='funcao_create'),
    path('funcao/update/<int:pk>/', FuncaoUpdateView.as_view(), name='funcao_update'),
    path('funcao/delete/<int:pk>/', FuncaoDeleteView.as_view(), name='funcao_delete'),

    path('tiporisco/', TiporiscoListView.as_view(), name='tiporisco_list'),
    path('tiporisco/create/', TiporiscoCreateView.as_view(), name='tiporisco_create'),
    path('tiporisco/update/<int:pk>/', TiporiscoUpdateView.as_view(), name='tiporisco_update'),
    path('tiporisco/delete/<int:pk>/', TiporiscoDeleteView.as_view(), name='tiporisco_delete'),

    path('descricaoperigo/', DescricaoperigoListView.as_view(), name='descricaoperigo_list'),
    path('descricaoperigo/create/', DescricaoperigoCreateView.as_view(), name='descricaoperigo_create'),
    path('descricaoperigo/update/<int:pk>/', DescricaoperigoUpdateView.as_view(), name='descricaoperigo_update'),
    path('descricaoperigo/delete/<int:pk>/', DescricaoperigoDeleteView.as_view(), name='descricaoperigo_delete'),

    path('empregado/', EmpregadoListView.as_view(), name='empregado_list'),
    path('empregado/create/', EmpregadoCreateView.as_view(), name='empregado_create'),
    path('empregado/update/<int:pk>/', EmpregadoUpdateView.as_view(), name='empregado_update'),
    path('empregado/delete/<int:pk>/', EmpregadoDeleteView.as_view(), name='empregado_delete'),

    path('inventario/', InventarioListView.as_view(), name='inventario_list'),
    path('inventario/create/', InventarioCreateView.as_view(), name='inventario_create'),
    path('inventario/update/<int:pk>/', InventarioUpdateView.as_view(), name='inventario_update'),
    path('inventario/delete/<int:pk>/', InventarioDeleteView.as_view(), name='inventario_delete'),

    path('planoacao/', PlanoacaoListView.as_view(), name='planoacao_list'),
    path('planoacao/create/', PlanoacaoCreateView.as_view(), name='planoacao_create'),
    path('planoacao/update/<int:pk>/', PlanoacaoUpdateView.as_view(), name='planoacao_update'),
    path('planoacao/delete/<int:pk>/', PlanoacaoDeleteView.as_view(), name='planoacao_delete'),

    path('identificacaorisco/', IdentificacaoriscoListView.as_view(), name='identificacaorisco_list'),
    path('identificacaorisco/create/', IdentificacaoriscoCreateView.as_view(), name='identificacaorisco_create'),
    path('identificacaorisco/update/<int:pk>/', IdentificacaoriscoUpdateView.as_view(), name='identificacaorisco_update'),
    path('identificacaorisco/delete/<int:pk>/', IdentificacaoriscoDeleteView.as_view(), name='identificacaorisco_delete'),

    path('avaliacaorisco/', AvaliacaoriscoListView.as_view(), name='avaliacaorisco_list'),
    path('avaliacaorisco/create/', AvaliacaoriscoCreateView.as_view(), name='avaliacaorisco_create'),
    path('avaliacaorisco/update/<int:pk>/', AvaliacaoriscoUpdateView.as_view(), name='avaliacaorisco_update'),
    path('avaliacaorisco/delete/<int:pk>/', AvaliacaoriscoDeleteView.as_view(), name='avaliacaorisco_delete'),

    path('empregadoinventario/', EmpregadoinventarioListView.as_view(), name='empregadoinventario_list'),
    path('empregadoinventario/create/', EmpregadoinventarioCreateView.as_view(), name='empregadoinventario_create'),
    path('empregadoinventario/update/<int:pk>/', EmpregadoinventarioUpdateView.as_view(), name='empregadoinventario_update'),
    path('empregadoinventario/delete/<int:pk>/', EmpregadoinventarioDeleteView.as_view(), name='empregadoinventario_delete'),

    path('empregadoplano/', EmpregadoplanoListView.as_view(), name='empregadoplano_list'),
    path('empregadoplano/create/', EmpregadoplanoCreateView.as_view(), name='empregadoplano_create'),
    path('empregadoplano/update/<int:pk>/', EmpregadoplanoUpdateView.as_view(), name='empregadoplano_update'),
    path('empregadoplano/delete/<int:pk>/', EmpregadoplanoDeleteView.as_view(), name='empregadoplano_delete'),    
]