import caesar


def test_encrypt_ahoj():
    assert caesar.encrypt("ahoj", 1) == "bipk"


def test_encrypt_ahoj_02():
    assert caesar.encrypt("ahoj", 13) == "nubw"


def test_encrypt_ahoj_03():
    assert caesar.encrypt("ahoj blazne cos cekal?", 13) == "nubw oynmar pbf prxny?"
