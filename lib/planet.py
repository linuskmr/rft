import math
from dataclasses import dataclass
from lib.unit_float import UnitFloat


@dataclass(frozen=True)
class Planet:
    """Ein Planet."""

    name: str
    """Name des Planeten."""

    M: float
    """Masse in kg."""

    mu: float
    """Gravitationskonstante in km^3/s^2."""

    a: float
    """Große Halbachse in km."""

    R: float
    """Radius des Planeten in km."""

    v: float
    """Geschwindigkeit in km/s um die Sonne."""


# Definition einiger Planeten
SONNE = Planet(
    name='Helios (Sonne)',
    M=UnitFloat(1.989 * 10**30, 'kg'),
    mu=UnitFloat(1.327_1 * 10**11, 'km³/s²'),
    a=UnitFloat(math.nan, 'km'),  # Die Sonne hat keine große Halbachse um sich selber
    R=UnitFloat(60_000, 'km'),
    v=UnitFloat(math.nan, 'km/s'),  # Die Sonne hat keine Geschwindigkeit um sich selber
)
ERDE = Planet(
    name='Erde',
    M=UnitFloat(5.974_2 * 10**24, 'kg'),
    mu=UnitFloat(398_599, 'km³/s²'),
    a=UnitFloat(149_599_366, 'km'),
    R=UnitFloat(6_378, 'km'),
    v=UnitFloat(29.784, 'km/s'),
)
VENUS = Planet(
    name='Venus',
    M=UnitFloat(4.869 * 10**24, 'kg'),
    mu=UnitFloat(324_860, 'km³/s²'),
    a=UnitFloat(108_208_777, 'km'),
    R=UnitFloat(6_052, 'km'),
    v=UnitFloat(35.020, 'km/s'),
)
MARS = Planet(
    name='Mars',
    M=UnitFloat(6.419_1 * 10**23, 'kg'),
    mu=UnitFloat(42_828, 'km³/s²'),
    a=UnitFloat(227_946_314, 'km'),
    R=UnitFloat(3_397, 'km'),
    v=UnitFloat(24.129, 'km/s'),
)
SATURN = Planet(
    name='Saturn',
    M=UnitFloat(5.686 * 10**26, 'kg'),
    mu=UnitFloat(37_930_320, 'km³/s²'),
    a=UnitFloat(1_425_945_953, 'km'),
    R=UnitFloat(60_000, 'km'),
    v=UnitFloat(9.647, 'km/s'),
)
JUPITER = Planet(
    name='Jupiter',
    M=UnitFloat(1.898_8 * 10**27, 'kg'),
    mu=UnitFloat(126_687_936, 'km³/s²'),
    a=UnitFloat(778_344_254, 'km'),
    R=UnitFloat(71_398, 'km'),
    v=UnitFloat(13.058, 'km/s'),
)


def planet_from_name(planet_name: str) -> Planet:
    planeten = {
        'erde': ERDE,
        'sonne': SONNE,
        'helios': SONNE,
        'mars': MARS,
        'venus': VENUS,
        'saturn': SATURN,
        'jupiter': JUPITER
    }
    planet_name = planet_name.lower()
    return planeten[planet_name]
