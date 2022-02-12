import pytest
from src.firstquestion import FirstQuestion


@pytest.mark.first
@pytest.mark.usefixtures("not_valid_card_number", "valid_card_number")
class TestFirstQuestion:
    @pytest.fixture
    def first_question_object(self):
        return FirstQuestion()

    def test_run_valid(self, first_question_object, valid_card_number):
        assert first_question_object.run(valid_card_number)

    def test_run_not_valid(self, first_question_object, not_valid_card_number):
        assert not first_question_object.run(not_valid_card_number)