from challenge_tools import unique_tags


def test_r07_distingue_mayusculas_y_conserva_orden():
    etiquetas = ["api", "API", "web", "api", "Web", "API"]
    esperado = ["api", "API", "web", "Web"]

    resultado = unique_tags(etiquetas)

    assert resultado == esperado
    assert etiquetas == ["api", "API", "web", "api", "Web", "API"]