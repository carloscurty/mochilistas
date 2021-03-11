from website.views import IndexTemplateView, TransfTemplateView, TransfeListView, TranspTemplateView, ReforcoTemplateView, MerendaTemplateView, ContatoTemplateView, EscolaListView, EscolaUpdateView, EscolaDeleteView, AlunoCreateView, AlunoUpdateView, AlunoDeleteView, AlunoListView, EscolaCreateView

from django.urls import path

app_name = 'website'

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),

    # GET /Escola/cadastrar
    path('Escolas/cadastrar', EscolaCreateView.as_view(), name="cadastra_Escola"),

    # GET /Escolas
    path('Escolas/', EscolaListView.as_view(), name="lista_Escolas"),

    # GET/POST /Escola/{pk}
    path('Escolas/<pk>', EscolaUpdateView.as_view(), name="atualiza_Escola"),

    # GET/POST /Escolas/excluir/{pk}
    path('Escolas/excluir/<pk>', EscolaDeleteView.as_view(), name="deleta_Escola"),

    # GET /Aluno/cadastrar
    path('Alunos/cadastrar', AlunoCreateView.as_view(), name="cadastra_Aluno"),

    # GET /Aluno
    path('Alunos/listar/<pk>', AlunoListView.as_view(), name="lista_Aluno"),

    # GET/POST /Aluno/{pk}
    path('Alunos/<pk>', AlunoUpdateView.as_view(), name="atualiza_Aluno"),

    # GET/POST /Alunos/excluir/{pk}
    path('Alunos/excluir/<pk>', AlunoDeleteView.as_view(), name="deleta_Aluno"),

    # GET /Transferências
    path('Transf', TransfTemplateView.as_view(), name="transf"),

    # GET /TransfEscolas
    path('Transfe', TransfeListView.as_view(), name="transfe"),

    # GET /Transporte
    path('Transp', TranspTemplateView.as_view(), name="transp"),

    # GET /Reforço
    path('Reforco', ReforcoTemplateView.as_view(), name="reforco"),

    # GET /Merenda
    path('Merenda', MerendaTemplateView.as_view(), name="merenda"),

    # GET /Contato
    path('Contato', ContatoTemplateView.as_view(), name="contato"),

]


