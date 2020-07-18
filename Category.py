import statistics as stat
from math import fsum

class MachineError(Exception):
    ''' Standard exception of the machine'''
    def __init__(self, stmt):
        self.stmt = stmt
        
class Category:
    ''' basic class to represent a category for classification.'''
    '''I have added some extra functions to this class to make dealing with the'''
    ''' statistics used on this class a bit easier.'''
    def __init__(self, x, y, name = None):
        self.category_name = name
        if len(x) != len(y):
            raise MachineError("ALERT ! : Unequal sample sizes for x and y !") 
        self.x = x
        self.y = y
    def __repr__(self):
        '''returns name'''
        return self.category_name
    def mean_of(self, att):
        ''' returns mean of the specified value'''
        return stat.mean(getattr(self, att.lower()))
    def mode_of(self, att):
        '''returns mode of the specified value'''
        return stat.mode(getattr(self, att.lower()))
    def median_of(self, att):
        '''returns median of the specified value'''
        return stat.median(getattr(self, att.lower()))
    def stdev_of(self, att):
        '''returns standard deviation of the specified value'''
        return stat.stdev(getattr(self, att.lower()))
    def pstdev_of(self, att):
        '''returns population standard deviation of the specified value'''
        return stat.pstdev(getattr(self, att.lower()))
    def variance_of(self, att):
        '''returns variance of the specified value'''
        return stat.variance(getattr(self, att.lower()))
    def pvariance_of(self, att):
        '''return population variance of the specified value'''
        return stat.pvariance(getattr(self, att.lower()))
    def category_formula(self):
        '''returns the categorical field formula'''
        self.factor = self.mean_of('x') if self.variance_of('X') > self.variance_of('y') else self.mean_of('y')
        self.req = 'x' if self.variance_of('X') > self.variance_of('y') else 'y'
        # here, we take the mean of the variable having the highest variance
        # as the mass around which we create the field. Thus, the field can fluctuate
        # based on the value we use for mass, thereby creating a fluctuating decision boundary
        self.z_scores_x = [ (i - self.mean_of('x'))/self.stdev_of('x') for i in self.x]
        self.z_scores_y = [ (j - self.mean_of('y'))/self.stdev_of('y') for j in self.y]
        self.total_zscore = fsum([self.z_scores_x[m] * self.z_scores_y[m] for m in range(len(self.x))])
        self.correl_coeff = self.total_zscore / (len(self.x) - 1) # Pearson's correlation coefficient
        self.categorical_formula = lambda point: (self.correl_coeff * self.factor * point[self.req])/((self.mean_of('x') - point['x'])**2 + (self.mean_of('y') - point['y'])**2)
        return self.categorical_formula
    def update(self, point):
       ''' updates the data in the model with the new data'''
       self.x.append(point['x'])
       self.y.append(point['y'])
        
    
    
