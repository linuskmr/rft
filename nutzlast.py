import json
from decimal import Decimal
from lib.unit_decimal import UnitDecimal, return_unit
from lib.solvable import Solvable


@return_unit('kg')
def nutzlast(*, m0: Decimal, mk: Decimal, mT: Decimal) -> Decimal:
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


def konstruktionsmasse(m0: Decimal, mT: Decimal, mN: Decimal) -> Decimal:
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


def startmasse(*, mK: Decimal, mT: Decimal, mN: Decimal) -> Decimal:
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


def nutzlastverhaeltnis(*, mN: Decimal, m0: Decimal) -> Decimal:
    """
    Berechnet das Nutzlastverhältnis lambda bzw. mN/m0.

    Args:
        mN: Nutzlast in kg.
        m0: Startmasse in kg.

    Returns:
        Decimal: Nutzlastverhältnis lambda bzw. mN/m0.
    """
    return mN / m0


def strukturverhaeltnis(*, mK: Decimal, mT: Decimal) -> Decimal:
    """
    Berechnet das Strukturverhältnis sigma bzw. mK / (mk+mT).

    Args:
        mK: Konstruktionsmasse in kg.
        mT: Treibstoffmasse in kg.

    Returns:
        Decimal: Strukturverhältnis sigma bzw. mK / (mk+mT).
    """
    return mK / (mK + mT)


def massenverhaeltnis(*, m0: Decimal, mb: Decimal) -> Decimal:
    """
    Berechnet das Massenverhältnis r bzw. m0/mb.

    Args:
        m0: Startmasse in kg.
        mb: Brennschlussmasse in kg.

    Returns:
        Decimal: Massenverhältnis r bzw. m0/mb.
    """
    return m0 / mb


class Nutzlast(Solvable):
    mN: UnitDecimal
    """Nutzlast in kg."""
    m0: UnitDecimal
    """Startmasse in kg (Masse Rakete + Treibstoff + Nutzlast)."""
    mK: UnitDecimal
    """Konstruktionsmasse in kg."""
    mb: UnitDecimal
    """Brennschlussmasse in kg (Konstruktionsmasse + Nutzlast)."""
    mT: UnitDecimal
    """Treibstoffmasse in kg."""
    r: UnitDecimal
    """Massenverhältnis (m0/mb)."""
    sigma: UnitDecimal
    """Strukturverhältnis (mK / (mk+mT))"""
    lambda_: UnitDecimal
    """Nutzlastverhältnis (mN/m0)"""

    param_funcs: dict = {
        "mN": [nutzlast],
        "lambda_": [nutzlastverhaeltnis],
        "sigma": [strukturverhaeltnis],
        "r": [massenverhaeltnis],
        "mk": [konstruktionsmasse],
        "m0": [startmasse]
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


def main():
    nutzlast_input_json = input('Nutzlast Data: ')
    nutzlast_input = json.loads(nutzlast_input_json)
    nutzlast_obj = Nutzlast(**nutzlast_input)
    print(json.dumps(nutzlast_obj.__dict__, indent='  ', default=lambda x: str(x)))


if __name__ == '__main__':
    main()
