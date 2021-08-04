from decimal import Decimal

from bahnen.ellipse import Ellipse
from lib.planet import Planet
from datetime import timedelta, datetime
from lib.planet import planet_from_name
from lib.unit_decimal import UnitDecimal


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
    """Delta Zeit bis zum ersten Erreichen der Startkonstellation nach dem Referenzzeitpunkt."""
    startzeit_periode: timedelta
    """Dauer nach einem Startzeitpunkt, bis zum Auftreten des nächsten."""

    def startzeitpunkt_nach_index(self, n: int) -> datetime:
        """Berechnet den n-te Startzeitpunkt der nach dem Referenzdatum.

        Args:
            n (int): Index der Konstellation.

        Returns:
            datetime: Zeitpunkt der Konstellation.
        """
        erster_startzeitpunkt = self.start_planet.L0_DATETIME + self.delta_t
        return erster_startzeitpunkt + n * self.periode

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


def transfer_ellipse() -> TransferEllipse:
    """
    Berechnet die Transferellipse vom Start- zum Zielplaneten.

    :return: Transferellipsesinstanz.
    """
    # TODO
    return TransferEllipse()


def main():
    print('Transferellipse 🌍 🚀 🪐 - Eingabe der Parameter')

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


if __name__ == '__main__':
    main()
