import math
from planet import *


def bahngleichung(*, p: float, epsilon: float, psi: float) -> float:
    """
    Berechnet die allgemeine Bahngleichung.

    :param p: Bahnparameter p.
    :param epsilon: Numerische Exzentrizität.
    :param psi: Wahre Anomalie.
    :return: Radius r in km.
    """
    return p / (1 + epsilon * math.cos(psi))


def bahngleichung_perizentrum(*, p: float, epsilon: float) -> float:
    """
    Berechnet die Bahngleichung am Perizentrum, also der Ort mit minimaler Entfernung zum Planeten.

    :param p: Bahnparameter p in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Radius r in km.
    """
    return p / (1 + epsilon)


def bahngleichung_apozentrum(*, p: float, epsilon: float) -> float:
    """
    Berechnet die Bahngleichung am Apozentrum, also der Ort mit maximaler Entfernung zum Planeten.

    :param p: Bahnparameter p in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Radius r in km.
    """
    return p / (1 - epsilon)


def vis_viva(*, planet: Planet, r: float, epsilon: float, p: float) -> float:
    """
    Berechnet das Vis-Viva-Integral.

    Beispiel: Das Vis-Viva-Integral der Erde um die Sonne sollte die Geschwindigkeit der Erde ergeben.

    >>> vis_viva(planet=sonne, r=erde.a, epsilon=0, p=erde.a)
    29.784269170050496

    :param planet: Planet, an dem das Vis-Viva-Integral berechnet werden soll.
    :param r: Radius bzw. Abstand zum Planeten in km.
    :param epsilon: Numerische Exzentrizität der Bahn.
    :param p: Bahnparameter p in km.
    :return: Geschwindigkeit des Satelliten in km/s.
    """
    return math.sqrt(planet.mu * ((2/r) + ((epsilon**2 - 1) / p)))


def numerische_exzentrizitaet_allgemein(*, ra: float, rp: float) -> float:
    """
    Berechnet die numerische Exzentrizität epsilon.

    :param ra: Radius des Apozentrums in km, also der Ort mit maximaler Entfernung zum Planten.
    :param rp: Radius des Perizentrums in km, also der Ort mit minimaler Entfernung zum Planten.
    :return: Numerische Exzentrizität.
    """
    assert rp <= ra, "Apozentrum ist kleiner als Perizentrum. Vielleicht beide Werte tauschen?"
    return (ra - rp) / (ra + rp)


def lineare_exzentrizitaet_allgemein(*, a: float, epsilon: float) -> float:
    """
    Berechnet die lineare Exzentrizität e.
    
    :param a: Große Halbachse in km.
    :param epsilon: Nnumerische Exzentrizität.
    :return: Lineare Exzentrizität.
    """
    return a * epsilon


print(erde)

print()
print('Geschwindigkeit der Erde um die Sonne', vis_viva(planet=sonne, r=erde.a, epsilon=0, p=erde.a))
