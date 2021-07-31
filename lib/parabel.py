import math
from planet import Planet


def grosse_halbachse() -> float:
    """
    Gibt die große Halbachse a einer Parabel zurück.
    Hinweis: Die große Halbachse einer Parabel ist immer unendlich.

    :return: Große Halbachse a in km.
    """
    return math.inf


def lineare_exzentrizitaet() -> float:
    """
    Gibt die lineare Exzentrizität e einer Parabel zurück.
    Hinweis: Die lineare Exzentrizität einer Parabel ist immer unendlich.

    :return: Lineare Exzentrizität.
    """
    return math.inf


def perizentrum_radius(*, p: float) -> float:
    """
    Berechnet den Perizentrumsradius einer Parabel, also die Entfernung des Orts mit minimaler Entfernung zum Planeten.

    :param p: Bahnparameter p in km.
    :return: Perizentrumsradius rp in km.
    """
    return p / 2


def apozentrum_radius() -> float:
    """
    Gibt den Apozentrumsradius einer Parabel zurück, also die Entfernung des Orts mit maximaler Entfernung zum Planeten.
    Hinweis: Der pozentrumsradius einer Parabel ist immer unendlich.

    :return: Der Apozentrumsradius ra in km.
    """
    return math.inf


def perizentrum_geschwindigkeit(*, vk: float) -> float:
    """
    Berechnet die Perizentrumsgeschwindigkeit einer Parabel, also die Geschwindigkeit am Ort mit minimaler Entfernung
    zum Planeten.

    :param vk: Die Kreisgeschwindigkeit.
    :return: Die Perizentrumsgeschwindigkeit in km/s.
    """
    return math.sqrt(2) * vk


def unendlichkeitsanomalie() -> float:
    """
    Gibt die Unendlichkeitsanomalie einer Parabel zurück.
    Hinweis: Die Unendlichkeitsanomalie einer Parabel ist immer unendlich.

    :return: Die Unendlichkeitsanomalie.
    """
    return math.inf
