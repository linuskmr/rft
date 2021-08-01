import math
from decimal import *
from dataclasses import dataclass
from lib.unit_decimal import UnitDecimal


@dataclass(frozen=True)
class Planet:
    """Ein Planet."""

    name: str
    """Name des Planeten."""

    M: Decimal
    """Masse in kg."""

    mu: Decimal
    """Gravitationskonstante in km^3/s^2."""

    a: Decimal
    """Große Halbachse in km."""

    R: Decimal
    """Radius des Planeten in km."""

    v: Decimal
    """Geschwindigkeit in km/s um die Sonne."""


# Definition einiger Planeten
SONNE = Planet(
    name='Helios (Sonne)',
    M=UnitDecimal('1.989e30', 'kg'),
    mu=UnitDecimal('1.327_1e11', 'km³/s²'),
    a=UnitDecimal(math.nan, 'km'),  # Die Sonne hat keine große Halbachse um sich selber
    R=UnitDecimal('60_000', 'km'),
    v=UnitDecimal(math.nan, 'km/s'),  # Die Sonne hat keine Geschwindigkeit um sich selber
)
ERDE = Planet(
    name='Erde',
    M=UnitDecimal('5.9_742e24', 'kg'),
    mu=UnitDecimal('398_599', 'km³/s²'),
    a=UnitDecimal('149_599_366', 'km'),
    R=UnitDecimal('6_378', 'km'),
    v=UnitDecimal('29.784', 'km/s'),
)
VENUS = Planet(
    name='Venus',
    M=UnitDecimal('4.869e24', 'kg'),
    mu=UnitDecimal('324_860', 'km³/s²'),
    a=UnitDecimal('108_208_777', 'km'),
    R=UnitDecimal('6_052', 'km'),
    v=UnitDecimal('35.020', 'km/s'),
)
MARS = Planet(
    name='Mars',
    M=UnitDecimal('6.419_1e23', 'kg'),
    mu=UnitDecimal('42_828', 'km³/s²'),
    a=UnitDecimal('227_946_314', 'km'),
    R=UnitDecimal('3_397', 'km'),
    v=UnitDecimal('24.129', 'km/s'),
)
SATURN = Planet(
    name='Saturn',
    M=UnitDecimal('5.686_e26', 'kg'),
    mu=UnitDecimal('37_930_320', 'km³/s²'),
    a=UnitDecimal('1_425_945_953', 'km'),
    R=UnitDecimal('60_000', 'km'),
    v=UnitDecimal('9.647', 'km/s'),
)
JUPITER = Planet(
    name='Jupiter',
    M=UnitDecimal('1.898_8e27', 'kg'),
    mu=UnitDecimal('126_687_936', 'km³/s²'),
    a=UnitDecimal('778_344_254', 'km'),
    R=UnitDecimal('71_398', 'km'),
    v=UnitDecimal('13.058', 'km/s'),
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
