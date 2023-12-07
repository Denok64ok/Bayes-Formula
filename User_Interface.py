from Working_DataFrame import WorkDataFrame


class UserInterface:
    @staticmethod
    def user_answer(parameter, values):
        return float(input(
            f"\nКак вы думаете каков у вашего вина, "
            f"{parameter} ({min(values)}-{max(values)}):"))

    @staticmethod
    def print_probabilities_classes(probability, category):
        for i in range(0, len(category)):
            print(f"С вероятностью {probability[i]:.2f}, что качество вина равно: {category[i]}")

    @staticmethod
    def print_result(classes, probabilities):
        print(f"\nВероятнее всего ваше вино {classes[probabilities.index(max(probabilities))]} качества")
