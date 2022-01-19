from django.contrib import admin
from escola.models import Aluno, Curso, Matricula


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


class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_filter = ('periodo',)


admin.site.register(Aluno, Alunos)
admin.site.register(Curso, Cursos)
admin.site.register(Matricula, Matriculas)


