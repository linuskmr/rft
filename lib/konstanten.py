from datetime import timedelta
from decimal import *
from lib.unit_decimal import UnitDecimal

SIDERISCHER_WINKELGESCHWINDIGKEIT_GRAD_PRO_TAG = UnitDecimal(Decimal('360') / Decimal('365.2422'), '°/d')
SIDERISCHER_WINKELGESCHWINDIGKEIT_GRAD_PRO_STUNDE = UnitDecimal(
    (360 + SIDERISCHER_WINKELGESCHWINDIGKEIT_GRAD_PRO_TAG) / 24, '°/h'
)
SIDERISCHER_TAG = timedelta(hours=float(360 / SIDERISCHER_WINKELGESCHWINDIGKEIT_GRAD_PRO_STUNDE))
GEO_HOEHE = UnitDecimal('35_786', 'km')
GEO_RADIUS = UnitDecimal('42_164', 'km')
