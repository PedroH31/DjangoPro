from typing import List

from sitedevpro.modulos.models import Modulo


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos coordenados por títulos
    :return:
    """
    return list(Modulo.objects.order_by('titulo').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)
