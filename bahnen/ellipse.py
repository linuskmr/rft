import math
from datetime import timedelta
from decimal import Decimal
from lib import konstanten
from lib.planet import Planet, ERDE
from lib.unit_decimal import return_unit, UnitDecimal
from typing import Optional
from lib.allgemein import *
from lib.solvable import Solvable


@return_unit('km')
def grosse_halbachse_p_epsilon(*, p: Decimal, epsilon: Decimal) -> Decimal:
    """
    Berechnet die große Halbachse a einer Ellipse.

    :param p: Bahnparameter p in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Große Halbachse a in km.
    """
    return p / (1 - epsilon**2)


@return_unit('km')
def grosse_halbachse_ra_rp(*, ra: Decimal, rp: Decimal) -> Decimal:
    """
    Berechnet die große Halbachse a einer Ellipse.

    >>> grosse_halbachse_ra_rp(ra=ERDE.R+200, rp=konstanten.GEO_RADIUS)
    24371.000 km

    :param ra: Radius Apozentrum, also der Ort mit maximaler Entfernung zum Planten.
    :param rp: Radius Perizentrum, also der Ort mit maximaler Entfernung zum Planten.
    :return: Große Halbachse a in km.
    """
    return (ra + rp) / 2

# TODO: Konflikt in Formelsammlung.
# @return_unit('km')
# def grosse_halbachse_p_epsilon(*, p: Decimal, epsilon: Decimal) -> Decimal:
#     """
#     Berechnet die große Halbachse a einer Ellipse.
#
#     :param p: Bahnparameter p in km.
#     :param epsilon: Numerische Exzentrizität.
#     :return: Große Halbachse a in km.
#     """
#     return (p / 2) * ((1 / (1 - epsilon)) + (1 / (1 + epsilon)))


@return_unit('km')
def kleine_halbachse(*, a: Decimal, e: Decimal) -> Decimal:
    """
    Berechnet die kleine Halbachse b einer Ellipse.

    :param a: Große Halbachse in km.
    :param e: Lineare Exzentrizität.
    :return: Kleine Halbachse b in km.
    """
    return (a**2 - e**2).sqrt()


@return_unit('km')
def bahnparameter_p(*, rp: Decimal, epsilon: Decimal) -> Decimal:
    """
    Berechnet den Bahnparameter p.

    :param rp: Perizentrumsradius, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.
    :param epsilon: Numerische Exzentrizität.
    :return: Bahnparameter p in km.
    """
    return rp * (Decimal(1) + epsilon)


@return_unit('km')
def lineare_exzentrizitaet(*, a: Decimal, rp: Decimal) -> Decimal:
    """
    Berechnet die lineare Exzentrizität e einer Ellipse.

    :param a: Große Halbachse in km.
    :param rp: Radius des Perizentrums in km, also der Ort mit minimaler Entfernung zum Planten.
    :return: Lineare Exzentrizität in km.
    """
    return a - rp


@return_unit('km')
def perizentrum_radius_a_epsilon(*, a: Decimal, epsilon: Decimal) -> Decimal:
    """
    Berechnet den Perizentrumsradius einer Ellipse, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.

    :param a: Große Halbachse in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Perizentrumsradius rp in km.
    """
    return a * (Decimal(1) - epsilon)


@return_unit('km')
def perizentrum_radius_p_epsilon(*, p: Decimal, epsilon: Decimal) -> Decimal:
    """
    Berechnet den Perizentrumsradius einer Ellipse, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.

    :param p: Bahnparameter p in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Perizentrumsradius rp in km.
    """
    return p / (1 + epsilon)


@return_unit('km')
def perizentrum_radius_a_ra(*, a: Decimal, ra: Decimal) -> Decimal:
    """
    Berechnet den Perizentrumsradius einer Ellipse, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.

    :param a: Große Halbachse in km.
    :param ra: Radius des Aprozentrums in km, also der Ort mit maximaler Entfernung zum Planten.
    :return: Perizentrumsradius rp in km.
    """
    return 2 * a - ra


@return_unit('km')
def apozentrum_radius_a_epsilon(*, a: Decimal, epsilon: Decimal) -> Decimal:
    """
    Berechnet den Apozentrumsradius einer Ellipse, also die Entfernung des Orts mit maximaler Entfernung zum Planeten.

    :param a: Große Halbachse in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Apozentrumsradius ra in km.
    """
    return a * (1 + epsilon)


@return_unit('km')
def apozentrum_radius_p_epsilon(*, p: Decimal, epsilon: Decimal) -> Decimal:
    """
    Berechnet den Apozentrumsradius einer Ellipse, also die Entfernung des Orts mit maximaler Entfernung zum Planeten.

    :param p: Bahnparameter p in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Apozentrumsradius ra in km.
    """
    return p / (1 - epsilon)


@return_unit('km')
def apozentrum_radius_a_e(*, a: Decimal, e: Decimal) -> Decimal:
    """
    Berechnet den Apozentrumsradius einer Ellipse, also die Entfernung des Orts mit maximaler Entfernung zum Planeten.

    :param a: Große Halbachse in km.
    :param e: Lineare Exzentrizität in km.
    :return: Apozentrumsradius ra in km.
    """
    return a + e


@return_unit('km/s')
def perizentrum_geschwindigkeit_rp_ra(*, zentralgestirn: Planet, rp: Decimal, ra: Decimal) -> Decimal:
    """
    Berechnet die Perizentrumsgeschwindigkeit einer Ellipse, also die Geschwindigkeit am Ort mit minimaler Entfernung
    zum Planeten.

    :param planet: Der Planet, an dem die Perizentrumsgeschwindigkeit berechnet werden soll.
    :param rp: Perizentrumsradius rp in km.
    :param ra: Apozentrumsradius ra in km.
    :return: Perizentrumsgeschwindigkeit in km/s.
    """
    return (2 * zentralgestirn.mu * ((1 / rp) - (1 / (rp + ra)))).sqrt()


@return_unit('km/s')
def perizentrum_geschwindigkeit_rp_p_epsilon(*, zentralgestirn: Planet, rp: Decimal, p: Decimal, epsilon: Decimal) -> Decimal:
    """
    Berechnet die Perizentrumsgeschwindigkeit einer Ellipse, also die Geschwindigkeit am Ort mit minimaler Entfernung
    zum Planeten.

    :param planet: Der Planet, an dem die Perizentrumsgeschwindigkeit berechnet werden soll.
    :param rp: Perizentrumsradius rp in km.
    :param p: Bahnparameter p in km.
    :return: Perizentrumsgeschwindigkeit in km/s.
    """
    return (zentralgestirn.mu * ((2 / rp) + ((epsilon**2 - 1) / p))).sqrt()


@return_unit('km/s')
def apozentrum_geschwindigkeit(*, zentralgestirn: Planet, ra: Decimal, epsilon: Decimal, p: Decimal) -> Decimal:
    """
    Berechnet die Apozentrumsgeschwindigkeit einer Ellipse, also die Geschwindigkeit am Ort mit maximaler Entfernung
    zum Planeten.

    :param planet: Der Planet, an dem die Apozentrumsgeschwindigkeit berechnet werden soll.
    :param ra: Apozentrumsradius ra in km.
    :param epsilon: Numerische Exzentrizität.
    :param p: Bahnparameter p in km.
    :return: Perizentrumsgeschwindigkeit in km/s.
    """
    return (zentralgestirn.mu * ((2 / ra) + ((epsilon**2 - 1) / p))).sqrt()


def umlaufzeit(*, zentralgestirn: Planet, a: Decimal) -> timedelta:
    """
    Berechnet die Umlaufzeit der Ellipse.

    :param planet: Planet, an dem die Umlaufzeit berechnet werden soll.
    :param a: Große Halbachse in km.
    :return: Umlaufzeit.
    """
    return timedelta(seconds=2 * math.pi * math.sqrt(a**3 / zentralgestirn.mu))


class Ellipse(Solvable):
    ra: UnitDecimal
    """Radius Apozentrum in km."""
    rp: UnitDecimal
    """Radius Perizentrum in km."""
    epsilon: UnitDecimal
    """Numerische Exzentrizität."""
    p: UnitDecimal
    """Bahnparameter p in km."""
    a: UnitDecimal
    """Große Halbachse in km."""
    b: UnitDecimal
    """Kleine Halbachse in km."""
    e: UnitDecimal
    """Lineare Exzentrizität."""
    vp: UnitDecimal
    """Geschwindigkeit am Perizentrum in km/s"""
    va: UnitDecimal
    """Geschwindigkeit am Apozentrum in km/s."""
    zentralgestirn: Planet
    """Zentraler Körper um den sich die Bahn bewegt."""
    umlaufzeit: timedelta
    """Dauer einer Umrundung der Ellipse."""

    param_funcs: dict = {
        "ra": [apozentrum_radius_a_e,
               apozentrum_radius_a_epsilon, apozentrum_radius_p_epsilon],
        "rp": [perizentrum_radius_a_epsilon,
               perizentrum_radius_a_ra, perizentrum_radius_p_epsilon],
        "epsilon": [numerische_exzentrizitaet_e_a, numerische_exzentrizitaet_epsilon_a, numerische_exzentrizitaet_ra_rp],
        "p": [bahnparameter_p],
        "a": [grosse_halbachse_p_epsilon, grosse_halbachse_ra_rp],
        "b": [kleine_halbachse],
        "e": [lineare_exzentrizitaet],
        "vp": [perizentrum_geschwindigkeit_rp_p_epsilon,
               perizentrum_geschwindigkeit_rp_ra],
        "va": [apozentrum_geschwindigkeit],
        "zentralgestirn": [],
        "umlaufzeit": [umlaufzeit]
    }
    """All bekannten Funktionen, welche einen gegebenen paramter berechnen."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
