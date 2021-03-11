from mochilistas.models import Escolas
from mochilistas.models import Alunos
from django import forms


# FORMULÁRIO DE INCLUSÃO DE ESCOLAS
# -------------------------------------------

class InsereEscolaForm(forms.ModelForm):

    chefe = forms.BooleanField(
        label='Chefe?',
        required=False,
    )

    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.Textarea
    )

    class Meta:
        # Modelo base
        model = Escolas

        # Campos que estarão no form
        fields = [
            'nome_escola',
            'cidade_escola',
            'uf_escola',
            'ensino_fundamental',
            'ensino_medio',
            'ensino_infantil',
            'vagas_infantil',
            'vagas_fundamental',
            'vagas_medio'
        ]


class InsereAlunoForm(forms.ModelForm):    

    chefe = forms.BooleanField(
        label='Chefe?',
        required=False,
    )

    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.Textarea
    )

    class Meta:
        # Modelo base
        model = Alunos

        # Campos que estarão no form
        fields = [
            'id_aluno',
            'nome_aluno',
            'email_aluno',
            'cidade_aluno',
            'uf_aluno'
        ]
        
