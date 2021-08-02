import dataclasses
import json
from typing import Dict
from decimal import *
from lib import kreis, hyperbel
from lib.planet import *
from lib.unit_decimal import UnitDecimal
from dataclasses import dataclass


@dataclass(frozen=True)
class Fluchthyperbel:
    vinf: UnitDecimal
    """Hyperbolische Exzessgeschwindigkeit; Geschwindigkeit im Unendlichen in km/s."""
    hp: UnitDecimal
    """Höhe über dem Perizentrum in km."""
    a: UnitDecimal
    """Große Halbachse in km."""
    rp: UnitDecimal
    """Radius des Perizentrums in km."""
    epsilon: UnitDecimal
    """Numerische Exzentrizität."""
    p: UnitDecimal
    """Bahnparameter p in km."""
    grosses_epsilon: UnitDecimal
    """"""
    psi_inf: UnitDecimal
    """"""
    vk: UnitDecimal
    """Kreisbahngeschwindigkeit am Perizentrum in km/s."""
    vp: UnitDecimal
    """Geschwindigkeit am Perizentrum in km/s."""
    v_total: UnitDecimal
    """Insgesamt benötigter Schubimpuls in km/s."""


def fluchthyperbel(planet: Planet, vinf: Decimal, hp: Decimal) -> Fluchthyperbel:
    """
    Berechnet eine Fluchthyperbel am Startplaneten.

    :param planet: Planet, an dem die Fluchthyperbel berechnet werden soll.
    :param hp: Höhe des Perizentrums über der Planetenoberfläche in km.
    :param vinf: Hyperbolische Exzessgeschwindigkeit im Unendlichen in km/s.
    :return: Sämtliche berechneten Werte.
    """

    vinf = UnitDecimal(vinf, 'km/s')
    hp = UnitDecimal(hp, 'km')

    print('Fluchthyperbel 🚀')
    print(f'{planet=}')
    print(f'Hyperbolische Exzessgeschwindigkeit; Geschwindigkeit im Unendlichen {vinf=}')
    print(f'Höhe über Perizentrum {hp=}')
    rp = hp + planet.R
    print(f'Radius Perizentrum (Höhe Perizentrum + Radius Planet) {rp=}')
    print()

    a = hyperbel.grosse_halbachse_planet_vinf(planet=planet, vinf=vinf)
    print(f'Große Halbachse {a=}')
    ra = hyperbel.apozentrum_radius_a_rp(a=a, rp=rp)
    print(f'Radius Apozentrum {ra=}')
    epsilon = hyperbel.numerische_exzentrizitaet(a=a, ra=ra)
    print(f'Numerische Exzentrizität {epsilon=}')
    e = hyperbel.lineare_exzentrizitaet(a=a, rp=rp)
    print(f'Lineare Exzentrizität {e=}')
    b = hyperbel.kleine_halbachse(a=a, e=e)
    print(f'Kleine Halbachse {b=}')
    p = hyperbel.bahnparameter_p(a=a, epsilon=epsilon)
    print(f'Bahnparameter {p=}')
    grosses_epsilon = hyperbel.umlenkwinkel(epsilon=epsilon)
    print(f'Umlenkwinkel {grosses_epsilon}')
    psi_inf = hyperbel.unendlichkeitsanomalie(epsilon=epsilon)
    print(f'Unendlichkeitsanomalie {psi_inf=}')
    vk = kreis.geschwindigkeit(planet=planet, rk=rp)
    print()

    print(f'Bereits vorhandene Kreisbahngeschwindigkeit bei Perizentrum mit Radius {rp}: {vk=}')
    vp = hyperbel.perizentrum_geschwindigkeit(vk=vk, vinf=vinf)
    print(f'Benötigte Perizentrumsgeschwindigkeit {vp=}')
    v_total = UnitDecimal(vp - vk, 'km/s')
    print(f'Benötigter Gesamtschubimpuls {v_total=}')

    return Fluchthyperbel(
        vinf=vinf, hp=hp, a=a, rp=rp, epsilon=epsilon, p=p, grosses_epsilon=grosses_epsilon, psi_inf=psi_inf, vk=vk,
        vp=vp, v_total=v_total
    )


def main():
    print('Fluchthyperbel 🚀 - Eingabe der Parameter')
    planet = planet_from_name(input('Planet: '))
    vinf = Decimal(input('Geschwindigkeit im Unendlichen vinf (in km/s): '))
    hp = Decimal(input('Höhe Perizentrum über Planetenoberfläche (in km): '))
    print('---')
    data = fluchthyperbel(planet=planet, vinf=vinf, hp=hp)
    data_json = json.dumps(dataclasses.asdict(data), indent='  ', default=lambda x: str(x), ensure_ascii=False)
    print()
    print('Raw data:')
    print(data_json)


if __name__ == '__main__':
    main()
