import math
from datetime import timedelta
from lib.planet import *
from lib.unit_float import return_unit, UnitFloat


def keplersche_zeitgleichung(planet: Planet, a: float, epsilon: float, psi: float):
    return math.sqrt(a**3 / planet.mu) * (2 * math.atan(math.sqrt((1 - epsilon) / (1 + epsilon)) * math.tan(psi / 2)))
    # Todo


@return_unit('km')
def bahngleichung(*, p: float, epsilon: float, psi: float) -> float:
    """
    Berechnet die allgemeine Bahngleichung / Kegelschnittgleichung in Polarkoordinaten.

    :param p: Bahnparameter p.
    :param epsilon: Numerische Exzentrizität.
    :param psi: Wahre Anomalie.
    :return: Radius r in km.
    """
    return p / (1 + epsilon * math.cos(psi))


@return_unit('km')
def bahngleichung_perizentrum(*, p: float, epsilon: float) -> float:
    """
    Berechnet die Bahngleichung am Perizentrum, also der Ort mit minimaler Entfernung zum Planeten.

    :param p: Bahnparameter p in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Radius r in km.
    """
    return p / (1 + epsilon)


@return_unit('km')
def bahngleichung_apozentrum(*, p: float, epsilon: float) -> float:
    """
    Berechnet die Bahngleichung am Apozentrum, also der Ort mit maximaler Entfernung zum Planeten.

    :param p: Bahnparameter p in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Radius r in km.
    """
    return p / (1 - epsilon)


@return_unit('km/s')
def vis_viva_r_epsilon_p(*, planet: Planet, r: float, epsilon: float, p: float) -> float:
    """
    Berechnet das Vis-Viva-Integral.

    Beispiel: Das Vis-Viva-Integral der Erde um die Sonne sollte die Geschwindigkeit der Erde ergeben.

    >>> vis_viva_r_epsilon_p(planet=SONNE, r=ERDE.a, epsilon=0, p=ERDE.a)
    29.784 km/s

    :param planet: Planet, an dem das Vis-Viva-Integral berechnet werden soll.
    :param r: Radius bzw. Abstand zum Planeten in km.
    :param epsilon: Numerische Exzentrizität der Bahn.
    :param p: Bahnparameter p in km.
    :return: Geschwindigkeit des Satelliten in km/s.
    """
    return math.sqrt(planet.mu * ((2 / r) + ((epsilon ** 2 - 1) / p)))


@return_unit('km/s')
def vis_viva_r_a(*, planet: Planet, r: float, a: float) -> float:
    """
    Berechnet das Vis-Viva-Integral.

    :param planet: Planet, an dem das Vis-Viva-Integral berechnet werden soll.
    :param r: Radius bzw. Abstand zum Planeten in km.
    :param a: Große Halbachse in km.
    :return: Geschwindigkeit des Satelliten in km/s.
    """
    return math.sqrt(planet.mu * ((2 / r) - (1 / a)))


def numerische_exzentrizitaet_ra_rp(*, rp: float, ra: float) -> float:
    """
    Berechnet die numerische Exzentrizität epsilon.

    :param ra: Radius des Apozentrums in km, also der Ort mit maximaler Entfernung zum Planten.
    :param rp: Radius des Perizentrums in km, also der Ort mit minimaler Entfernung zum Planten.
    :return: Numerische Exzentrizität.
    """
    return (ra - rp) / (ra + rp)


def numerische_exzentrizitaet_e_a(*, e: float, a: float) -> float:
    """
    Berechnet die numerische Exzentrizität epsilon.

    :param e: Lineare Exzentrizität in km.
    :param a: Große Halbachse in km.
    :return: Numerische Exzentrizität.
    """
    return e / a


def numerische_exzentrizitaet_epsilon_a(*, epsilon: float, a: float) -> float:
    """
    Berechnet die numerische Exzentrizität epsilon.

    :param epsilon: Numerische Exzentrizität.
    :param a: Große Halbachse in km.
    :return: Numerische Exzentrizität.
    """
    return (a * (1 + epsilon) - a * (1 - epsilon)) / (2 * a)


@return_unit('km')
def lineare_exzentrizitaet_allgemein(*, a: float, epsilon: float) -> float:
    """
    Berechnet die lineare Exzentrizität e.

    :param a: Große Halbachse in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Lineare Exzentrizität  in km.
    """
    return a * epsilon