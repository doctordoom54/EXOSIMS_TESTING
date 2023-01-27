class test(object):
    def __init__(self,a,b):
        
        self.a = a
        self.b = b
        
    def add(self,c,d):
        e = self.a+self.b
        g =self.c*self.d
        return e,g
    
class test2(test):
    
    def __init__(self,f,a,b):
        test.__init__(self,a,b)
        self.f = f
        
    def addin(self):
        u = self.f+self.b
        return u

y = test2(1,1,2)
y.addin()
