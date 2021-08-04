from bahnen.transfer_ellipse import TransferEllipse
from lib.planet import *
from lib.unit_decimal import UnitDecimal

transfer: TransferEllipse = TransferEllipse(zentralgestirn=SONNE,
                           start_planet=ERDE,
                           ziel_planet=MARS,
                           epsilon=UnitDecimal('0.5237',''),
                           p=MARS.a)

for i in range(10):
    print(transfer.startzeitpunkt_nach_index(i))

print("Done")
