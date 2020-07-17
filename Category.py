import statistics as stat

class Category:
    ''' basic class to represent a category for classification.'''
    '''I have added some extra functions to this class to make dealing with the'''
    ''' statistics used on this class a bit easier.'''
    def __init__(self, x, y, name = None):
        self.cat_name = name
        self.x = x
        self.y = y
    def __repr__(self):
        '''returns name'''
        return self.cat_name
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
    
    
    
