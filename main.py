from lib.planet import *
from lib.allgemein import *
from lib import ellipse, kreis, hyperbel, parabel

print('Geschwindigkeit der Erde um die Sonne:', vis_viva_r_epsilon_p(planet=SONNE, r=ERDE.a, epsilon=0, p=ERDE.a))
print('Apozentrum bei p=1000 und epsilon=0.4:', bahngleichung_apozentrum(p=1000, epsilon=0.4))
print(
    'Perizentrumsgeschwindigkeit einer Parabel bei einer Kreisgeschwindigkeit von 21.3:',
    parabel.perizentrum_geschwindigkeit(vk=21.3)
)

print(ellipse.umlaufzeit(planet=ERDE, a=ERDE.R + 200000))

# 200 km um die Erde
print(vis_viva_r_epsilon_p(planet=ERDE, r=ERDE.R + 200, epsilon=0, p=ERDE.R + 200))
