from lib.planet import *
from lib.allgemein import *
from lib import ellipse, kreis, hyperbel, parabel

print('Geschwindigkeit der Erde um die Sonne:', vis_viva(planet=SONNE, r=ERDE.a, epsilon=0, p=ERDE.a))
print('Apozentrum bei p=1000 und epsilon=0.4:', bahngleichung_apozentrum(p=1000, epsilon=0.4))
print(
    'Perizentrumsgeschwindigkeit einer Parabel bei einer Kreisgeschwindigkeit von 21.3:',
    parabel.perizentrum_geschwindigkeit(vk=21.3)
)
