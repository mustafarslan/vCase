import pytest


@pytest.mark.first
@pytest.fixture(scope="module", params=[4518377421351212])
def not_valid_card_number(request):
    return request.param


@pytest.mark.first
@pytest.fixture(scope="module", params=[6011566926687256, 370642420667124, 5417438903761250])
def valid_card_number(request):
    return request.param
