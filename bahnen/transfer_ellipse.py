from decimal import Decimal

from bahnen.ellipse import Ellipse
from lib.planet import Planet
from datetime import timedelta, datetime
from lib.planet import planet_from_name
from lib.unit_decimal import UnitDecimal, return_unit
from lib.helper import jahre_zu_timedelta, merge_param_funcs, timedelta_zu_jahre
import math


@return_unit("rad")
def phi_ankunft(*, epsilon: Decimal, a: Decimal, ziel_planet: Planet) -> Decimal:
    """Berechnet die Winkelposition, zu der der Zielplanet erreicht wird.

    Args:
        epsilon (Decimal): Numerische Exzentrizität.
        a (Decimal): Große Halbachse in km.
        ziel_planet (Planet): Zielplanet.

    Returns:
        Decimal: Ankunftswinkelposition in rad.
    """
    return Decimal(math.acos(1 / epsilon * ((a * (1 - epsilon**2) / ziel_planet.a) - 1)))


def transfer_dauer(*, zentralgestirn: Planet, a: Decimal, epsilon: Decimal, phi_ankunft: Decimal) -> timedelta:
    """Berechnet die Transferdauer einer (schnellen) Übergangsellipse.

    Args:
        zentralgestirn (Planet): Zentralgestirn um den die Bahn liegt.
        a (Decimal): Große Halbachse in km.
        epsilon (Decimal): Numerische Exzentrizität.
        phi_ankunft (Decimal): Ankunftswinkel in rad.

    Returns:
        timedelta: Dauer des Transfers.
    """
    return timedelta(
        seconds=float(Decimal(
            math.sqrt(a**3 / zentralgestirn.mu)
        ) * (
            Decimal(2) * Decimal(
                math.atan(Decimal(
                    math.sqrt(
                        (1 - epsilon)/(1 + epsilon)
                    )) * Decimal(
                        math.tan(phi_ankunft/2)
                    )
                )
            ) - (
                epsilon * Decimal(
                    math.sqrt(1 - epsilon**2)
                ) * Decimal(
                    math.sin(phi_ankunft)
                )/(
                    1 + epsilon * Decimal(
                        math.cos(phi_ankunft)
                    )
                )
            )
        ))
    )


@return_unit("km/s")
def vk(*, zentralgestirn: Planet, radius: Decimal) -> Decimal:
    """Kreisbahngeschwindigkeit um den Planeten mit entsprechendem Radius.

    Args:
        planet (Planet): Planet der umkreist wird.
        radius (Decimal): Radius mit Planetenradius in km.

    Returns:
        Decimal: Geschwindigkeit in km/s.
    """
    return Decimal(math.sqrt(zentralgestirn.mu/radius))


@return_unit("rad")
def psi(*, phi_ankunft: Decimal, transfer_dauer: timedelta, ziel_planet: Planet) -> Decimal:
    """Winkeldelta welches zwischen Start- und Zielplanet zum Startzeitpunkt herrschen muss, damit man beim Zielplaneten ankommt.

    Args:
        phi_ankunft (Decimal): Ankunftswinkel in rad.
        transfer_dauer (timedelta): Transferdauer als timedelta.
        ziel_planet (Planet): Zielplanet.

    Returns:
        Decimal: Psi in rad.
    """
    return phi_ankunft - timedelta_zu_jahre(transfer_dauer) * 2 * Decimal(math.pi) / ziel_planet.T


@return_unit("a")
def synodische_periode(*, start_planet: Planet, ziel_planet: Planet) -> Decimal:
    """Synodische Periode zwischen den gegebenen Planeten.

    Args:
        start_planet (Planet): Startplanet.
        ziel_planet (Planet): Zielplanet.

    Returns:
        timedelta: Dauer der synodischen Periode.
    """
    return 1/((1/start_planet.T) - (1/ziel_planet.T))


@return_unit("a")
def delta_t(*, psi: Decimal, start_planet: Planet, ziel_planet: Planet) -> Decimal:
    """Das Delta an Zeit bis zum Eintreten des ersten Startzeitpunkts nach dem Referenzdatum der Planeten.

    Args:
        psi (Decimal): Psi in rad.
        start_planet (Planet): Startplanet.
        ziel_planet (Planet): Zielplanet.

    Returns:
        Decimal: Delta-t in Jahren.
    """
    return (psi + start_planet.L0 - ziel_planet.L0)/(2 * Decimal(math.pi) * ((1/ziel_planet.T) - (1/start_planet.T)))


class TransferEllipse(Ellipse):
    start_planet: Planet
    """Planet, von dem aus man starten möchte."""
    ziel_planet: Planet
    """Planet, den man erreichen möchte."""

    vk_start: UnitDecimal
    """Geschwindigkeit auf Kreisbahn um Startplaneten."""
    vk_ziel: UnitDecimal
    """Geschwindigkeit auf Kreisbahn um Zielplaneten."""

    delta_v1: UnitDecimal
    """Geschwindigkeitsdelta/Schubimpuls Nr.1 in km/s."""
    delta_v2: UnitDecimal
    """Geschwindigkeitsdelta/Schubimpuls Nr.2 in km/s."""
    v_total: UnitDecimal
    """Insgesamt benötigter Geschwindigkeitsimpuls in km/s."""

    phi_ankunft: UnitDecimal
    """Bei welchem Winkel man auf den Zielplaneten trifft."""
    transfer_dauer: timedelta
    """Dauer des Transfers vom Start- zum Zielplanet."""
    psi: UnitDecimal
    """Benötigte Konstellation der Planeten zueinander zum Starten. Genauer: Winkel von Start- zu Zielplanet."""
    delta_t: UnitDecimal
    """Delta Zeit bis zum ersten Erreichen der Startkonstellation nach dem Referenzzeitpunkt in Jahren."""
    synodische_periode: UnitDecimal
    """Dauer nach einem Startzeitpunkt, bis zum Auftreten des nächsten in Jahren."""

    param_funcs: dict = merge_param_funcs({
        "start_planet": [],
        "ziel_planet": [],
        "vk_start": [lambda start_planet, zentralgestirn: vk(zentralgestirn=zentralgestirn, radius=start_planet.a)],
        "vk_ziel": [lambda ziel_planet, zentralgestirn: vk(zentralgestirn=zentralgestirn, radius=ziel_planet.a)],
        "delta_v1": [lambda vp, vk_start: UnitDecimal(vp - vk_start, "km/s")],
        "delta_v2": [],
        "v_total": [lambda delta_v1, delta_v2: UnitDecimal(delta_v1.copy_abs() + delta_v2.copy_abs(), "km/s")],
        "phi_ankunft": [phi_ankunft],
        "transfer_dauer": [transfer_dauer],
        "psi": [psi],
        "delta_t": [delta_t],
        "synodische_periode": [synodische_periode],
        "rp": [lambda start_planet: start_planet.a]
    }, Ellipse.param_funcs)

    def startzeitpunkt_nach_index(self, n: int) -> datetime:
        """Berechnet den n-te Startzeitpunkt der nach dem Referenzdatum.

        Args:
            n (int): Index der Konstellation.

        Returns:
            datetime: Zeitpunkt der Konstellation.
        """
        erster_startzeitpunkt = self.start_planet.L0_DATETIME + \
            jahre_zu_timedelta(self.delta_t)
        return erster_startzeitpunkt + n * jahre_zu_timedelta(self.synodische_periode)

    def startzeitpunkt_um_datum(self, datum: datetime) -> tuple:
        """Berechnet den am nächsten liegenden Startzeitpunkt zum gegebenen Datum.

        Args:
            datum (datetime): Gewünschter Startzeitpunkt

        Returns:
            tuple: Tupel bestehend aus datetimes: (Startzeitpunkt früher oder am gleichen Tag, Startzeitpunkt später)
        """
        n_kleinste_obere_schranke: int = 0
        schritt: int = 1

        # Wenn datum kleiner als Referenzdatum, dann müssen wir rückwärts gehen
        if self.startzeitpunkt_nach_index(0) > datum:
            schritt = -1

        while not self.startzeitpunkt_nach_index(n_kleinste_obere_schranke) > datum >= self.startzeitpunkt_nach_index(n_kleinste_obere_schranke - 1):
            n_kleinste_obere_schranke += schritt

        return (self.startzeitpunkt_nach_index(n_kleinste_obere_schranke - 1),
                self.startzeitpunkt_nach_index(n_kleinste_obere_schranke))
