# ! Imports nicht optimieren bzw. welche rauslöschen, um in main() via eval() darauf Zugriff zu haben !
import json
from typing import Dict
from lib import ellipse, kreis, allgemein, konstanten
from lib.planet import *
from lib.unit_float import UnitFloat
from hohmann import hohmann


def print_mission_ablauf():
    print('Ablauf der Mission')
    print('1. Bahnaufstieg')
    print('2. Flucht aus dem Gravitationsfeld des Startplaneten')
    print('3. Übergang zum Zielplaneten (Hohmann-Transfer)')
    print('4. Einschwenken in den Orbit um die Zielplaneten')


def bahnaufstieg_1() -> Dict[str, float]:
    # TODO: Tatsächlichen Wert ausrechnen
    print('1. Bahnaufstieg in eine 200-km-Bahn.')
    delta_v = 9.58
    print(f'TODO: Fester Wert für eine 200km Umlaufbahn: {delta_v=}')
    return {
        'delta_v': delta_v
    }


def uebergang_zielplanet_3(*, start_planet: Planet, ziel_planet: Planet) -> Dict[str, float]:
    print('3. Übergang zum Zielplaneten')
    uebergang_zielplanet_data = hohmann(planet=SONNE, perizentrum_hoehe=start_planet.a, apozentrum_hoehe=ziel_planet.a)
    return uebergang_zielplanet_data


def flucht_gravitationsfeld_2(start_planet: Planet, start_planet_hoehe_umlaufbahn: float) -> Dict[str, float]:
    start_planet_hoehe_umlaufbahn = UnitFloat(start_planet_hoehe_umlaufbahn, 'km')

    print(f'2. Flucht aus dem Gravitationsfeld des Startplaneten {start_planet}')

    start_planet_r = UnitFloat(start_planet.R + start_planet_hoehe_umlaufbahn, 'km')
    print(f'Berechne bereits vorhandene Kreisbahngeschwindigkeit auf Umlaufbahn {start_planet_r=}')
    vk = kreis.geschwindigkeit(planet=start_planet, r=start_planet_r)
    print(f'{vk=}')

    return {
        'vk': vk
    }


def mission(
        start_planet: Planet, ziel_planet: Planet, start_planet_hoehe_umlaufbahn: float
) -> Dict[str, Dict[str, float]]:
    print_mission_ablauf()
    print('\n---\n')
    bahnaufstieg_data = bahnaufstieg_1()
    print('\n---\n')
    uebergang_zielplanet_data = uebergang_zielplanet_3(start_planet=start_planet, ziel_planet=ziel_planet)
    print('\n---\n')
    flucht_gravitationsfeld_data = flucht_gravitationsfeld_2(
        start_planet=start_planet, start_planet_hoehe_umlaufbahn=start_planet_hoehe_umlaufbahn
    )
    print('\n---\n')

    return {
        'Bahnaufstieg': bahnaufstieg_data,
        'Übergang Zielplanet': uebergang_zielplanet_data,
        'Flucht Gravitationsfeld': flucht_gravitationsfeld_data,
    }


def main():
    print('Vollständige Mission 🚀 - Eingabe der Parameter')
    # Eingabe lesen
    start_planet = planet_from_name(input('Start Planet: '))
    start_planet_hoehe_umlaufbahn = UnitFloat(float(input('Höhe Umlaufbahn (in km): ')), 'km')
    ziel_planet = planet_from_name(input('Ziel Planet: '))
    print('---')
    data = mission(
        start_planet=start_planet, ziel_planet=ziel_planet, start_planet_hoehe_umlaufbahn=start_planet_hoehe_umlaufbahn
    )
    data_json = json.dumps(data, indent='  ', default=lambda x: str(x), ensure_ascii=False)
    print()
    print('Raw data:')
    print(data_json)


if __name__ == '__main__':
    main()
