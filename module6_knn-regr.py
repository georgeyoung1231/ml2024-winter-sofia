import numpy as np

class KNNRegressor:
    def __init__(self):
        self.k = 0
        self.n = 0
        self.x = []
        self.y = []
        self.to_pred_x = 0

    def input_n(self):
        print("Input N")
        self.n = int(input())

    def input_k(self):
        print("Input k")
        self.k = int(input())
    
    def input_xy(self):
        print(f"Input (x,y) for {self.n} times")
        for _ in range(self.n):
            self.x.append(float(input()))
            self.y.append(float(input()))
    
    def input_to_pred_x(self):
        print("Input X to predict")
        self.to_pred_x = float(input())

    def predict(self):
        if self.k > self.n or self.k <= 0:
            print(f"k should be less than or equal to {self.n} and > 0")
            return
        # calculate distance from to_pred_x to each x
        distances = []
        for i in range(self.n):
            distances.append(abs(self.to_pred_x - self.x[i]))
        # sort the distances
        sorted_indices = np.argsort(distances)
        # get the k nearest neighbors
        k_nearest_y = []
        for i in range(self.k):
            k_nearest_y.append(self.y[sorted_indices[i]])
        # calculate the average of k_nearest_y
        print(f"The result(Y)={np.mean(k_nearest_y)}")
        return

        
if __name__ == "__main__":
    knn = KNNRegressor()
    knn.input_n()
    knn.input_k()
    knn.input_xy()
    knn.input_to_pred_x()
    knn.predict()
