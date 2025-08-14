import pytest

from testdata.user_factory import UserFactory


@pytest.fixture
def user_factory():
    return UserFactory()


@pytest.fixture
def user_data(user_factory, request):
    profile = getattr(request, "param", "normal")
    return user_factory.build(profile)
