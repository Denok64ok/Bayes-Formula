import pandas as pd


class WorkDataFrame:
    def __init__(self, dataframe):
        self.dataframe = pd.read_csv(dataframe)
        self.title_parameters = list(self.dataframe.columns)

    def data_len(self):
        return len(self.dataframe.columns)

    def column_list(self, index, selected_class=None):
        dataframe = self.dataframe

        if selected_class:
            dataframe = dataframe[dataframe.quality == selected_class]

        values_parameter = dataframe[self.title_parameters[index]].tolist()

        return values_parameter

    def show_parameter(self, index):
        return self.title_parameters[index]

    def show_classes(self):
        return list(set(self.column_list(self.data_len() - 1)))

    def count_classes(self):
        return len(self.show_classes())
