import dataclasses
import json
from typing import Dict
from decimal import *

from bahnaufstieg import bahnaufstieg, Bahnaufstieg
from fluchthyperbel import fluchthyperbel, Fluchthyperbel
from lib.planet import *
from lib.unit_decimal import UnitDecimal
from hohmann import hohmann, HohmannTransfer
from dataclasses import dataclass


@dataclass(frozen=True)
class Mission:
    bahnaufstieg_1: Bahnaufstieg
    """1. Das Starten der Rakete von der Oberfläche des Startplaneten in einen niedrigen Orbit."""
    flucht_gravitationsfeld_2: Fluchthyperbel
    """2. Die Flucht aus dem Gravitationsfeld des Startplaneten."""
    uebergang_zielplanet_3: HohmannTransfer
    """3. Der Hohmann-Transfeer vom Startplaneten zum Zielplaneten."""
    einschwenken_orbit_zielplanet_4: Fluchthyperbel
    """4. Eine 'umgedrehte' Fluchthyperbel zum Einschwenken in den Orbit um den Zielplaneten."""


def print_mission_ablauf():
    """Gibt den Missionsablauf aus."""

    print('Ablauf der Mission')
    print('1. Bahnaufstieg')
    print('2. Flucht aus dem Gravitationsfeld des Startplaneten')
    print('3. Übergang zum Zielplaneten (Hohmann-Transfer)')
    print('4. Einschwenken in den Orbit um die Zielplaneten')


def bahnaufstieg_1() -> Bahnaufstieg:
    """
    Berechnet den Bahnaufstieg vom Startplaneten.

    :return: Sämtliche berechneten Werte.
    """
    return bahnaufstieg()


def uebergang_zielplanet_3(*, start_planet: Planet, ziel_planet: Planet) -> HohmannTransfer:
    """
    Berechnet den Hohmann-Transfer (Ellipse) vom Startplaneten zum Zielplanten.

    :param start_planet: Startplanet.
    :param ziel_planet: Zielplanet.
    :return: Sämtliche berechneten Werte.
    """
    print('3. Übergang zum Zielplaneten')
    uebergang_zielplanet_data = hohmann(planet=SONNE, perizentrum_hoehe=start_planet.a, apozentrum_hoehe=ziel_planet.a)
    return uebergang_zielplanet_data


def flucht_gravitationsfeld_2(planet: Planet, hp: Decimal, vinf: Decimal) -> Fluchthyperbel:
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
    return fluchthyperbel(planet=planet, hp=hp, vinf=vinf)


def einschwenken_orbit_zielplanet_4(ziel_planet: Planet, hp: Decimal, vinf: Decimal) -> Fluchthyperbel:
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
) -> Mission:
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
        planet=start_planet, hp=start_planet_hoehe_umlaufbahn, vinf=uebergang_zielplanet_3_data.vp
    )
    print('\n---\n')
    einschwenken_orbit_zielplanet_4_data = einschwenken_orbit_zielplanet_4(
        ziel_planet=ziel_planet, hp=ziel_planet_hoehe_umlaufbahn, vinf=uebergang_zielplanet_3_data.va
    )

    return Mission(
        bahnaufstieg=bahnaufstieg_1_data,
        uebergang_zielplanet=uebergang_zielplanet_3_data,
        flucht_gravitationsfeld=flucht_gravitationsfeld_2_data,
        einschwenken_orbit_zielplanet=einschwenken_orbit_zielplanet_4_data
    )


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
    data_json = json.dumps(dataclasses.asdict(data), indent='  ', default=lambda x: str(x), ensure_ascii=False)
    print()
    print('Raw data:')
    print(data_json)


if __name__ == '__main__':
    main()
