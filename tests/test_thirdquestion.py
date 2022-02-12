import pytest
from src.thirdquestion import ThirdQuestion


@pytest.mark.third
class TestThirdQuestion:
    @pytest.fixture
    def third_question_object(self):
        return ThirdQuestion()

    @pytest.mark.parametrize("param1, param2",
                             [
                                 (10, 89),
                                 (20, 10946)
                             ],)
    def test_run_climb_stairs(self, third_question_object, param1, param2):
        assert third_question_object.run(param1) == param2
