
class FirstQuestion:
    def __init__(self):
        pass

    def run(self, card_number):
        string_card_number = str(card_number)
        result = False
        sum = 0
        stack = []

        for digit in range(len(string_card_number)):
            stack.append(int(string_card_number[digit]))

        check_digit = stack.pop()

        for digit in range(len(stack)):
            if digit % 2 == 0:
                number = stack.pop()
                value = number * 2
                if value > 9:
                    value -= 9
                sum += value
            else:
                number = stack.pop()
                sum += number

        sum += check_digit

        if sum % 10 == 0:
            result = True

        return result
