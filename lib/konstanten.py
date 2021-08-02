from datetime import timedelta
from decimal import *
from lib.unit_decimal import UnitDecimal

SIDERISCHER_WINKELGESCHWINDIGKEIT_GRAD_PRO_TAG = UnitDecimal(Decimal('360') / Decimal('365.2422'), '°/d')
SIDERISCHER_WINKELGESCHWINDIGKEIT_GRAD_PRO_STUNDE = UnitDecimal(
    (360 + SIDERISCHER_WINKELGESCHWINDIGKEIT_GRAD_PRO_TAG) / 24, '°/h'
)
SIDERISCHER_TAG = timedelta(hours=float(360 / SIDERISCHER_WINKELGESCHWINDIGKEIT_GRAD_PRO_STUNDE))
ERDE_GEO_OHNE_ERDRADIUS = UnitDecimal('35_786', 'km')
ERDE_GEO_MIT_ERDRADIUS = UnitDecimal('42_164', 'km')
