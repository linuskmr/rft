import math
from datetime import timedelta
from decimal import *
from lib import konstanten
from lib.planet import ERDE, Planet
from lib.unit_decimal import return_unit


@return_unit('km')
def grosse_halbachse(r: Decimal) -> Decimal:
    """
    Berechnet die große Halbachse a des Kreises.
    Hinweis: Die große Halbachse eines Kreises ist immer gleich mit seinem Radius.

    :param r: Radius des Kreises in km.
    :return: Große Halbachse a in km.
    """
    return r


@return_unit('km')
def kleine_halbachse(r: Decimal) -> Decimal:
    """
    Berechnet die kleine Halbachse b eines Kreises.
    Hinweis: Die kleine Halbachse eines Kreises ist immer gleich mit seinem Radius.

    :param r: Radius des Kreises in km.
    :return: Kleine Halbachse b in km.
    """
    return r


@return_unit('km')
def lineare_exzentrizitaet() -> Decimal:
    """
    Gibt die lineare Exzentrizität e einer Kreises zurück.
    Hinweis: Die lineare Exzentrizität ist immer 0.
    """
    return Decimal(0)


@return_unit('km')
def perizentrum_radius(r: Decimal) -> Decimal:
    """
    Berechnet den Perizentrumsradius eines Kreises, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.
    Hinweis: Der Perizentrumsradius eines Kreises ist immer gleich mit seinem Radius.

    :param r: Radius des Kreises in km.
    :return: Perizentrumsradius rp in km.
    """
    return r


@return_unit('km')
def apozentrum_radius(r: Decimal) -> Decimal:
    """
    Berechnet den Apozentrumsradius eines Kreises, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.
    Hinweis: Der Apozentrumsradius eines Kreises ist immer gleich mit seinem Radius.

    :param r: Radius des Kreises in km.
    :return: Apozentrumsradius ra in km.
    """
    return r


@return_unit('km/s')
def geschwindigkeit(*, planet: Planet, rk: Decimal) -> Decimal:
    """
    Berechnet die Geschwindigkeit auf einer Kreisbahn.
    Die Herleitung aus dem Vis-Viva-Integral findet sich in der großen Übung 6 auf Seite 9.

    >>> geschwindigkeit(planet=ERDE, rk=ERDE.R + 200)
    7.784 km/s
    >>> geschwindigkeit(planet=ERDE, rk=konstanten.ERDE_GEO_MIT_ERDRADIUS)
    3.075 km/s

    :param planet: Planet, an dem die Perizentrumsgeschwindigkeit berechnet werden soll.
    :param rk: Radius der Kreisbahn.
    :return: Kreisbahngeschwindigkeit in km/s.
    """
    return Decimal(math.sqrt(planet.mu / rk))


def winkelgeschwindigkeit(*, planet: Planet, rk: Decimal) -> Decimal:
    """
    Berechnet die Winkelgeschwindigkeit einer Kreisbahn um einen Planeten mit dem angegebenen Radius.

    :param planet: Planet, um den die Kreisbahn geflogen wird.
    :param rk: Radius des Kreises in km.
    :return: Winkelgeschwindigkeit TODO: welche Einheit?.
    """
    return (planet.mu / rk**3).sqrt()


def umlaufzeit(*, planet: Planet, r: Decimal) -> timedelta:
    """
    Berechnet die Umlaufzeit des Kreises.

    :param planet: Planet, an dem die Umlaufzeit berechnet werden soll.
    :param r: Radius des Kreises.
    :return: Umlaufzeit in Sekunden?
    """
    # TODO: Ist die Umlaufzeit wirklich in Sekunden?
    # TODO: Umlaufzeit als timedelta returnen?
    return timedelta(seconds=2 * math.pi * math.sqrt(r ** 3 / planet.mu))
