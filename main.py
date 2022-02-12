from src.mediator import Mediator


class vCase:

    def __init__(self):
        self.mediator = Mediator()

    def validate_credit_card_number(self, card_number):
        return self.mediator.run_first_question(card_number)

    def schedule_courses(self, list):
        return self.mediator.run_second_question(list)

    def distinct_way_stair_case(self, stair_number):
        return self.mediator.run_third_question(stair_number)


if __name__ == "__main__":
    case = vCase()
    print("Question 1: Credit Card Number Checker =>  Input: {0}, Result: {1}, Expected: {2}".format(6011566926687256, case.validate_credit_card_number(6011566926687256), True))
    print("Question 1: Credit Card Number Checker =>  Input: {0}, Result: {1}, Expected: {2}".format(370642420667124, case.validate_credit_card_number(370642420667124), True))
    print("Question 1: Credit Card Number Checker =>  Input: {0}, Result: {1}, Expected: {2}".format(5417438903761250, case.validate_credit_card_number(5417438903761250), True))
    print("Question 1: Credit Card Number Checker =>  Input: {0}, Result: {1}, Expected: {2}".format(4518377421351212, case.validate_credit_card_number(4518377421351212), False))
    print("Question 2: Course Schedule =>  Input: {0}, Result: {1}, Expected: {2}".format([[4], [1,0], [2, 0], [3,1,2]], case.schedule_courses([[4], [1,0], [2, 0], [3,1,2]]), [0, 1, 2, 3]))
    print("Question 2: Course Schedule =>  Input: {0}, Result: {1}, Expected: {2}".format([[7], [0, 1, 2], [1, 3], [2, 3], [3, 4, 5], [4, 6], [5, 6]], case.schedule_courses([[7], [0, 1, 2], [1, 3], [2, 3], [3, 4, 5], [4, 6], [5, 6]]), [6, 4, 5, 3, 1, 2, 0]))
    print("Question 2: Course Schedule =>  Input: {0}, Result: {1}, Expected: {2}".format([[8], [4, 0, 2], [0, 1, 6], [2, 3, 7], [1, 5], [6, 5], [3, 5], [7, 5]], case.schedule_courses([[8], [4, 0, 2], [0, 1, 6], [2, 3, 7], [1, 5], [6, 5], [3, 5], [7, 5]]), [5, 1, 6, 3, 7, 0, 2, 4]))
    print("Question 2: Course Schedule =>  Input: {0}, Result: {1}, Expected: {2}".format([[4], [2, 1, 3]], case.schedule_courses([[4], [2, 1, 3]]), [0, 1, 3, 2]))
    print("Question 3: Climbing Stair Case =>  Input: {0}, Result: {1}, Expected: {2}".format(10, case.distinct_way_stair_case(10), 89))
    print("Question 3: Climbing Stair Case =>  Input: {0}, Result: {1}, Expected: {2}".format(20, case.distinct_way_stair_case(20), 10946))


