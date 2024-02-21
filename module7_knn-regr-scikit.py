import numpy as np
from sklearn.neighbors import KNeighborsRegressor

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
        
        regressor = KNeighborsRegressor(n_neighbors=self.k)
        regressor.fit(np.array(self.x).reshape(-1, 1), self.y)
        k_nearest_y = regressor.predict(np.array(self.to_pred_x).reshape(-1, 1))
        coefficient_of_determination = regressor.score(np.array(self.x).reshape(-1, 1), self.y)
        print(f"The result(Y)={k_nearest_y[0]}")
        print(f"The coefficient of determination={coefficient_of_determination}")
        return

        
if __name__ == "__main__":
    knn = KNNRegressor()
    knn.input_n()
    knn.input_k()
    knn.input_xy()
    knn.input_to_pred_x()
    knn.predict()
