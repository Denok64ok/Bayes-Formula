from numpy import histogram
from Working_DataFrame import WorkDataFrame
from User_Interface import UserInterface


class BayesFormula:
    def __init__(self, dataframe):
        self.dataframe = WorkDataFrame(dataframe)
        self.ui = UserInterface()

        self.len_dataframe = self.dataframe.data_len() - 1

        self.all_classes = self.dataframe.column_list(self.len_dataframe)

        self.unique_classes = self.dataframe.show_classes()
        self.count_unique_classes = self.dataframe.count_classes()

        self.priori_probabilities = []

    def basic_priori_probabilities(self):
        for index in range(0, self.count_unique_classes):
            self.priori_probabilities.append(self.all_classes.count(self.unique_classes[index]) / len(self.all_classes))

    @staticmethod
    def check_accessories(sample, number):
        for i in range(0, len(sample) - 1):
            if sample[i] <= number <= sample[i + 1]:
                return i

    def formulizer(self):

        self.basic_priori_probabilities()

        self.ui.print_probabilities_classes(self.priori_probabilities, self.unique_classes)

        for count in range(0, self.len_dataframe):
            values_parameter = self.dataframe.column_list(count)
            user_feature = self.ui.user_answer(self.dataframe.show_parameter(count), values_parameter)

            cond_density = []

            for index in range(0, self.count_unique_classes):
                values_parameter_class = self.dataframe.column_list(count, self.unique_classes[index])

                density_values, bin_edges = histogram(values_parameter_class, density=True)

                if not (min(bin_edges) <= user_feature <= max(bin_edges)):
                    cond_density.append(self.priori_probabilities[index] * 0)
                else:
                    cond_density.append(
                        self.priori_probabilities[index] * density_values[
                            self.check_accessories(bin_edges, user_feature)])

            for index in range(0, self.count_unique_classes):
                self.priori_probabilities[index] = cond_density[index] / sum(cond_density)

            self.ui.print_probabilities_classes(self.priori_probabilities, self.unique_classes)

        self.ui.print_result(self.unique_classes, self.priori_probabilities)
