# ! Imports nicht optimieren bzw. welche rauslöschen, um in main() via eval() darauf Zugriff zu haben !
import json
from typing import Dict
from lib import ellipse, kreis, allgemein, konstanten
from lib.planet import *
from lib.unit_float import UnitFloat


def hohmann(planet: Planet, perizentrum_hoehe: float, apozentrum_hoehe: float) -> Dict[str, float]:
    """
    Berechnet einen Hohmann-Transfer.

    :param planet: Planet, bei dem der Hohmann-Transfer ausgeführt wird.
    :param perizentrum_hoehe: Höhe des Perizentrums über der Oberfläche des Planeten.
    :param apozentrum_hoehe: Höhe des Apozentrums über der Oberfläche des Planeten.
    :return: Sämtliche berechneten Werte.
    """
    print('Hohmann Transfer 🚀')
    print(f'{planet=}')

    perizentrum_hoehe = UnitFloat(perizentrum_hoehe, 'km')
    apozentrum_hoehe = UnitFloat(apozentrum_hoehe, 'km')
    rp = UnitFloat(planet.R + perizentrum_hoehe, 'km')
    ra = UnitFloat(planet.R + apozentrum_hoehe, 'km')
    print(f'Start Umlaufbahnhöhe: {perizentrum_hoehe}')
    print(f'Radius Perizentrum (Start Umlaufbahnhöhe + Radius des Planeten): {rp=}')
    print(f'Ziel Umlaufbahnhöhe: {apozentrum_hoehe}')
    print(f'Radius Apozentrum (Ziel Umlaufbahnhöhe + Radius des Planeten): {ra=}')
    print()

    print('Berechne allgemeine Parameter der Übergangsellipse:')
    epsilon = allgemein.numerische_exzentrizitaet_ra_rp(rp=rp, ra=ra)
    print(f'Numerische Exzentrizität {epsilon=}')
    p = ellipse.bahnparameter_p(rp=ra, epsilon=epsilon)
    print(f'Bahnparameter {p=}')
    a = ellipse.grosse_halbachse_ra_rp(rp=rp, ra=ra)
    print(f'Große Halbachse {a=}')
    e = ellipse.lineare_exzentrizitaet(a=a, rp=rp)
    print(f'Lineare Exzentrizität {e=}')
    print()

    vp = ellipse.perizentrum_geschwindigkeit_rp_ra(planet=planet, ra=ra, rp=rp)
    print(f'Benötigte Geschwindigkeit Perizentrum {vp=}')
    vk_start = kreis.geschwindigkeit(planet=planet, r=rp)
    print(f'Bereits vorhandene Kreisbahngeschwindigkeit auf Start-Umlaufbahnhöhe {perizentrum_hoehe}: {vk_start=}')
    delta_v1 = UnitFloat(vp - vk_start, 'km/s')
    print(f'Schubimpuls Geschwindigkeitsdelta Δv1 = vp - vk_start = {delta_v1}')
    print()

    va = ellipse.apozentrum_geschwindigkeit(planet=planet, ra=ra, epsilon=epsilon, p=p)
    print(f'Benötigte Geschwindigkeit Apozentrum {va=}')
    vk_ziel = kreis.geschwindigkeit(planet=planet, r=ra)
    print(f'Kreisbahngeschwindigkeit bei Ziel-Umlaufbahnhöhe {apozentrum_hoehe}: {vk_ziel=}')
    delta_v2 = UnitFloat(vk_ziel - va, 'km/s')
    print(f'Schubimpuls Geschwindigkeitsdelta Δv2 = vk_ziel - va = {delta_v2}')
    print()

    v_total = UnitFloat(abs(delta_v1) + abs(delta_v2), 'km/s')
    print(f'Benötigter Gesamt-Schubimpuls {v_total=}')
    tu = ellipse.umlaufzeit(planet=planet, a=a)
    flugdauer = 0.5 * tu
    print(f'Flugdauer (Halbe Umlaufzeit der Ellipse): {flugdauer} bzw. {flugdauer.total_seconds()} Sekunden')

    data = {
        'ra': ra, 'rp': rp, 'epsilon': epsilon, 'p': p, 'a': a, 'e': e, 'vp': vp, 'vk_start': vk_start,
        'delta_v1': delta_v1, 'va': va, 'vk_ziel': vk_ziel, 'delta_v2': delta_v2, 'v_total': v_total,
        'flugdauer': flugdauer
    }
    return data


def main():
    """
    Liest die für den Hohmann-Transfer benötigten Parameter von stdin. Dabei werden die Eingaben mittels eval()
    ausgewertet. Daher kann auf Konstanten
    :return:
    """
    print('Hohmann Transfer 🚀 - Eingabe der Parameter')
    # Eingabe lesen. eval() führt Eingabe als Programmcode aus. Daher ist es möglich
    planet = planet_from_name(input('Planet: '))
    perizentrum_hoehe = eval(input('Perizentrum Höhe über Planet (in km): '))
    apozentrum_hoehe = eval(input('Apozentrum Höhe über Planet (in km): '))
    print('---')
    data = hohmann(planet=planet, perizentrum_hoehe=perizentrum_hoehe, apozentrum_hoehe=apozentrum_hoehe)
    data_json = json.dumps(data, indent='  ', default=lambda x: str(x), ensure_ascii=False)
    print()
    print('Raw data:')
    print(data_json)


if __name__ == '__main__':
    main()
