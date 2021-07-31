from lib.unit_float import return_unit
from lib.planet import *
from lib import ellipse, kreis, hyperbel, parabel


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
def vis_viva(*, planet: Planet, r: float, epsilon: float, p: float) -> float:
    """
    Berechnet das Vis-Viva-Integral.

    Beispiel: Das Vis-Viva-Integral der Erde um die Sonne sollte die Geschwindigkeit der Erde ergeben.

    >>> vis_viva(planet=SONNE, r=ERDE.a, epsilon=0, p=ERDE.a)
    29.784269170050496

    :param planet: Planet, an dem das Vis-Viva-Integral berechnet werden soll.
    :param r: Radius bzw. Abstand zum Planeten in km.
    :param epsilon: Numerische Exzentrizität der Bahn.
    :param p: Bahnparameter p in km.
    :return: Geschwindigkeit des Satelliten in km/s.
    """
    return math.sqrt(planet.mu * ((2 / r) + ((epsilon ** 2 - 1) / p)))


def numerische_exzentrizitaet_ra_rp(*, ra: float, rp: float) -> float:
    """
    Berechnet die numerische Exzentrizität epsilon.

    :param ra: Radius des Apozentrums in km, also der Ort mit maximaler Entfernung zum Planten.
    :param rp: Radius des Perizentrums in km, also der Ort mit minimaler Entfernung zum Planten.
    :return: Numerische Exzentrizität.
    """
    assert rp <= ra, "Apozentrum ist kleiner als Perizentrum. Vielleicht beide Werte tauschen?"
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
    return (a * (1 + epsilon) - a * (1 - epsilon)) / (2*a)


@return_unit('km')
def lineare_exzentrizitaet_allgemein(*, a: float, epsilon: float) -> float:
    """
    Berechnet die lineare Exzentrizität e.
    
    :param a: Große Halbachse in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Lineare Exzentrizität  in km.
    """
    return a * epsilon


print('Geschwindigkeit der Erde um die Sonne:', vis_viva(planet=SONNE, r=ERDE.a, epsilon=0, p=ERDE.a))
print('Apozentrum bei p=1000 und epsilon=0.4:', bahngleichung_apozentrum(p=1000, epsilon=0.4))
print(
    'Perizentrumsgeschwindigkeit einer Parabel bei einer Kreisgeschwindigkeit von 21.3:',
    parabel.perizentrum_geschwindigkeit(vk=21.3)
)
