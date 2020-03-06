
def addition(a, b):
    a = int(a)
    b = int(b)
    c = b + a
    return c

def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c

def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = b * a
    return c

def division(a, b):
    a = float(a)
    b = float(b)
    c = b / a
    return c

def square(a):
    a = int(a)
    c = a * a
    return c

def squareroot(a):
    a = int(a)
    c = a ** .5
    return c



class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        self.result = squareroot(a)
        return self.result





