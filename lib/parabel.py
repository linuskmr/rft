import math
from lib.unit_decimal import return_unit
from decimal import *


@return_unit('km')
def grosse_halbachse() -> Decimal:
    """
    Gibt die große Halbachse a einer Parabel zurück.
    Hinweis: Die große Halbachse einer Parabel ist immer unendlich.

    :return: Große Halbachse a in km.
    """
    return Decimal(math.inf)


@return_unit('km')
def lineare_exzentrizitaet() -> Decimal:
    """
    Gibt die lineare Exzentrizität e einer Parabel zurück.
    Hinweis: Die lineare Exzentrizität einer Parabel ist immer unendlich.

    :return: Lineare Exzentrizität in km.
    """
    return Decimal(math.inf)


@return_unit('km')
def perizentrum_radius(*, p: Decimal) -> Decimal:
    """
    Berechnet den Perizentrumsradius einer Parabel, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.

    :param p: Bahnparameter p in km.
    :return: Perizentrumsradius rp in km.
    """
    return p / 2


@return_unit('km')
def apozentrum_radius() -> Decimal:
    """
    Gibt den Apozentrumsradius einer Parabel zurück, also die Entfernung des Orts mit maximaler Entfernung zum Planeten.
    Hinweis: Der pozentrumsradius einer Parabel ist immer unendlich.

    :return: Der Apozentrumsradius ra in km.
    """
    return Decimal(math.inf)


@return_unit('km/s')
def perizentrum_geschwindigkeit(*, vk: Decimal) -> Decimal:
    """
    Berechnet die Perizentrumsgeschwindigkeit einer Parabel, also die Geschwindigkeit am Ort mit minimaler Entfernung
    zum Planeten.

    :param vk: Die Kreisgeschwindigkeit.
    :return: Die Perizentrumsgeschwindigkeit in km/s.
    """
    return Decimal(math.sqrt(2)) * vk


def unendlichkeitsanomalie() -> Decimal:
    """
    Gibt die Unendlichkeitsanomalie einer Parabel zurück.
    Hinweis: Die Unendlichkeitsanomalie einer Parabel ist immer unendlich.

    :return: Die Unendlichkeitsanomalie.
    """
    return Decimal(math.inf)
