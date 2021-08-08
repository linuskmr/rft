import math
from decimal import Decimal
from datetime import datetime, timedelta
from dataclasses import dataclass
from lib.unit_decimal import UnitDecimal
from lib.helper import grad_zu_rad


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

    L0: Decimal
    """Referenzposition des Planeten am 12.10.1987 in Grad."""

    T: Decimal
    """Umlaufzeit des Planeten um die Sonne in Jahren."""

    L0_DATETIME: datetime = datetime(1987, 10, 12, 0, 0, 0, 0, datetime.now().tzinfo)
    """Referenzzeitpunkt für L0."""


# Definition einiger Planeten
SONNE = Planet(
    name='Helios (Sonne)',
    M=UnitDecimal('1.989e30', 'kg'),
    mu=UnitDecimal('1.327_1e11', 'km³/s²'),
    a=UnitDecimal(math.nan, 'km'),  # Die Sonne hat keine große Halbachse um sich selber
    R=UnitDecimal('60_000', 'km'),
    v=UnitDecimal(math.nan, 'km/s'),  # Die Sonne hat keine Geschwindigkeit um sich selber
    L0=UnitDecimal(math.nan, "°"),    # Die Sonne kreist nicht um sich selber
    T=UnitDecimal(math.nan, 'a'),   # Kreist nicht um sich selber.
)
ERDE = Planet(
    name='Erde',
    M=UnitDecimal('5.9_742e24', 'kg'),
    mu=UnitDecimal('398_599', 'km³/s²'),
    a=UnitDecimal('149_599_366', 'km'),
    R=UnitDecimal('6_378', 'km'),
    v=UnitDecimal('29.784', 'km/s'),
    L0=UnitDecimal('20.042_7', '°'),
    T=UnitDecimal('1', 'a'),
)
VENUS = Planet(
    name='Venus',
    M=UnitDecimal('4.869e24', 'kg'),
    mu=UnitDecimal('324_860', 'km³/s²'),
    a=UnitDecimal('108_208_777', 'km'),
    R=UnitDecimal('6_052', 'km'),
    v=UnitDecimal('35.020', 'km/s'),
    L0=UnitDecimal('229.096_1', '°'),
    T=UnitDecimal('0.615_2', 'a'),
)
MARS = Planet(
    name='Mars',
    M=UnitDecimal('6.419_1e23', 'kg'),
    mu=UnitDecimal('42_828', 'km³/s²'),
    a=UnitDecimal('227_946_314', 'km'),
    R=UnitDecimal('3_397', 'km'),
    v=UnitDecimal('24.129', 'km/s'),
    L0=UnitDecimal('175.736_5', '°'),
    T=UnitDecimal('1.880_9', 'a'),
)
SATURN = Planet(
    name='Saturn',
    M=UnitDecimal('5.686_e26', 'kg'),
    mu=UnitDecimal('37_930_320', 'km³/s²'),
    a=UnitDecimal('1_425_945_953', 'km'),
    R=UnitDecimal('60_000', 'km'),
    v=UnitDecimal('9.647', 'km/s'),
    L0=UnitDecimal('260.522_9', '°'),
    T=UnitDecimal('29.428_4', 'a'),
)
JUPITER = Planet(
    name='Jupiter',
    M=UnitDecimal('1.898_8e27', 'kg'),
    mu=UnitDecimal('126_687_936', 'km³/s²'),
    a=UnitDecimal('778_344_254', 'km'),
    R=UnitDecimal('71_398', 'km'),
    v=UnitDecimal('13.058', 'km/s'),
    L0=UnitDecimal('23.270_7', '°'),
    T=UnitDecimal('11.867_8', 'a'),
)
# Ab hier sind die Planeten-Daten von Wikipedia. Am besten nochmal mit den in der Aufgabenstellung angegebenen Daten
# vergleichen.
MERKUR = Planet(
    name='Merkur',
    M=UnitDecimal('3.301e23', 'kg'),
    mu=UnitDecimal('398_479', 'km³/s²'),
    a=UnitDecimal('57.909e6', 'km'),
    R=UnitDecimal('4_879', 'km'),
    v=UnitDecimal('47.36', 'km/s'),
    L0=UnitDecimal(math.nan, "°"),    # Unknown
    T=UnitDecimal(math.nan, 'a'),   # Unknown
)
URANUS = Planet(
    name='Uranus',
    M=UnitDecimal('8.681e25', 'kg'),
    mu=UnitDecimal('5_791_963', 'km³/s²'),
    a=UnitDecimal('2_872.4e6', 'km'),
    R=UnitDecimal('51_118', 'km'),
    v=UnitDecimal('6.81', 'km/s'),
    L0=UnitDecimal(math.nan, "°"),    # Unknown
    T=UnitDecimal(math.nan, 'a'),   # Unknown
)
NEPTUN = Planet(
    name='Neptun',
    M=UnitDecimal('1.024e26', 'kg'),
    mu=UnitDecimal('6_832_128', 'km³/s²'),
    a=UnitDecimal('4_495e6', 'km'),
    R=UnitDecimal('49_528', 'km'),
    v=UnitDecimal('5.43', 'km/s'),
    L0=UnitDecimal(math.nan, "°"),    # Unknown
    T=UnitDecimal(math.nan, 'a'),   # Unknown
)
PLUTO = Planet(
    name='Pluto',
    M=UnitDecimal('1.303e22', 'kg'),
    mu=UnitDecimal('869', 'km³/s²'),
    a=UnitDecimal('5.90642e12', 'km'),
    R=UnitDecimal('2374', 'km'),
    v=UnitDecimal('4.67', 'km/s'),
    L0=UnitDecimal(math.nan, "°"),    # Unknown
    T=UnitDecimal(math.nan, 'a'),   # Unknown
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
