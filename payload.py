import json
from decimal import Decimal
from lib.unit_decimal import UnitDecimal, return_unit
from lib.solvable import Solvable


@return_unit('kg')
def payload(*, m0: Decimal, mk: Decimal, mT: Decimal) -> Decimal:
    """
    Berechnet die Nutzlast mN aus m0, mK und mT.

    Args:
        m0: Startmasse in kg.
        mk: Konstruktionsmasse in kg.
        mT: Treibstoffmasse in kg.

    Returns:
        Decimal: Nutzlast mN in kg.
    """
    return m0 - mk - mT


def structural_mass(m0: Decimal, mT: Decimal, mN: Decimal) -> Decimal:
    """
    Berechnet die Konstruktionsmasse mK aus m0, mT und mN.
    Args:
        m0: Startmasse in kg.
        mT: Treibstoffmasse in kg.
        mN: Nutzlast in kg.

    Returns:
        Decimal: Konstruktionsmasse mK in kg.
    """
    return m0 - mT - mN


def launch_mass(*, mK: Decimal, mT: Decimal, mN: Decimal) -> Decimal:
    """
    Berechnet die Startmasse m0 aus mK, mT und mN.
    Args:
        mK: Konstruktionsmasse in kg.
        mT: Treibstoffmasse in kg.
        mN: Nutzlast in kg.

    Returns:
        Decimal: Startmasse m0 in kg.
    """
    return mK + mT + mN


def payload_ratio(*, mN: Decimal, m0: Decimal) -> Decimal:
    """
    Berechnet das Nutzlastverhältnis lambda bzw. mN/m0.

    Args:
        mN: Nutzlast in kg.
        m0: Startmasse in kg.

    Returns:
        Decimal: Nutzlastverhältnis lambda bzw. mN/m0.
    """
    return mN / m0


def structural_ratio(*, mK: Decimal, mT: Decimal) -> Decimal:
    """
    Berechnet das Strukturverhältnis sigma bzw. mK / (mk+mT).

    Args:
        mK: Konstruktionsmasse in kg.
        mT: Treibstoffmasse in kg.

    Returns:
        Decimal: Strukturverhältnis sigma bzw. mK / (mk+mT).
    """
    return mK / (mK + mT)


def mass_ratio(*, m0: Decimal, mb: Decimal) -> Decimal:
    """
    Berechnet das Massenverhältnis r bzw. m0/mb.

    Args:
        m0: Startmasse in kg.
        mb: Brennschlussmasse in kg.

    Returns:
        Decimal: Massenverhältnis r bzw. m0/mb.
    """
    return m0 / mb


class Payload(Solvable):
    mN: UnitDecimal
    """Payload in kg."""
    m0: UnitDecimal
    """Launch mass in kg (mass of rocket + propellant + payload)."""
    mK: UnitDecimal
    """Structural mass in kg."""
    mb: UnitDecimal
    """Burnout mass in kg (structural mass + payload)."""
    mT: UnitDecimal
    """Propellant in kg."""
    r: UnitDecimal
    """Mass ratio (m0/mb)."""
    sigma: UnitDecimal
    """Structural ratio (mK / (mk+mT))"""
    lambda_: UnitDecimal
    """Payload ratio (mN/m0)"""

    param_funcs: dict = {
        "mN": [payload],
        "lambda_": [payload_ratio],
        "sigma": [structural_ratio],
        "r": [mass_ratio],
        "mk": [structural_mass],
        "m0": [launch_mass]
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


def main():
    payload_input_json = input('Payload JSON Data: ')
    payload_input = json.loads(payload_input_json)
    payload_obj = Payload(**payload_input)
    print(json.dumps(payload_obj.__dict__, indent='  ', default=lambda x: str(x)))


if __name__ == '__main__':
    main()
