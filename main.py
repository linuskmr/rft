from bahnen.transfer_ellipse import TransferEllipse
from bahnen.ellipse import Ellipse
from bahnen.hohmann import HohmannTransfer
from lib.planet import *
from lib.unit_decimal import UnitDecimal
from datetime import timedelta

ellipse: Ellipse = Ellipse(zentralgestirn=SONNE,
                           ra=UnitDecimal('147_134_000', 'km'),
                           umlaufzeit=timedelta(days=187))

print("Ellipse from WS 20/21 A.6 done")


hohmann: HohmannTransfer = HohmannTransfer(
    ziel_planet=PLUTO,
    start_planet=ERDE
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
