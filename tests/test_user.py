import pytest

from app.models import User


def test_assert_password_not_accessable():
    user = User('test', 'test')
    with pytest.raises(AttributeError):
        user.password


def test_password_hashed():
    user = User('test', 'password')
    assert not user.password_hash == 'password'
    assert len(user.password_hash) > 8


def test_login():
    user = User('test', 'password')
    assert not user.validate('asdjasdaad')
    assert not user.validate('passwor')
    assert user.validate('password')

