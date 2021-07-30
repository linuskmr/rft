import math
from planet import Planet


def grosse_halbachse(r: float) -> float:
    """
    Berechnet die große Halbachse a des Kreises.
    Hinweis: Die große Halbachse eines Kreises ist immer gleich mit seinem Radius.

    :param r: Radius des Kreises in km.
    :return: Große Halbachse a in km.
    """
    return r


def kleine_halbachse(r: float) -> float:
    """
    Berechnet die kleine Halbachse b eines Kreises.
    Hinweis: Die kleine Halbachse eines Kreises ist immer gleich mit seinem Radius.

    :param r: Radius des Kreises in km.
    :return: Kleine Halbachse b in km.
    """
    return r


def lineare_exzentrizitaet() -> float:
    """
    Gibt die lineare Exzentrizität e einer Kreises zurück.
    Hinweis: Die lineare Exzentrizität ist immer 0.
    """
    return 0


def perizentrum_radius(r: float) -> float:
    """
    Berechnet den Perizentrumsradius eines Kreises, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.
    Hinweis: Der Perizentrumsradius eines Kreises ist immer gleich mit seinem Radius.

    :param r: Radius des Kreises in km.
    :return: Perizentrumsradius rp in km.
    """
    return r


def apozentrum_radius(r: float) -> float:
    """
    Berechnet den Apozentrumsradius eines Kreises, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.
    Hinweis: Der Apozentrumsradius eines Kreises ist immer gleich mit seinem Radius.

    :param r: Radius des Kreises in km.
    :return: Apozentrumsradius ra in km.
    """
    return r


def perizentrum_geschwindigkeit(*, planet: Planet, r: float) -> float:
    """
    Berechnet die Perizentrumsgeschwindigkeit eines Kreises, also die Geschwindigkeit am Ort mit minimaler Entfernung
    zum Planeten.

    :param planet: Planet, an dem die Perizentrumsgeschwindigkeit berechnet werden soll.
    :param r: Radius des Planeten.
    :return: Perizentrumsgeschwindigkeit in km/s.
    """
    return math.sqrt(planet.mu / r)


def umlaufzeit(*, planet: Planet, r: float) -> float:
    """
    Berechnet die Umlaufzeit des Kreises.

    :param planet: Planet, an dem die Umlaufzeit berechnet werden soll.
    :param r: Radius des Kreises.
    :return: Umlaufzeit in Sekunden?
    """
    # TODO: Ist die Umlaufzeit wirklich in Sekunden?
    # TODO: Umlaufzeit als timedelta returnen?
    return 2 * math.pi * math.sqrt(r ** 3 / planet.mu)
