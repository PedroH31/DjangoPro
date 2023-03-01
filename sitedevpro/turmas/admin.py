from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from sitedevpro.turmas.models import Turma


@admin.register(Turma)
class TurmaAdmin(OrderedModelAdmin):
    list_display = ('nome', 'slug', 'inicio', 'fim')
    prepopulated_fields = ({'slug': ('nome',)})
    ordering = ('-inicio',)
