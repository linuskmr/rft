import math
from decimal import Decimal

from lib import konstanten
from lib.planet import *
from lib.unit_decimal import return_unit


@return_unit('km')
def grosse_halbachse_p_epsilon(*, p: Decimal, epsilon: Decimal) -> Decimal:
    """
    Berechnet die große Halbachse a einer Hyperbel.

    :param p: Bahnparameter p in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Große Halbachse a in km.
    """
    return p / (epsilon**2 - 1)


@return_unit('km')
def grosse_halbachse_planet_vinf(*, planet: Planet, vinf: Decimal) -> Decimal:
    """
    Berechnet die große Halbachse a einer Fluchthyperbel.

    >>> from lib.unit_decimal import UnitDecimal
    >>> UnitDecimal.output_decimal_points = 3
    >>> grosse_halbachse_planet_vinf(planet=ERDE, vinf=Decimal('2.495'))
    64031.711 km

    :param planet: Planet, an dem die Fluchthyperbel berechnet werden soll.
    :param vinf: Hyperbolische Exzessgeschwindigkeit; Geschwindigkeit im Unendlichen in km/s.
    :return: Große Halbachse a in km.
    """
    return planet.mu / (vinf**2)


@return_unit('km')
def grosse_halbachse_ra_rp(*, ra: Decimal, rp: Decimal) -> Decimal:
    """
    Berechnet die große Halbachse a einer Hyperbel.

    :param ra: Radius Apozentrum in km.
    :param rp: Radius Perizentrum in km.
    :return: Große Halbachse a in km.
    """
    return (ra - rp) / 2


@return_unit('km')
def kleine_halbachse(*, a: Decimal, e: Decimal) -> Decimal:
    """
    Berechnet die kleine Halbachse b einer Hyperbel.

    :param a: Große Halbachse in km.
    :param e: Lineare Exzentrizität.
    :return: Kleine Halbachse b in km.
    """
    return (e**2 - a**2).sqrt()


@return_unit('km')
def lineare_exzentrizitaet(*, a: Decimal, rp: Decimal) -> Decimal:
    """
    Berechnet die lineare Exzentrizität e einer Hyperbel.

    :param a: Große Halbachse in km.
    :param rp: Radius des Perizentrums in km, also der Ort mit minimaler Entfernung zum Planten.
    :return: Lineare Exzentrizität in km.
    """
    return a + rp


def numerische_exzentrizitaet(*, a: Decimal, ra: Decimal) -> Decimal:
    """
    Berechnet die numerische Exzentrizität epsilon einer Hyperbel.
    Die Herleitung findet sich in der großen Übung 6 auf Seite 9.

    :param a: Große Halbachse in km.
    :param ra: Radius des Apozentrums der Hyperbel in km.
    :return: Numerische Exzentrizität.
    """
    return round(Decimal((ra / a) - 1), konstanten.EPSILON_PRECISION)


@return_unit('km')
def bahnparameter_p(*, a: Decimal, epsilon: Decimal) -> Decimal:
    """
    Berechnet den Bahnparameter p einer Hyperbel.

    :param a: Große Halbachse in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Bahnparameter p in km.
    """
    return a * (epsilon**2 - 1)


@return_unit('km')
def perizentrum_radius_a_epsilon(*, a: Decimal, epsilon: Decimal) -> Decimal:
    """
    Berechnet den Perizentrumsradius einer Hyperbel, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.

    :param a: Große Halbachse in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Perizentrumsradius rp in km.
    """
    return a * (1 - epsilon)


@return_unit('km')
def apozentrum_radius_a_epsilon(*, a: Decimal, epsilon: Decimal) -> Decimal:
    """
    Berechnet den Apozentrumsradius einer Hyperbel, also die Entfernung des Orts mit maximaler Entfernung zum Planeten.

    :param a: Große Halbachse in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Apozentrumsradius ra in km.
    """
    return a * (1 + epsilon)


@return_unit('km')
def apozentrum_radius_a_rp(*, a: Decimal, rp: Decimal) -> Decimal:
    """
    Berechnet den Apozentrumsradius einer Hyperbel, also die Entfernung des Orts mit maximaler Entfernung zum Planeten.

    :param a: Große Halbachse in km.
    :param rp: Radius des Perizentrums in km, also der Ort mit minimaler Entfernung zum Planten.
    :return: Apozentrumsradius ra in km.
    """
    return 2 * a + rp


@return_unit('km/s')
def perizentrum_geschwindigkeit(*, vk: Decimal, vinf: Decimal) -> Decimal:
    """
    Berechnet die Perizentrumsgeschwindigkeit einer Hyperbel, also die Geschwindigkeit am Ort mit minimaler Entfernung
    zum Planeten.

    :param vk: Die Kreisbahngeschwindigkeit in km/s.
    :param vinf: Die Geschwindigkeit im Unendlichen nach der Hyperbel in km/s.
    :return: Perizentrumsgeschwindigkeit in km/s.
    """
    return (2 * vk**2 + vinf**2).sqrt()


def unendlichkeitsanomalie(*, epsilon: Decimal) -> Decimal:
    """
    Berechnet die Umlaufzeit der Hyperbel.

    :param epsilon: Die numerische Exzentrizität.
    :return: Unendlichkeitsanomalie.
    """
    return Decimal(math.acos(-(1 / epsilon)))


def umlenkwinkel(epsilon: Decimal) -> Decimal:
    """
    Berechnet den Umlenkwinkel der Parabel.
    :param epsilon: Die numerische Exzentrizität.
    :return: Den Umlinkwinkel als sin(Psi/2).
    """
    # TODO: Was ist der Return-Wert?
    return 1 / epsilon
