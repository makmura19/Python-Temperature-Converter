class TemperatureConverter:
    def __init__(self, input_value):
        self.value = input_value
    

    def c_to_f(self):
        return ((9/5)*self.value) + 32
    
    
    def c_to_r(self):
        return (4/5)*self.value
    
    
    def c_to_k(self):
        return self.value + 273.15
    
    
    def f_to_c(self):
        return (self.value - 32) * 5/9
    
    
    def f_to_r(self):
        return (self.value - 32) * 4/9
    
    
    def f_to_k(self):
        return ((self.value - 32) * 5/9) + 273.15
    
    
    def r_to_c(self):
        return (5/4)*self.value
    
    
    def r_to_f(self):
        return ((9/4)*self.value) + 32
    
    
    def r_to_k(self):
        return ((5/4)*self.value) + 273.15
    
    
    def k_to_c(self):
        return self.value - 273.15
    
    
    def k_to_f(self):
        return ((9/5)*(self.value - 273.15)) + 32
    
    
    def k_to_r(self):
        return ((4/5)*self.value) - 273.15