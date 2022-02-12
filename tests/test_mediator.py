import pytest
from src.mediator import Mediator


class TestMediator:
    @pytest.fixture
    def mediator_object(self):
        return Mediator()

    @pytest.mark.parametrize("param1, param2",
                             [
                                 (4518377421351212, False),
                                 (370642420667124, True),
                                 (6011566926687256, True),
                                 (5417438903761250, True)
                             ],)
    def test_run_first_question(self, mediator_object, param1, param2):
        assert mediator_object.run_first_question(param1) == param2

    @pytest.mark.parametrize("param1, param2",
                             [
                                 ([[4], [1, 0], [2, 0], [3, 1, 2]], [0, 1, 2, 3]),
                                 ([[7], [0, 1, 2], [1, 3], [2, 3], [3, 4, 5], [4, 6], [5, 6]], [6, 4, 5, 3, 1, 2, 0]),
                                 ([[8], [4, 0, 2], [0, 1, 6], [2, 3, 7], [1, 5], [6, 5], [3, 5], [7, 5]],
                                  [5, 1, 6, 3, 7, 0, 2, 4]),
                                 ([[4], [2, 1, 3]], [0, 1, 3, 2])
                             ],)
    def test_run_second_question(self, mediator_object, param1, param2):
        assert mediator_object.run_second_question(param1) == param2

    @pytest.mark.parametrize("param1, param2",
                             [
                                 (10, 89),
                                 (20, 10946)
                             ],)
    def test_run_third_question(self, mediator_object, param1, param2):
        assert mediator_object.run_third_question(param1) == param2
