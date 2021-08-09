# ! Imports nicht optimieren bzw. welche rauslöschen, um in main() via eval() darauf Zugriff zu haben !
from bahnen.transfer_ellipse import TransferEllipse, vk
from lib.helper import merge_param_funcs
from lib.planet import *
from lib.unit_decimal import UnitDecimal


class HohmannTransfer(TransferEllipse):
    param_funcs: dict = merge_param_funcs({
        "vk_ziel": [lambda ra, zentralgestirn: vk(zentralgestirn=zentralgestirn, radius=ra)],
        "ra": [lambda ziel_planet: ziel_planet.a],
        "delta_v2": [lambda va, vk_ziel: UnitDecimal(vk_ziel - va, 'km/s')]
    }, TransferEllipse.param_funcs)

    def __init__(self, **kwargs):
        super().__init__(**kwargs, phi_ankunft=UnitDecimal('180', '°'))


# def hohmann(*, zentralgestirn: Planet, rp: Decimal, ra: Decimal) -> HohmannTransfer:
#     """
#     Berechnet einen Hohmann-Transfer.

#     :param zentralgestirn: Gestirn als Brennpunkt der Übergangsellipse.
#     :param rp: Radius des Perizentrums.
#     :param ra: Radius des Apozentrums.
#     :return: Sämtliche berechneten Werte.
#     """
#     print('Hohmann Transfer 🚀')
#     print(f'{zentralgestirn=}')

#     rp = UnitDecimal(rp, 'km')
#     ra = UnitDecimal(ra, 'km')
#     print(f'Radius Perizentrum {rp=}')
#     print(f'Radius Apozentrum {ra=}')
#     print()

#     print('Berechne allgemeine Parameter der Übergangsellipse:')
#     epsilon = allgemein.numerische_exzentrizitaet_ra_rp(rp=rp, ra=ra)
#     print(f'Numerische Exzentrizität {epsilon=}')
#     p = ellipse.bahnparameter_p(rp=ra, epsilon=epsilon)
#     print(f'Bahnparameter {p=}')
#     a = ellipse.grosse_halbachse_ra_rp(rp=rp, ra=ra)
#     print(f'Große Halbachse {a=}')
#     e = ellipse.lineare_exzentrizitaet(a=a, rp=rp)
#     print(f'Lineare Exzentrizität {e=}')
#     print()

#     vp = ellipse.perizentrum_geschwindigkeit_rp_ra(planet=zentralgestirn, ra=ra, rp=rp)
#     print(f'Benötigte Geschwindigkeit Perizentrum {vp=}')
#     vk_start = kreis.geschwindigkeit(planet=zentralgestirn, rk=rp)
#     print(f'Bereits vorhandene Kreisbahngeschwindigkeit bei Perizentrum {rp=}: {vk_start=}')
#     delta_v1 = UnitDecimal(vp - vk_start, 'km/s')
#     print(f'Schubimpuls Geschwindigkeitsdelta Δv1 = vp - vk_start = {delta_v1}')
#     print()

#     va = ellipse.apozentrum_geschwindigkeit(planet=zentralgestirn, ra=ra, epsilon=epsilon, p=p)
#     print(f'Benötigte Geschwindigkeit Apozentrum {va=}')
#     vk_ziel = kreis.geschwindigkeit(planet=zentralgestirn, rk=ra)
#     print(f'Kreisbahngeschwindigkeit bei Apozentrum {ra=}: {vk_ziel=}')
#     delta_v2 = UnitDecimal(vk_ziel - va, 'km/s')
#     print(f'Schubimpuls Geschwindigkeitsdelta Δv2 = vk_ziel - va = {delta_v2}')
#     print()

#     v_total = UnitDecimal(abs(delta_v1) + abs(delta_v2), 'km/s')
#     print(f'Benötigter Gesamt-Schubimpuls {v_total=}')
#     tu = ellipse.umlaufzeit(planet=zentralgestirn, a=a)
#     flugdauer = 0.5 * tu
#     print(f'Flugdauer (Halbe Umlaufzeit der Ellipse): {flugdauer} bzw. {flugdauer.total_seconds()} Sekunden')

#     return HohmannTransfer(
#         ra=ra, rp=rp, epsilon=epsilon, p=p, a=a, e=e, vp=vp, vk_start=vk_start, delta_v1=delta_v1, va=va,
#         vk_ziel=vk_ziel, delta_v2=delta_v2, v_total=v_total, flugdauer=flugdauer
#     )


def main():
    """
    Liest die für den Hohmann-Transfer benötigten Parameter von stdin. Dabei werden die Eingaben mittels eval()
    ausgewertet. Daher kann auf Konstanten
    :return:
    """
    # print('Hohmann Transfer 🚀 - Eingabe der Parameter')
    # # Eingabe lesen. eval() führt Eingabe als Programmcode aus. Daher ist es möglich
    # planet = planet_from_name(input('Planet: '))
    # R = planet.R
    # perizentrum_hoehe = eval(input('Perizentrum Höhe über Planet (in km): '))
    # apozentrum_hoehe = eval(input('Apozentrum Höhe über Planet (in km): '))
    # print('---')
    # data = hohmann(zentralgestirn=planet, perizentrum_hoehe=perizentrum_hoehe, apozentrum_hoehe=apozentrum_hoehe)
    # data_json = json.dumps(dataclasses.asdict(data), indent='  ', default=lambda x: str(x), ensure_ascii=False)
    # print()
    # print('Raw data:')
    # print(data_json)


if __name__ == '__main__':
    main()
