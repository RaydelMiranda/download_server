import pytest

from django.contrib.auth.models import UserManager


@pytest.fixture(scope='session')
def test_user():
    user = UserManager().create_user(
        'test', 'test.pass.123', email='test@test.com'
    )
    return user
