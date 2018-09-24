import pytest

from django.contrib.auth.models import UserManager


@pytest.fixture(scope='session')
def test_user():
    user_manager = UserManager()
    user = user_manager.create_user(
        'test', email='test@test.com', password='test.pass.123'
    )
    return user
