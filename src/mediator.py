from firstquestion import FirstQuestion
from secondquestion import SecondQuestion
from thirdquestion import ThirdQuestion
from utility import Utility


class Mediator:
    def __init__(self):
        self.first_question = FirstQuestion()
        self.second_question = SecondQuestion()
        self.third_question = ThirdQuestion()
        self.utility = Utility()

    def run_first_question(self, card_number):
        return self.first_question.run(card_number)

    def run_second_question(self, list):
        self.second_question.init(list[0][0])
        graph = self.utility.convert_to_graph(list)
        return self.second_question.run(graph)

    def run_third_question(self, stair_number):
        return self.third_question.run(stair_number)