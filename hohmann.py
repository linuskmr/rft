# ! Imports nicht optimieren bzw. welche rauslöschen, um in main() via eval() darauf Zugriff zu haben !
import dataclasses
import json
from datetime import timedelta
from typing import Dict
from decimal import *
from lib import ellipse, kreis, allgemein, konstanten
from lib.planet import *
from lib.unit_decimal import UnitDecimal
from dataclasses import dataclass


@dataclass(frozen=True)
class HohmannTransfer:
    ra: UnitDecimal
    """Radius Apozentrum in km."""
    rp: UnitDecimal
    """Radius Perizentrum in km."""
    epsilon: UnitDecimal
    """Numerische Exzentrizität."""
    p: UnitDecimal
    """Bahnparameter p in km."""
    a: UnitDecimal
    """Große Halbachse in km."""
    e: UnitDecimal
    """Lineare Exzentrizität."""
    vp: UnitDecimal
    """Geschwindigkeit am Perizentrum in km/s"""
    vk_start: UnitDecimal
    """Geschwindigkeit auf Kreisbahn um Startplaneten."""
    delta_v1: UnitDecimal
    """Geschwindigkeitsdelta/Schubimpuls Nr.1 in km/s."""
    va: UnitDecimal
    """Geschwindigkeit am Apozentrum in km/s."""
    vk_ziel: UnitDecimal
    """Geschwindigkeit auf Kreisbahn um Zielplaneten."""
    delta_v2: UnitDecimal
    """Geschwindigkeitsdelta/Schubimpuls Nr.2 in km/s."""
    v_total: UnitDecimal
    """Insgesamt benötigter Geschwindigkeitsimpuls in km/s."""
    flugdauer: timedelta
    """Flugdauer des Hohmann Transfers."""


def hohmann(planet: Planet, perizentrum_hoehe: Decimal, apozentrum_hoehe: Decimal) -> HohmannTransfer:
    """
    Berechnet einen Hohmann-Transfer.

    :param planet: Planet, bei dem der Hohmann-Transfer ausgeführt wird.
    :param perizentrum_hoehe: Höhe des Perizentrums über der Oberfläche des Planeten.
    :param apozentrum_hoehe: Höhe des Apozentrums über der Oberfläche des Planeten.
    :return: Sämtliche berechneten Werte.
    """
    print('Hohmann Transfer 🚀')
    print(f'{planet=}')

    perizentrum_hoehe = UnitDecimal(perizentrum_hoehe, 'km')
    apozentrum_hoehe = UnitDecimal(apozentrum_hoehe, 'km')
    rp = UnitDecimal(planet.R + perizentrum_hoehe, 'km')
    ra = UnitDecimal(planet.R + apozentrum_hoehe, 'km')
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
    vk_start = kreis.geschwindigkeit(planet=planet, rk=rp)
    print(f'Bereits vorhandene Kreisbahngeschwindigkeit auf Start-Umlaufbahnhöhe {perizentrum_hoehe}: {vk_start=}')
    delta_v1 = UnitDecimal(vp - vk_start, 'km/s')
    print(f'Schubimpuls Geschwindigkeitsdelta Δv1 = vp - vk_start = {delta_v1}')
    print()

    va = ellipse.apozentrum_geschwindigkeit(planet=planet, ra=ra, epsilon=epsilon, p=p)
    print(f'Benötigte Geschwindigkeit Apozentrum {va=}')
    vk_ziel = kreis.geschwindigkeit(planet=planet, rk=ra)
    print(f'Kreisbahngeschwindigkeit bei Ziel-Umlaufbahnhöhe {apozentrum_hoehe}: {vk_ziel=}')
    delta_v2 = UnitDecimal(vk_ziel - va, 'km/s')
    print(f'Schubimpuls Geschwindigkeitsdelta Δv2 = vk_ziel - va = {delta_v2}')
    print()

    v_total = UnitDecimal(abs(delta_v1) + abs(delta_v2), 'km/s')
    print(f'Benötigter Gesamt-Schubimpuls {v_total=}')
    tu = ellipse.umlaufzeit(planet=planet, a=a)
    flugdauer = 0.5 * tu
    print(f'Flugdauer (Halbe Umlaufzeit der Ellipse): {flugdauer} bzw. {flugdauer.total_seconds()} Sekunden')

    return HohmannTransfer(
        ra=ra, rp=rp, epsilon=epsilon, p=p, a=a, e=e, vp=vp, vk_start=vk_start, delta_v1=delta_v1, va=va,
        vk_ziel=vk_ziel, delta_v2=delta_v2, v_total=v_total, flugdauer=flugdauer
    )


def main():
    """
    Liest die für den Hohmann-Transfer benötigten Parameter von stdin. Dabei werden die Eingaben mittels eval()
    ausgewertet. Daher kann auf Konstanten
    :return:
    """
    print('Hohmann Transfer 🚀 - Eingabe der Parameter')
    # Eingabe lesen. eval() führt Eingabe als Programmcode aus. Daher ist es möglich
    planet = planet_from_name(input('Planet: '))
    R = planet.R
    perizentrum_hoehe = eval(input('Perizentrum Höhe über Planet (in km): '))
    apozentrum_hoehe = eval(input('Apozentrum Höhe über Planet (in km): '))
    print('---')
    data = hohmann(planet=planet, perizentrum_hoehe=perizentrum_hoehe, apozentrum_hoehe=apozentrum_hoehe)
    data_json = json.dumps(dataclasses.asdict(data), indent='  ', default=lambda x: str(x), ensure_ascii=False)
    print()
    print('Raw data:')
    print(data_json)


if __name__ == '__main__':
    main()
