import math
from datetime import timedelta

from lib import konstanten
from lib.planet import ERDE, Planet
from lib.unit_float import return_unit


@return_unit('km')
def grosse_halbachse(r: float) -> float:
    """
    Berechnet die große Halbachse a des Kreises.
    Hinweis: Die große Halbachse eines Kreises ist immer gleich mit seinem Radius.

    :param r: Radius des Kreises in km.
    :return: Große Halbachse a in km.
    """
    return r


@return_unit('km')
def kleine_halbachse(r: float) -> float:
    """
    Berechnet die kleine Halbachse b eines Kreises.
    Hinweis: Die kleine Halbachse eines Kreises ist immer gleich mit seinem Radius.

    :param r: Radius des Kreises in km.
    :return: Kleine Halbachse b in km.
    """
    return r


@return_unit('km')
def lineare_exzentrizitaet() -> float:
    """
    Gibt die lineare Exzentrizität e einer Kreises zurück.
    Hinweis: Die lineare Exzentrizität ist immer 0.
    """
    return 0


@return_unit('km')
def perizentrum_radius(r: float) -> float:
    """
    Berechnet den Perizentrumsradius eines Kreises, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.
    Hinweis: Der Perizentrumsradius eines Kreises ist immer gleich mit seinem Radius.

    :param r: Radius des Kreises in km.
    :return: Perizentrumsradius rp in km.
    """
    return r


@return_unit('km')
def apozentrum_radius(r: float) -> float:
    """
    Berechnet den Apozentrumsradius eines Kreises, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.
    Hinweis: Der Apozentrumsradius eines Kreises ist immer gleich mit seinem Radius.

    :param r: Radius des Kreises in km.
    :return: Apozentrumsradius ra in km.
    """
    return r


@return_unit('km/s')
def geschwindigkeit(*, planet: Planet, rk: float) -> float:
    """
    Berechnet die Geschwindigkeit auf einer Kreisbahn.
    Die Herleitung aus dem Vis-Viva-Integral findet sich in der großen Übung 6 auf Seite 9.

    >>> geschwindigkeit(planet=ERDE, rk=ERDE.R + 200)
    7.784 km/s
    >>> geschwindigkeit(planet=ERDE, rk=konstanten.ERDE_GEO)
    3.337 km/s

    :param planet: Planet, an dem die Perizentrumsgeschwindigkeit berechnet werden soll.
    :param rk: Radius der Kreisbahn.
    :return: Kreisbahngeschwindigkeit in km/s.
    """
    return math.sqrt(planet.mu / rk)


def umlaufzeit(*, planet: Planet, r: float) -> timedelta:
    """
    Berechnet die Umlaufzeit des Kreises.

    :param planet: Planet, an dem die Umlaufzeit berechnet werden soll.
    :param r: Radius des Kreises.
    :return: Umlaufzeit in Sekunden?
    """
    # TODO: Ist die Umlaufzeit wirklich in Sekunden?
    # TODO: Umlaufzeit als timedelta returnen?
    return timedelta(seconds=2 * math.pi * math.sqrt(r ** 3 / planet.mu))
