from lib.kingdom import Kingdom


def test_should_encrypt_emblem():
    air = Kingdom('AIR', 'OWL')
    assert air.encrypted_emblem() == 'rzo'


def test_should_return_true_if_ally():
    air = Kingdom('AIR', 'OWL')

    assert air.is_ally('ROZO')


def test_should_return_true_if_message_contains_emblem():
    air = Kingdom('AIR', 'OWL')

    assert air.contains_emblem('ROZO')
