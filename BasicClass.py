'''
Created on 11-Mar-2014

@author: akm
'''

class BasicClass:
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name;
        
        
    def show(self):
        print 'Basic --name  %s' %self.name;

class Special(BasicClass):
    def __init__(self,name,edible):
        BasicClass.__init__(self, name);
        self.upper = name.upper();
        self.edible= edible;
    def show(self):
        BasicClass.show(self);
        print 'Special --upper name %s' %self.upper;
        if self.edible:
            print "it's edible";
        else:
            print "it's not edible";
    def edible(self):
        return self.edible;
        
         
            
                               
def test():
    obj1 = BasicClass('Ajay');
    obj1.show();
    print '='*30;
    obj2 = Special('vijay',12);
    obj2.show();
test();   