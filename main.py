class Calculator:
    def __init__(self):
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }
        
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        return x / y if y != 0 else 'Error: Division by zero'
    
## Test case

if __name__ == '__main__':
    calculator = Calculator()
    ## Let add two numbers
    x, y = 10, 12
    print(f"The addition of {x} + {y} = {calculator.add(x, y)}")
    print(f"The subtraction of {x} - {y} = {calculator.subtract(x, y)}")
    print(f"The multiplication of {x} * {y} = {calculator.multiply(x, y)}")
    print(f"The division of {x} / {y} = {calculator.divide(x, y)}")