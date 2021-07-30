import math


def grosse_halbachse(*, p: float, epsilon: float) -> float:
    """
    Berechnet die große Halbachse a einer Hyperbel.

    :param p: Bahnparameter p in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Große Halbachse a in km.
    """
    return p / (epsilon**2 - 1)


def kleine_halbachse(*, a: float, e: float) -> float:
    """
    Berechnet die kleine Halbachse b einer Hyperbel.

    :param a: Große Halbachse in km.
    :param e: Lineare Exzentrizität.
    :return: Kleine Halbachse b in km.
    """
    return math.sqrt(e**2 - a**2)


def lineare_exzentrizitaet(*, a: float, rp: float) -> float:
    """
    Berechnet die lineare Exzentrizität e einer Hyperbel.

    :param a: Große Halbachse in km.
    :param rp: Radius des Perizentrums in km, also der Ort mit minimaler Entfernung zum Planten.
    :return: Lineare Exzentrizität.
    """
    return a + rp


def perizentrum_radius(*, a: float, epsilon: float) -> float:
    """
    Berechnet den Perizentrumsradius einer Hyperbel, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.

    :param a: Große Halbachse in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Perizentrumsradius rp in km.
    """
    return a * (1 - epsilon)


def apozentrum_radius(*, a: float, epsilon: float) -> float:
    """
    Berechnet den Apozentrumsradius einer Hyperbel, also die Entfernung des Orts mit maximaler Entfernung zum Planeten.

    :param a: Große Halbachse in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Apozentrumsradius ra in km.
    """
    return a * (1 + epsilon)


def perizentrum_geschwindigkeit(*, vk: float, vinf: float) -> float:
    """
    Berechnet die Perizentrumsgeschwindigkeit einer Hyperbel, also die Geschwindigkeit am Ort mit minimaler Entfernung
    zum Planeten.

    :param vk: Die Kreisbahngeschwindigkeit in km/s.
    :param vinf: Die Geschwindigkeit im Unendlichen nach der Hyperbel in km/s.
    :return: Perizentrumsgeschwindigkeit in km/s.
    """
    return math.sqrt(2 * vk**2 + vinf**2)


def unendlichkeitsanomalie(*, epsilon: float) -> float:
    """
    Berechnet die Umlaufzeit der Hyperbel.

    :param epsilon: Die numerische Exzentrizität.
    :return: Unendlichkeitsanomalie.
    """
    return math.acos(-(1 / epsilon))


def umlenkwinkel(epsilon: float) -> float:
    """
    Berechnet den Umlenkwinkel der Parabel.
    :param epsilon: Die numerische Exzentrizität.
    :return: Den Umlinkwinkel als sin(Psi/2).
    """
    # TODO: Was ist der Return-Wert?
    return 1 / epsilon
