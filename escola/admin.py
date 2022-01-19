from django.contrib import admin
from escola.models import Aluno, Curso


class Alunos(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'rg',
        'cpf',
        'data_nascimento'
    )
    list_display_links = ('id', 'nome',)
    search_fields = ('id', 'nome', 'rg', 'cpf')
    list_per_page = 20


class Cursos(admin.ModelAdmin):
    list_display = (
        'id',
        'codigo_curso',
        'descricao',
        'nivel'
    )
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('id', 'codigo_curso')
    list_filter = ('nivel',)


admin.site.register(Aluno, Alunos)
admin.site.register(Curso, Cursos)


