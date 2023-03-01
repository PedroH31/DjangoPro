from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from sitedevpro.turmas.models import Turma


class MatriculaInline(admin.TabularInline):
    model = Turma.alunos.through
    extra = 1
    readonly_fields = ('data',)
    autocomplete_fields = ('usuario',)
    ordering = ('-data',)


@admin.register(Turma)
class TurmaAdmin(OrderedModelAdmin):
    inlines = [MatriculaInline]
    list_display = ('nome', 'slug', 'inicio', 'fim')
    prepopulated_fields = ({'slug': ('nome',)})
    ordering = ('-inicio',)
