from Working_DataFrame import WorkDataFrame


class UserInterface:
    def __init__(self, dataframe):
        self.dataframe = WorkDataFrame(dataframe)

    def user_answer(self, count):
        values_parameter = self.dataframe.column_list(count)
        return float(input(
            f"\nКак вы думаете каков у вашего вина, "
            f"{self.dataframe.show_parameter(count)} ({min(values_parameter)}-{max(values_parameter)}):"))

    @staticmethod
    def print_probabilities_classes(probability, category):
        for i in range(0, len(category)):
            print(f"С вероятностью {probability[i]:.2f}, что качество вина равно: {category[i]}")

    @staticmethod
    def print_result(classes, probabilities):
        print(f"\nВероятнее всего ваше вино {classes[probabilities.index(max(probabilities))]} качества")
