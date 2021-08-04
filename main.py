from lib.ellipse import Ellipse
from lib.planet import *
from lib.unit_decimal import UnitDecimal

el = Ellipse(a=UnitDecimal('463_971_810', 'km'),
             e=UnitDecimal('314_372_451', 'km'),
             zentralgestirn=SONNE)

print(el.p)
