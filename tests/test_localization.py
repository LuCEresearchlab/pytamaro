from pytamaro.localization import translate


def test_missing_key():
    assert translate("xxx") == "xxx"


def test_with_params():
    msg = translate("INVALID_TYPE", "p", "t1", "t2")
    assert "p" in msg
    assert "t1" in msg
    assert "t2" in msg


def test_localized_params():
    import sys
    sys.modules["pytamaro"].LANGUAGE = "it"   # type: ignore
    msg = translate("INVALID_TYPE", translate("graphic"), translate("Graphic"), translate("Point"))
    assert "grafica" in msg
    assert "Grafica" in msg
    assert "Punto" in msg
