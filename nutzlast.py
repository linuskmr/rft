from decimal import Decimal
from lib.unit_decimal import UnitDecimal


class Nutzlast:
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
    """Strukturverhältnis (mk / (mk+mT))"""
    lambda_: UnitDecimal
    """Nutzlastverhältnis (mN/m0)"""

    def __init__(self, *, mN: Decimal, m0: Decimal, mK: Decimal):
        """

        Args:
            mN: Nutzlast in kg.
            m0: Startmasse in kg (Masse Rakete + Treibstoff + Nutzlast).
            mK: Konstruktionsmasse in kg.
        """
        self.mN = mN
        self.m0 = m0
        self.mK = mK
        self.mb = self.mK + self.mN
        self.mT = self.m0 - self.mb
        self.r = self.m0 / self.mb
        self.sigma = self.mK / (self.mK + self.mT)
        self.lambda_ = self.mN / self.m0


