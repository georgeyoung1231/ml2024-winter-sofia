class DataProcessor:
    def __init__(self):
        self._user_inputs = []
        self._n = 0
        self._x = 0

    def input_n(self):
        print("How many number in the list?")
        self._n = int(input())

    def input_n_list(self):
        print("Input your number and press enter")
        for _ in range(self._n):
            temp = int(input())
            self._user_inputs.append(temp)
    
    def input_x(self):
        print("Input the number you want to check")
        self._x = int(input())

    def output_idx_of_inputs(self):
        for idx,val in enumerate(self._user_inputs):
            if self._x==val:
                print(idx+1)
                return
        print(-1)
        return
