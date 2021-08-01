import json
from typing import Dict
from lib import kreis, hyperbel
from lib.planet import *
from lib.unit_float import UnitFloat


def fluchthyperbel(planet: Planet, vinf: float, hp: float) -> Dict[str, float]:
    vinf = UnitFloat(vinf, 'km/s')
    hp = UnitFloat(hp, 'km')

    print('Fluchthyperbel 🚀')
    print(f'{planet}')
    print(f'Geschwindigkeit im Unendlichen {vinf=}')
    print(f'Höhe über Perizentrum {hp=}')
    print()

    rp = hp + planet.R
    print(f'Radius Perizentrum {rp=}')
    a = hyperbel.grosse_halbachse_planet_vinf(planet=planet, vinf=vinf)
    print(f'Große Halbachse {a=}')
    epsilon = hyperbel.numerische_exzentrizitaet(a=a, rp=rp)
    print(f'Numerische Exzentrizität {epsilon=}')
    p = hyperbel.bahnparameter_p(a=a, epsilon=epsilon)
    print(f'Bahnparameter {p=}')
    grosses_epsilon = hyperbel.umlenkwinkel(epsilon=epsilon)
    print(f'Umlenkwinkel {grosses_epsilon}')
    psi_inf = hyperbel.unendlichkeitsanomalie(epsilon=epsilon)
    print(f'Unendlichkeitsanomalie {psi_inf=}')
    vk = kreis.geschwindigkeit(planet=planet, r=rp)
    print(f'Bereits vorhandene Kreisbahngeschwindigkeit bei Perizentrum mit Radius {rp}: {vk=}')
    vp = hyperbel.perizentrum_geschwindigkeit(vk=vk, vinf=vinf)
    print(f'Perizentrumsgeschwindigkeit {vp=}')
    v_total = vp - vk
    print(f'Benötigter Gesamtschubimpuls {v_total}')

    return {
        'vinf': vinf, 'hp': hp, 'a': a, 'rp': rp, 'epsilon': epsilon, 'p': p, 'grosses_epsilon': grosses_epsilon,
        'psi_inf': psi_inf, 'vk': vk, 'vp': vp, 'v_total': v_total
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
