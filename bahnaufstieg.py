from dataclasses import dataclass
from lib.unit_decimal import UnitDecimal


@dataclass(frozen=True)
class Bahnaufstieg:
    v_total: UnitDecimal
    """Insgesamt benötigter Schubimpuls in km/s."""


def bahnaufstieg() -> Bahnaufstieg:
    """
    Berechnet den Bahnaufstieg vom Startplaneten.

    :return: Sämtliche berechneten Werte.
    """
    # TODO: Tatsächlichen Wert ausrechnen
    print('Bahnaufstieg in eine 200-km-Bahn.')
    v_total = UnitDecimal(9.58, 'km/s')
    print(f'TODO: Fester Wert für eine 200km Umlaufbahn: {v_total=}')
    return Bahnaufstieg(v_total=v_total)