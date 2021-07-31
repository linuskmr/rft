import math
from datetime import timedelta
from lib.planet import Planet
from lib.unit_float import return_unit


@return_unit('km')
def grosse_halbachse_p_epsilon(*, p: float, epsilon: float) -> float:
    """
    Berechnet die große Halbachse a einer Ellipse.

    :param p: Bahnparameter p in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Große Halbachse a in km.
    """
    return p / (1 - epsilon**2)


@return_unit('km')
def grosse_halbachse_ra_rp(*, ra: float, rp: float) -> float:
    """
    Berechnet die große Halbachse a einer Ellipse.

    :param ra: Radius Apozentrum, also der Ort mit maximaler Entfernung zum Planten.
    :param rp: Radius Perizentrum, also der Ort mit maximaler Entfernung zum Planten.
    :return: Große Halbachse a in km.
    """
    return (ra + rp) / 2

# TODO: Konflikt in Formelsammlung.
# @return_unit('km')
# def grosse_halbachse_p_epsilon(*, p: float, epsilon: float) -> float:
#     """
#     Berechnet die große Halbachse a einer Ellipse.
#
#     :param p: Bahnparameter p in km.
#     :param epsilon: Numerische Exzentrizität.
#     :return: Große Halbachse a in km.
#     """
#     return (p / 2) * ((1 / (1 - epsilon)) + (1 / (1 + epsilon)))


@return_unit('km')
def kleine_halbachse(*, a: float, e: float) -> float:
    """
    Berechnet die kleine Halbachse b einer Ellipse.

    :param a: Große Halbachse in km.
    :param e: Lineare Exzentrizität.
    :return: Kleine Halbachse b in km.
    """
    return math.sqrt(a**2 - e**2)


@return_unit('km')
def bahnparameter_p(*, rp: float, epsilon: float) -> float:
    """
    Berechnet den Bahnparameter p.

    :param rp: Perizentrumsradius, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.
    :param epsilon: Numerische Exzentrizität.
    :return: Bahnparameter p in km.
    """
    return rp * (1 + epsilon)


@return_unit('km')
def lineare_exzentrizitaet(*, a: float, rp: float) -> float:
    """
    Berechnet die lineare Exzentrizität e einer Ellipse.

    :param a: Große Halbachse in km.
    :param rp: Radius des Perizentrums in km, also der Ort mit minimaler Entfernung zum Planten.
    :return: Lineare Exzentrizität in km.
    """
    return a - rp


@return_unit('km')
def perizentrum_radius_a_epsilon(*, a: float, epsilon: float) -> float:
    """
    Berechnet den Perizentrumsradius einer Ellipse, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.

    :param a: Große Halbachse in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Perizentrumsradius rp in km.
    """
    return a * (1 - epsilon)


@return_unit('km')
def perizentrum_radius_p_epsilon(*, p: float, epsilon: float) -> float:
    """
    Berechnet den Perizentrumsradius einer Ellipse, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.

    :param p: Bahnparameter p in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Perizentrumsradius rp in km.
    """
    return p / (1 + epsilon)


@return_unit('km')
def perizentrum_radius_a_ra(*, a: float, ra: float) -> float:
    """
    Berechnet den Perizentrumsradius einer Ellipse, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.

    :param a: Große Halbachse in km.
    :param ra: Radius des Aprozentrums in km, also der Ort mit maximaler Entfernung zum Planten.
    :return: Perizentrumsradius rp in km.
    """
    return 2 * a - ra


@return_unit('km')
def apozentrum_radius_a_epsilon(*, a: float, epsilon: float) -> float:
    """
    Berechnet den Apozentrumsradius einer Ellipse, also die Entfernung des Orts mit maximaler Entfernung zum Planeten.

    :param a: Große Halbachse in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Apozentrumsradius ra in km.
    """
    return a * (1 + epsilon)


@return_unit('km')
def apozentrum_radius_p_epsilon(*, p: float, epsilon: float) -> float:
    """
    Berechnet den Apozentrumsradius einer Ellipse, also die Entfernung des Orts mit maximaler Entfernung zum Planeten.

    :param p: Bahnparameter p in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Apozentrumsradius ra in km.
    """
    return p / (1 - epsilon)


@return_unit('km')
def apozentrum_radius_a_e(*, a: float, e: float) -> float:
    """
    Berechnet den Apozentrumsradius einer Ellipse, also die Entfernung des Orts mit maximaler Entfernung zum Planeten.

    :param a: Große Halbachse in km.
    :param e: Lineare Exzentrizität in km.
    :return: Apozentrumsradius ra in km.
    """
    return a + e


@return_unit('km/s')
def perizentrum_geschwindigkeit_rp_ra(*, planet: Planet, rp: float, ra: float) -> float:
    """
    Berechnet die Perizentrumsgeschwindigkeit einer Ellipse, also die Geschwindigkeit am Ort mit minimaler Entfernung
    zum Planeten.

    :param planet: Der Planet, an dem die Perizentrumsgeschwindigkeit berechnet werden soll.
    :param rp: Perizentrumsradius rp in km.
    :param ra: Apozentrumsradius ra in km.
    :return: Perizentrumsgeschwindigkeit in km/s.
    """
    return math.sqrt(2 * planet.mu * ((1 / rp) - (1 / (rp + ra))))


@return_unit('km/s')
def perizentrum_geschwindigkeit_rp_p_epsilon(*, planet: Planet, rp: float, p: float, epsilon: float) -> float:
    """
    Berechnet die Perizentrumsgeschwindigkeit einer Ellipse, also die Geschwindigkeit am Ort mit minimaler Entfernung
    zum Planeten.

    :param planet: Der Planet, an dem die Perizentrumsgeschwindigkeit berechnet werden soll.
    :param rp: Perizentrumsradius rp in km.
    :param p: Bahnparameter p in km.
    :return: Perizentrumsgeschwindigkeit in km/s.
    """
    return math.sqrt(planet.mu * ((2 / rp) + ((epsilon**2 - 1) / p)))


@return_unit('km/s')
def apozentrum_geschwindigkeit(*, planet: Planet, ra: float, epsilon: float, p: float) -> float:
    """
        Berechnet die Apozentrumsgeschwindigkeit einer Ellipse, also die Geschwindigkeit am Ort mit maximaler Entfernung
        zum Planeten.

        :param planet: Der Planet, an dem die Apozentrumsgeschwindigkeit berechnet werden soll.
        :param ra: Apozentrumsradius ra in km.
        :param epsilon: Numerische Exzentrizität.
        :param p: Bahnparameter p in km.
        :return: Perizentrumsgeschwindigkeit in km/s.
        """
    return math.sqrt(planet.mu * ((2 / ra) + ((epsilon**2 - 1) / p)))


def umlaufzeit(*, planet: Planet, a: float) -> timedelta:
    """
    Berechnet die Umlaufzeit der Ellipse.

    :param planet: Planet, an dem die Umlaufzeit berechnet werden soll.
    :param a: Große Halbachse in km.
    :return: Umlaufzeit.
    """
    return timedelta(seconds=2 * math.pi * math.sqrt(a**3 / planet.mu))
