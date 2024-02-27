import numpy as np
from sklearn.metrics import precision_score, recall_score

class Metrics:
    def __init__(self):
        self.n = 0
        self.x = []
        self.y = []

    def input_n(self):
        print("Input N")
        self.n = int(input())

    def input_xy(self):
        print(f"Input (x,y) for {self.n} times")
        for _ in range(self.n):
            self.x.append(input())
            self.y.append(input())
        self.x = np.array(self.x, dtype=int)
        self.y = np.array(self.y, dtype=int)
    
    def calculate_precision(self):
        precision = precision_score(self.x, self.y)
        print(f"The precision={precision}")
        return
    
    def calculate_recall(self):
        recall = recall_score(self.x, self.y)
        print(f"The recall={recall}")
        return

if __name__ == "__main__":
    metrics = Metrics()
    metrics.input_n()
    metrics.input_xy()
    metrics.calculate_precision()
    metrics.calculate_recall()
