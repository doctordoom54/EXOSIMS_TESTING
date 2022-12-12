# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 23:16:05 2022

@author: sachin kelkar
"""

class test(object):
    
   
    
    def __init__(self,a,b):
        
        self.a = a
        self.b = b
        
    def add(self,c,d):
        e = self.a+self.b
        return e
    


class test2(test):
    
    def __init__(self,f,a,b):
        test.__init__(self,a,b)
        self.f = f
        
    def addin(self):
        u = self.f+self.b
        return u


y = test2(1,1,2)
y.addin()
