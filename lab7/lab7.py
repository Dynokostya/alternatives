import numpy as np
import matplotlib.pyplot as plt


class Probability:
    def __init__(self, error: int, n: int, m: int, rand_range: tuple):
        self.error = error
        self.n = n
        self.m = m
        self.rand_range = rand_range
        self.success_experiments = np.zeros(self.n, dtype=int)

    def __find_success_experiments(self):
        for i in range(1, self.n):
            for j in range(self.m):
                values = np.random.randint(self.rand_range[0], self.rand_range[1] + 1, self.n)
                x_max = np.max(values[:i])
                for k in values[i:]:
                    if k > x_max:
                        diff = np.abs(k - np.max(values)) / np.max(values) * 100
                        if diff <= self.error:
                            self.success_experiments[i] += 1
                        break

    def calculate_probabilities(self):
        self.__find_success_experiments()
        self.success_experiments = self.success_experiments / self.m
        return np.max(self.success_experiments), np.argmax(self.success_experiments)


def plot_graphs():
    errors = [0, 2, 4, 6, 8, 10]
    n = 100
    m = 1000
    rand_range = (0, 100)
    probabilities = [0 for _ in range(len(errors))]
    optimal = [0 for _ in range(len(errors))]
    for i in range(len(errors)):
        prob = Probability(errors[i], n, m, rand_range)
        probabilities[i], optimal[i] = prob.calculate_probabilities()
        print(f'Error: {errors[i]}%, Probability: {probabilities[i]}')
        window_size = 15
        smoothed_values = np.convolve(prob.success_experiments, np.ones(window_size)/window_size, mode='valid')
        smoothed_x = np.arange(window_size // 2, n - window_size // 2, 1)
        plt.scatter(np.arange(0, n, 1), prob.success_experiments, color='black', marker='.', alpha=0.5)
        plt.plot(smoothed_x, smoothed_values, color='black')
        plt.title(f'Error = {errors[i]}%')
        plt.ylabel('P(t)')
        plt.xlabel('t')
        plt.grid()
        plt.show()

    plt.plot(errors, probabilities, color='black')
    plt.ylabel('delta P')
    plt.xlabel('Errors, %')
    plt.grid()
    plt.show()

    plt.plot(errors, optimal, color='black')
    plt.ylabel('t')
    plt.xlabel('Errors, %')
    plt.grid()
    plt.show()


def main():
    plot_graphs()


main()
