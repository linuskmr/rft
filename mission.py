import dataclasses
import json
from typing import Optional

from ascent_trajectory import ascent_trajectory, Bahnaufstieg
from escape_hyperbola import fluchthyperbel, EscapeHyperbola
from lib.planet import *
from lib.solvable import Solvable
from lib.unit_decimal import UnitDecimal
from bahnen.hohmann import HohmannTransfer
from dataclasses import dataclass


@dataclass(frozen=True)
class Mission:
    ascent_trajectory_1: Optional[AscentTrajectory]
    """1. Launching the rocket from the surface of the departure planet into a low orbit."""
    escape_gravitational_field_2: EscapeHyperbola
    """2. Escaping the gravitational field of the departure planet."""
    transfer_to_target_planet_3: HohmannTransfer
    """3. The Hohmann transfer from the departure planet to the target planet."""
    insertion_orbit_target_planet_4: EscapeHyperbola
    """4. A 'reversed' escape hyperbola to the enter orbit around the target planet."""
    delta_v_total: UnitDecimal

    def __str__(self):
        return json.dumps(
            dataclasses.asdict(self), indent='  ',
            default=lambda x: vars(x) if isinstance(x, Solvable) else str(x),
            ensure_ascii=False
        )


def print_mission_ablauf():
    """Prints the mission sequence."""

    print('Mission Sequence')
    print('1. Ascent Trajectory')
    print('2. Escape from the gravitational field of the departure planet')
    print('3. Transfer to the target planet (Hohmann Transfer)')
    print('4. Enter orbit around the target planet')


def ascent_trajectory_1() -> AscentTrajectory:
    """
    Calculates the ascent trajectory from the departure planet.

    :return: All calculated values.
    """
    return ascent_trajectory()


def transfer_to_target_planet_3(*, departure_planet: Planet, target_planet: Planet) -> HohmannTransfer:
    """
    Calculates the Hohmann transfer (ellipse) from the departure planet to the target planet.

    :param departure_planet: Departure planet.
    :param target_planet: Target planet.
    :return: All calculated values.
    """
    print('3. Transfer to the target planet')
    transfer_to_target_planet_data = HohmannTransfer(central_star=SUN, departure_planet=departure_planet, target_planet=target_planet)
    return transfer_to_target_planet_data


def escape_gravitational_field_2(planet: Planet, hp: Decimal, vinf: Decimal) -> EscapeHyperbola:
    """
    2. Calculates the escape from the gravitational field of the departure planet.
    
    :param planet: Planet to escape from.
    :param hp: Pericenter height above the planet's surface in km.
    :param vinf: Hyperbolic excess velocity at infinity in km/s.
    :return: 
    """
    print(f'2. Escape from the gravitational field of departure {planet}')
    print(f'Calculating escape hyperbola from {planet=}')
    print(f'Pericenter height above the planet's surface {hp=}')
    print(f'Excess velocity delta_v1 (from Hohmann transfer) {vinf=}')
    return escape_hyperbola(planet=planet, hp=hp, vinf=vinf)


def insertion_orbit_target_planet_4(target_planet: Planet, hp: Decimal, vinf: Decimal) -> EscapeHyperbola:
    """
    4. Calculates the orbit insertion around the target planet.

    :param target_planet: Target planet.
    :param hp: Pericenter height above the planet's surface in km.
    :param vinf: Hyperbolic excess velocity; velocity at infinity; here approach velocity in km/s.
    :return: Hyperbola data.
    """
    print(f'4. Orbit insertion around the target planet')
    print(f'{target_planet=}')
    print(f'Pericenter height above the planet surface {hp=}')
    print(f'Approach velocity from Hohmann transfer (va) here as hyperbolic excess velocity {vinf=}')
    return escape_hyperbola(planet=target_planet, hp=hp, vinf=vinf)


def mission(
        *, departure_planet: Planet, target_planet: Planet, departure_planet_orbit_height: Decimal,
        target_planet_orbit_height: Decimal, perform_ascent_trajectory: bool
) -> Mission:
    """
    Calculates a complete mission from the departure planet to the target planet.

    :param departure_planet: Departure planet.
    :param target_planet: Target planet.
    :param departure_planet_orbit_height: The orbit height above the surface of the departure planet.
    :param target_planet_orbit_height: The orbit height above the surface of the target planet.
    :param perform_ascent_trajectory: Indicates whether an ascent trajectory should be performed from the departure planet.
    :return: All calculated values.
    """
    print_mission_sequence()
    print('\n---\n')
    ascent_trajectory_1_data = ascent_trajectory_1() if perform_ascent_trajectory else None
    print('\n---\n')
    transfer_to_target_planet_3_data = transfer_to_target_planet_3(departure_planet=departure_planet, target_planet=target_planet)
    print('\n---\n')
    escape_gravitational_field_2_data = escape_gravitational_field_2(
        planet=departure_planet, hp=departure_planet_orbit_height, vinf=transfer_to_target_planet_3_data.delta_v1
    )
    print('\n---\n')
    insertion_orbit_target_planet_4_data = insertion_orbit_target_planet_4(
        target_planet=target_planet, hp=target_planet_orbit_height, vinf=transfer_to_target_planet_3_data.delta_v2
    )

    return Mission(
        ascent_trajectory_1=ascent_trajectory_1_data,
        transfer_to_target_planet_3=transfer_to_target_planet_3_data,
        escape_gravitational_field_2=escape_gravitational_field_2_data,
        insertion_orbit_target_planet_4=insertion_orbit_target_planet_4_data,
        delta_v_total=UnitDecimal(
            escape_gravitational_field_2_data.v_total.copy_abs()
            + insertion_orbit_target_planet_4_data.v_total.copy_abs(),
            'km/s'
        )
    )


def main():
    print('Vollständige Mission 🚀 - Eingabe der Parameter')
    # Eingabe lesen
    start_planet = planet_from_name(input('Startplanet: '))
    R = start_planet.R
    start_planet_hoehe_umlaufbahn = UnitDecimal(Decimal(
        eval(input('Radius Umlaufbahn bei Startplanet (in km): '))
    ), 'km')
    bahnaufstieg_machen = input('Bahnaufstieg beim Startplaneten machen (True/False)? ').lower() == 'true'
    print(f'{bahnaufstieg_machen=}')
    ziel_planet = planet_from_name(input('Zielplanet: '))
    R = ziel_planet.R
    ziel_planet_hoehe_umlaufbahn = UnitDecimal(Decimal(
        eval(input('Radius Umlaufbahn bei Zielplanet (in km): '))
    ), 'km')
    print('---')
    data = mission(
        start_planet=start_planet, ziel_planet=ziel_planet, start_planet_hoehe_umlaufbahn=start_planet_hoehe_umlaufbahn,
        ziel_planet_hoehe_umlaufbahn=ziel_planet_hoehe_umlaufbahn, bahnaufstieg_machen=bahnaufstieg_machen
    )
    print('Raw data:', data)


if __name__ == '__main__':
    main()
