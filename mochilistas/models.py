from django.db import models

class Alunos(models.Model):

    id_aluno = models.IntegerField(
        primary_key=True,
    )

    nome_aluno = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
	
    email_aluno = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    cidade_aluno = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    uf_aluno = models.CharField(
        max_length=2,
        null=False,
        blank=False,
    )

class Escolas(models.Model):

    nome_escola = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    endereco_escola = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    bairro_escola = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    cidade_escola = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    uf_escola = models.CharField(
        max_length=2,
        null=False,
        blank=False
    )

    ensino_infantil = models.CharField(
        max_length=1,
        default="N",
        null=False,
        blank=False
    )

    ensino_fundamental = models.CharField(
        max_length=1,
        default="N",
        null=False,
        blank=False
    )

    ensino_medio = models.CharField(
        max_length=1,
        default="N",
        null=False,
        blank=False
    )

    vagas_infantil = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    vagas_fundamental = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    vagas_medio = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )


    objetos = models.Manager()