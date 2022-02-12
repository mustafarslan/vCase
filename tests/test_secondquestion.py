import pytest
from src.secondquestion import SecondQuestion
from src.utility import Utility


class TestSecondQuestion:
    @pytest.fixture
    def second_question_object(self):
        return SecondQuestion()

    @pytest.fixture
    def utility(self):
        return Utility()

    @pytest.mark.parametrize("param1, param2",
                             [
                                 ([[4], [1,0], [2, 0], [3,1,2]], [0, 1, 2, 3]),
                                 ([[7], [0, 1, 2], [1, 3], [2, 3], [3, 4, 5], [4, 6], [5, 6]], [6, 4, 5, 3, 1, 2, 0]),
                                 ([[8], [4, 0, 2], [0, 1, 6], [2, 3, 7], [1, 5], [6, 5], [3, 5], [7, 5]], [5, 1, 6, 3, 7, 0, 2, 4]),
                                 ([[4], [2, 1, 3]], [0, 1, 3, 2])
                             ],)
    def test_run_schedules(self, second_question_object,param1, param2, utility):
        second_question_object.init(param1[0][0])
        graph = utility.convert_to_graph(param1)
        assert second_question_object.run(graph) == param2
