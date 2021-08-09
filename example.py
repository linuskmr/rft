from bahnen.transfer_ellipse import TransferEllipse
from bahnen.ellipse import Ellipse
from bahnen.hohmann import HohmannTransfer
from lib.planet import *
from lib.unit_decimal import UnitDecimal
from datetime import timedelta
from lib.konstanten import *

ellipse: Ellipse = Ellipse(zentralgestirn=SONNE,
                           ra=UnitDecimal('147_134_000', 'km'),
                           umlaufzeit=timedelta(days=187))

print("Ellipse from WS 20/21 A.6 done")


hohmann: HohmannTransfer = HohmannTransfer(
    zentralgestirn=SONNE,
    ziel_planet=PLUTO,
    start_planet=ERDE
)

print(hohmann.transfer_dauer)


#! TODO Delta v1 und v2 können nicht ausgerechenet werden, sollte aber möglich sein!
hohmann: HohmannTransfer = HohmannTransfer(
    zentralgestirn=ERDE,
    rp=ERDE.R + 200,
    ra=GEO_RADIUS
)

print(hohmann.transfer_dauer)


transfer: TransferEllipse = TransferEllipse(zentralgestirn=SONNE,
                           start_planet=ERDE,
                           ziel_planet=MARS,
                           epsilon=UnitDecimal('0.5237',''),
                           p=MARS.a)

for i in range(10):
    print(transfer.startzeitpunkt_nach_index(i))

print("Done")
