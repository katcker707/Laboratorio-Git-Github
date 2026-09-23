from challenge_tools import average_score


def test_r08_calcula_media_no_entera():
    puntuaciones = [10, 15]

    resultado = average_score(puntuaciones)

    assert resultado == 12.5
    assert puntuaciones == [10, 15]


def test_r08_un_elemento_devuelve_el_mismo_valor():
    assert average_score([7]) == 7.0