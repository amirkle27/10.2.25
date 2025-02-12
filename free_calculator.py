from full_calculator import FullCalculator


class FreeCalculator:
    def __init__(self,username):
        self.full_calc = FullCalculator()
        self.username = username


    def add(self, a, b):
        """Returns the sum of a and b."""
        return f"{self.username}, the result is: {self.full_calc.add(a,b)}"

    def sub(self, a, b):
        """Returns the difference between a and b."""
        return f"{self.username}, the result is: {self.full_calc.sub(a,b)}"

    def mul(self, a, b):
        """Returns the product of a and b."""
        return f"Dear {self.username}, Multiplication is only available in the paid version. Upgrade to access this feature."


    def div(self, a, b):
        """Returns the quotient of a divided by b.
        Raises a ZeroDivisionError if b is 0.
        """
        return f"Dear {self.username}, Division is available only with paid version. Upgrade to access this feature."

    def power(self, a, b):
        """Returns a raised to the power of b."""
        return f"Dear {self.username}, Power is available only with paid version. Upgrade to access this feature."

calc1 = FreeCalculator("Amir")
print(calc1.div(2,1))
print(calc1.add(1,1))
print(calc1.power(2,200))
print(calc1.sub(2,2))