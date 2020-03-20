'''
Created on Mar 19, 2020

@author: marbe
'''

def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Substract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def devide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')    
    return x / y
