import pandas as pd
import matplotlib.pyplot as plt


class Data:
    def __init__(self, file_name: str):
        self.data = pd.read_excel(file_name)
        self.data = self.data.apply(pd.to_numeric, errors='coerce')
        self.df = self.data.copy()
        self.minimums = None
        self.maximums = None
        self.means = None
        self.stds = None
        self.fill_null()
        self.standardize()
        self.normalize()

    def fill_null(self, method='means'):
        if method == 'means':
            self.df = self.df.fillna(self.df.mean())

    def standardize(self):
        self.means = self.df.mean()
        self.stds = self.df.std()
        self.df = (self.df - self.means) / self.stds

    def normalize(self):
        self.minimums = self.df.min()
        self.maximums = self.df.max()
        self.df = ((self.df - self.minimums) / (self.maximums - self.minimums))


def task():
    work_data = Data("DATA_КП_1.xls")
    std_deviation = work_data.df.std()

    print(std_deviation)
    plt.figure(figsize=(10, 8))
    plt.xlabel('Показники')
    plt.ylabel('Стандартне відхилення')
    std_deviation.plot(kind='bar', color='gray')
    plt.xticks(rotation=45)
    plt.show()


task()
