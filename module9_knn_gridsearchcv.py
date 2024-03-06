import numpy as np
from sklearn.metrics import precision_score, recall_score
from sklearn.neighbors import KNeighborsClassifier

class KnnGridSearchCV:
    def __init__(self):
        self.n = 0
        self.train_x = []
        self.train_y = []
        self.m = 0
        self.test_x = []
        self.test_y = []
        self.best_k = 0
        self.best_accuracy = -1
    
    def input_n(self):
        print("Input N")
        self.n = int(input())

    def input_train_xy(self):
        print(f"Input (x,y) for {self.n} times")
        for _ in range(self.n):
            self.train_x.append(input())
            self.train_y.append(input())
        self.train_x = np.array(self.train_x, dtype=float)
        self.train_y = np.array(self.train_y, dtype=int)

    def input_m(self):
        print("Input M")
        self.m = int(input())

    def input_test_xy(self):
        print(f"Input (x,y) for {self.m} times")
        for _ in range(self.m):
            self.test_x.append(input())
            self.test_y.append(input())
        self.test_x = np.array(self.test_x, dtype=float)
        self.test_y = np.array(self.test_y, dtype=int)
    
    def grid_search_cv(self):
        # seach from k=1 to k=10 or k=n
        for i in range(1, min(self.n+1, 11)):
            knn = KNeighborsClassifier(n_neighbors=i)
            knn.fit(self.train_x.reshape(-1, 1), self.train_y)
            y_pred = knn.predict(self.test_x.reshape(-1, 1))
            accuracy = np.mean(y_pred == self.test_y)
            print(f"For k={i}, the accuracy={accuracy}")
            if accuracy > self.best_accuracy:
                self.best_k = i
                self.best_accuracy = accuracy
        print(f"The best k={self.best_k} and the corresponding test accuracy={self.best_accuracy}")
        return
    
if __name__ == '__main__':
    knn_grid_search_cv = KnnGridSearchCV()
    knn_grid_search_cv.input_n()
    knn_grid_search_cv.input_train_xy()
    knn_grid_search_cv.input_m()
    knn_grid_search_cv.input_test_xy()
    knn_grid_search_cv.grid_search_cv()
