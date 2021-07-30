import math
from dataclasses import dataclass


@dataclass
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
sonne = Planet(
    name='Sonne',
    M=1.989 * 10**30,
    mu=1.327_1 * 10**11,
    a=math.nan,  # Die Sonne hat keine große Halbachse um sich selber
    R=60_000,
    v=math.nan,  # Die Sonne hat keine Geschwindigkeit um sich selber
)
erde = Planet(
    name='Erde',
    M=5.974_2 * 10**24,
    mu=398_599,
    a=149_599_366,
    R=6_378,
    v=29.784
)
venus = Planet(
    name='Venus',
    M=4.869 * 10**24,
    mu=324_860,
    a=108_208_777,
    R=6_052,
    v=35.020,
)
mars = Planet(
    name='Mars',
    M=6.419_1 * 10**23,
    mu=42_828,
    a=227_946_314,
    R=3_397,
    v=24.129,
)
saturn = Planet(
    name='Saturn',
    M=5.686 * 10**26,
    mu=37_930_320,
    a=1_425_945_953,
    R=60_000,
    v=9.647
)
jupiter = Planet(
    name='Jupiter',
    M=1.898_8 * 10**27,
    mu=126_687_936,
    a=778_344_254,
    R=71_398,
    v=13.058,
)