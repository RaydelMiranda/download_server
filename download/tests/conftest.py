import pytest
from django.contrib.auth import get_user_model


@pytest.fixture(scope='function')
def test_user():

    user_model = get_user_model()

    user = user_model.objects.create_user(
        'test', email='test@test.com', password='test.pass.123'
    )

    return user
