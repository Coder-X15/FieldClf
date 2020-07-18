from Category import *

class Category_Field_Machine:
    ''' Categorical Field Machine'''
    def __init__(self, category_a, category_b):
        ''' initialiser'''
        self.category_a = Category(list(i[0] for i in category_a[list(category_a.keys())[0]]),list(j[1] for j in category_a[list(category_a.keys())[0]]), list(category_a.keys())[0])
        self.category_b = Category(list(i[0] for i in category_b[list(category_b.keys())[0]]),list(j[1] for j in category_b[list(category_b.keys())[0]]), list(category_b.keys())[0])
        self.category_a_formula = self.category_a.category_formula()
        self.category_b_formula = self.category_b.category_formula()
    def predict(self, point):
        '''predicts the class to which the point belongs'''
        val_a = self.category_a_formula(point)
        val_b = self.category_b_formula(point)
        if val_a > val_b:
            return str(self.category_a)
        elif val_b > val_a:
            return str(self.category_b)
        else:
            return 'Confused....'
    def train(self, point, actual_class):
        ''' trains the model'''
        if str(self.category_a).lower() == actual_class.lower():
            self.category_a.update(point)
            self.category_a_formula = self.category_a.category_formula()
        elif str(self.category_b).lower() == actual_class.lower():
            self.category_b.update(point)
            self.category_b_formula = self.category_b.category_formula()
            
        
        
