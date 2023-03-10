import numpy as np

# Open a csv file with numpy


class LinearRegression:
    def __init__(self, data):
        self.filename = data
        self.data = np.genfromtxt(self.filename, delimiter=',', skip_header=1)
        self.get_useful_data()
        
    
    def get_useful_data(self):
        data = self.data
        print(data[0])
        
        
        
        
    
    
        

        


ln = LinearRegression('kc_house_data.csv')
