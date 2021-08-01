# ! Imports nicht optimieren bzw. welche rauslöschen, um in main() via eval() darauf Zugriff zu haben !
import json
from typing import Dict
from lib import ellipse, kreis, allgemein, konstanten, hyperbel
from lib.planet import *
from lib.unit_float import UnitFloat


def fluchthyperbel(planet: Planet, vinf: float, hp: float) -> Dict[str, float]:
    vinf = UnitFloat(vinf, 'km/s')
    hp = UnitFloat(hp, 'km')

    print('Fluchthyperbel 🚀')
    print(f'Planet {planet}')
    print(f'Geschwindigkeit im Unendlichen {vinf=}')
    print()

    a = hyperbel.grosse_halbachse_planet_vinf(planet=planet, vinf=vinf)
    print(f'Große Halbachse {a=}')

    rp = hp + planet.R
    print(f'Radius Perizentrum: {rp=}')

    epsilon = hyperbel.numerische_exzentrizitaet(a=a, rp=rp)
    print(f'Numerische Exzentrizität {epsilon=}')

    p = hyperbel.bahnparameter_p(a=a, epsilon=epsilon)
    print(f'Bahnparameter {p=}')

    grosses_epsilon = hyperbel.umlenkwinkel(epsilon=epsilon)
    print(f'Umlenkwinkel {grosses_epsilon}')

    psi_inf = hyperbel.unendlichkeitsanomalie(epsilon=epsilon)
    print(f'Unendlichkeitsanomalie {psi_inf=}')

    return {
        'vinf': vinf, 'hp': hp, 'a': a, 'rp': rp, 'epsilon': epsilon, 'p': p, 'grosses_epsilon': grosses_epsilon,
        'psi_inf': psi_inf
    }


def main():
    print('Fluchthyperbel 🚀 - Eingabe der Parameter')
    planet = planet_from_name(input('Planet: '))
    vinf = float(input('Geschwindigkeit im Unendlichen vinf (in km/s): '))
    hp = float(input('Höhe Perizentrum über Planetenoberfläche (in km): '))
    print('---')
    data = fluchthyperbel(planet=planet, vinf=vinf, hp=hp)
    data_json = json.dumps(data, indent='  ', default=lambda x: str(x), ensure_ascii=False)
    print()
    print('Raw data:')
    print(data_json)


if __name__ == '__main__':
    main()
