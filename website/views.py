from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from mochilistas.models import Escolas, Alunos
from website.forms import InsereEscolaForm
from website.forms import InsereAlunoForm


# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


# LISTA DE ESCOLAS
# ----------------------------------------------

class EscolaListView(ListView):
    template_name = "website/lista.html"
    model = Escolas
    context_object_name = "Escolas"

# TRANSFERÊNCIAS
# ----------------------------------------------

class TransfTemplateView(TemplateView):
    template_name = "website/transf.html"

# LISTA DE ESCOLAS
# ----------------------------------------------

class TransfeListView(ListView):
    template_name = "website/transf_escola.html"
    model = Escolas
    context_object_name = "Escolas"

    
# TRANSPORTE ESCOLAR
# ----------------------------------------------

class TranspTemplateView(TemplateView):
    template_name = "website/transp.html"
    
# AULAS DE REFORÇO
# ----------------------------------------------

class ReforcoTemplateView(TemplateView):
    template_name = "website/reforco.html"
    
# DELIVERY DE MERENDA
# ----------------------------------------------

class MerendaTemplateView(TemplateView):
    template_name = "website/merenda.html"
    
# CONTATO
# ----------------------------------------------

class ContatoTemplateView(TemplateView):
    template_name = "website/contato.html"
    model = Escolas
    success_url = reverse_lazy("website:lista_Escolas")
    

# CADASTRAMENTO DE ESCOLAS
# ----------------------------------------------

class EscolaCreateView(CreateView):
    template_name = "website/cria.html"
    model = Escolas
    form_class = InsereEscolaForm
    success_url = reverse_lazy("website:lista_Escolas")


# ATUALIZAÇÃO DE ESCOLAS
# ----------------------------------------------

class EscolaUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Escolas
    fields = '__all__'
    context_object_name = 'Escola'
    success_url = reverse_lazy("website:lista_Escolas")


# EXCLUSÃO DE ESCOLAS
# ----------------------------------------------

class EscolaDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Escolas
    fields = '__all__'
    context_object_name = 'Escolas'
    success_url = reverse_lazy("website:lista_Escolas")

# CADASTRAMENTO DE ALUNOS
# ----------------------------------------------

class AlunoCreateView(CreateView):
    template_name = "website/cria_aluno.html"
    model = Alunos
    form_class = InsereAlunoForm
    success_url = reverse_lazy("website:lista_Aluno")

# ATUALIZAÇÃO DE ALUNOS
# ----------------------------------------------

class AlunoUpdateView(UpdateView):
    template_name = "website/atualiza_aluno.html"
    model = Alunos
    fields = '__all__'
    context_object_name = 'Alunos'
    success_url = reverse_lazy("website:lista_Aluno")


# EXCLUSÃO DE ALUNOS
# ----------------------------------------------

class AlunoDeleteView(DeleteView):
    template_name = "website/exclui_aluno.html"
    model = Alunos
    fields = '__all__'
    context_object_name = 'Alunos'
    success_url = reverse_lazy("website:lista_Aluno")

# LISTA DE ALUNO
# ----------------------------------------------

class AlunoListView(ListView):
    template_name = "website/lista_aluno.html"
    model = Alunos
    context_object_name = "Alunos"
    