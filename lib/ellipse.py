import math
from planet import Planet


def grosse_halbachse(*, p: float, epsilon: float) -> float:
    """
    Berechnet die große Halbachse a einer Ellipse.

    :param p: Bahnparameter p in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Große Halbachse a in km.
    """
    return p / (1 - epsilon**2)


def kleine_halbachse(*, a: float, e: float) -> float:
    """
    Berechnet die kleine Halbachse b einer Ellipse.

    :param a: Große Halbachse in km.
    :param e: Lineare Exzentrizität.
    :return: Kleine Halbachse b in km.
    """
    return math.sqrt(a**2 - e**2)


def lineare_exzentrizitaet(*, a: float, rp: float) -> float:
    """
    Berechnet die lineare Exzentrizität e einer Ellipse.

    :param a: Große Halbachse in km.
    :param rp: Radius des Perizentrums in km, also der Ort mit minimaler Entfernung zum Planten.
    :return: Lineare Exzentrizität.
    """
    return a - rp


def perizentrum_radius(*, a: float, epsilon: float) -> float:
    """
    Berechnet den Perizentrumsradius einer Ellipse, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.

    :param a: Große Halbachse in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Perizentrumsradius rp in km.
    """
    return a * (1 - epsilon)


def apozentrum_radius(*, a: float, epsilon: float) -> float:
    """
    Berechnet den Apozentrumsradius einer Ellipse, also die Entfernung des Orts mit maximaler Entfernung zum Planeten.

    :param a: Große Halbachse in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Apozentrumsradius ra in km.
    """
    return a * (1 + epsilon)


def perizentrum_geschwindigkeit(*, planet: Planet, rp: float, ra: float) -> float:
    """
    Berechnet die Perizentrumsgeschwindigkeit einer Ellipse, also die Geschwindigkeit am Ort mit minimaler Entfernung
    zum Planeten.

    :param planet: Der Planet, an dem die Perizentrumsgeschwindigkeit berechnet werden soll.
    :param rp: Perizentrumsradius rp in km.
    :param ra: Apozentrumsradius ra in km.
    :return: Perizentrumsgeschwindigkeit in km/s.
    """
    return math.sqrt(2 * planet.mu * ((1 / rp) - (1 / (rp + ra))))


def umlaufzeit(*, planet: Planet, a: float) -> float:
    """
    Berechnet die Umlaufzeit der Ellipse.

    :param planet: Planet, an dem die Umlaufzeit berechnet werden soll.
    :param a: Große Halbachse in km.
    :return: Umlaufzeit in Sekunden?
    """
    # TODO: Ist die Umlaufzeit wirklich in Sekunden?
    # TODO: Umlaufzeit als timedelta returnen?
    return 2 * math.pi * math.sqrt(a**3 / planet.mu)
