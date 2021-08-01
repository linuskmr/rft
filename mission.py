import json
from typing import Dict
from decimal import *
from fluchthyperbel import fluchthyperbel
from lib.planet import *
from lib.unit_decimal import UnitDecimal
from hohmann import hohmann


def print_mission_ablauf():
    """Gibt den Missionsablauf aus."""

    print('Ablauf der Mission')
    print('1. Bahnaufstieg')
    print('2. Flucht aus dem Gravitationsfeld des Startplaneten')
    print('3. Übergang zum Zielplaneten (Hohmann-Transfer)')
    print('4. Einschwenken in den Orbit um die Zielplaneten')


def bahnaufstieg_1() -> Dict[str, Decimal]:
    """
    Berechnet den Bahnaufstieg vom Startplaneten.

    :return: Sämtliche berechneten Werte.
    """
    # TODO: Tatsächlichen Wert ausrechnen
    print('1. Bahnaufstieg in eine 200-km-Bahn.')
    delta_v = 9.58
    print(f'TODO: Fester Wert für eine 200km Umlaufbahn: {delta_v=}')
    return {
        'delta_v': delta_v
    }


def uebergang_zielplanet_3(*, start_planet: Planet, ziel_planet: Planet) -> Dict[str, Decimal]:
    """
    Berechnet den Hohmann-Transfer (Ellipse) vom Startplaneten zum Zielplanten.

    :param start_planet: Startplanet.
    :param ziel_planet: Zielplanet.
    :return: Sämtliche berechneten Werte.
    """
    print('3. Übergang zum Zielplaneten')
    uebergang_zielplanet_data = hohmann(planet=SONNE, perizentrum_hoehe=start_planet.a, apozentrum_hoehe=ziel_planet.a)
    return uebergang_zielplanet_data


def flucht_gravitationsfeld_2(planet: Planet, hp: Decimal, vinf: Decimal) -> Dict[str, Decimal]:
    """
    2. Berechnet die Flucht aus dem Gravtiationsfeld des Startplaneten.
    
    :param planet: Planet, aus dessen Gravitationsfeld geflohen werden soll.
    :param hp: Höhe des Perizentrums über der Planetenoberfläche in km.
    :param vinf: Hyperbolische Exzessgeschwindigkeit im Unendlichen in km/s.
    :return: 
    """
    print(f'2. Flucht aus dem Gravitationsfeld von Start {planet}')
    print(f'Berechne Fluchthyperbel von {planet=}')
    print(f'Höhe des Perizentrums über der Planetenoberfläche {hp=}')
    print(f'Exzessgeschwindigkeit delta_v1 (vom Hohmann-Übergang) {vinf=}')
    fluchthyperbel_data = fluchthyperbel(planet=planet, hp=hp, vinf=vinf)
    return fluchthyperbel_data


def einschwenken_orbit_zielplanet_4(ziel_planet: Planet, hp: Decimal, vinf: Decimal) -> Dict[str, Decimal]:
    """
    4. Berechnet das Einschwenken in den Orbit des Zielplanten.

    :param ziel_planet: Zielplanet.
    :param hp: Höhe des Perizentrums über der Planetenoberfläche in km.
    :param vinf: Hyperbolische Exzessgeschwindigkeit; Geschwindigkeit im Unendlichen; Hier Anflugggeschwindigkeit in
    km/s.
    :return: Daten der Hyperbel.
    """
    print(f'4. Einschwenken in Orbit um den Zielplaneten')
    print(f'{ziel_planet=}')
    print(f'Höhe Perizentrum über Plantenoberfläche {hp=}')
    print(f'Anfluggeschwindigkeit vom Hohmann-Transfer (va) hier als hyperbolische Exzessgeschwindigkeit {vinf=}')
    return fluchthyperbel(planet=ziel_planet, hp=hp, vinf=ziel_planet.v)


def mission(
        start_planet: Planet, ziel_planet: Planet, start_planet_hoehe_umlaufbahn: Decimal,
        ziel_planet_hoehe_umlaufbahn: Decimal
) -> Dict[str, Dict[str, Decimal]]:
    """
    Berechnet eine vollständige Mission vom Startplanten zum Zielplaneten.

    :param start_planet: Startplanet.
    :param ziel_planet: Zielplanet.
    :param start_planet_hoehe_umlaufbahn: Die Höhe der Umlaufbahn über der Planetenoberfläche des Startplaneten.
    :param ziel_planet_hoehe_umlaufbahn: Die Höhe der Umlaufbahn über der Planetenoberfläche des Zielplanten.
    :return: Sämtliche berechneten Werte.
    """
    print_mission_ablauf()
    print('\n---\n')
    bahnaufstieg_1_data = bahnaufstieg_1()
    print('\n---\n')
    uebergang_zielplanet_3_data = uebergang_zielplanet_3(start_planet=start_planet, ziel_planet=ziel_planet)
    print('\n---\n')
    flucht_gravitationsfeld_2_data = flucht_gravitationsfeld_2(
        planet=start_planet, hp=start_planet_hoehe_umlaufbahn, vinf=uebergang_zielplanet_3_data['vp']
    )
    print('\n---\n')
    einschwenken_orbit_zielplanet_4_data = einschwenken_orbit_zielplanet_4(
        ziel_planet=ziel_planet, hp=ziel_planet_hoehe_umlaufbahn, vinf=uebergang_zielplanet_3_data['va']
    )

    return {
        'Bahnaufstieg': bahnaufstieg_1_data,
        'Übergang Zielplanet': uebergang_zielplanet_3_data,
        'Flucht Gravitationsfeld': flucht_gravitationsfeld_2_data,
        'Einschwenken Orbit Zielplanet': einschwenken_orbit_zielplanet_4_data
    }


def main():
    print('Vollständige Mission 🚀 - Eingabe der Parameter')
    # Eingabe lesen
    start_planet = planet_from_name(input('Startplanet: '))
    start_planet_hoehe_umlaufbahn = UnitDecimal(Decimal(
        input('Höhe Umlaufbahn über Plantenoberfläche des Startplanten (in km): ')
    ), 'km')
    ziel_planet = planet_from_name(input('Zielplanet: '))
    ziel_planet_hoehe_umlaufbahn = UnitDecimal(Decimal(
        input('Höhe Umlaufbahn über Plantenoberfläche des Zielplanten (in km): ')
    ), 'km')
    print('---')
    data = mission(
        start_planet=start_planet, ziel_planet=ziel_planet, start_planet_hoehe_umlaufbahn=start_planet_hoehe_umlaufbahn,
        ziel_planet_hoehe_umlaufbahn=ziel_planet_hoehe_umlaufbahn
    )
    data_json = json.dumps(data, indent='  ', default=lambda x: str(x), ensure_ascii=False)
    print()
    print('Raw data:')
    print(data_json)


if __name__ == '__main__':
    main()
