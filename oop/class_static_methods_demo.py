class Calculator:
    calculation_type = "Arithmetic Operations"

    def __init__(self):
        pass

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Returns the sum of two numbers.
        
        Args:
        a (float): The first number.
        b (float): The second number.
        
        Returns:
        float: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Returns the product of two numbers.

        Args:
        a (float): The first number.
        b (float): The second number.

        Returns:
        float: The product of a and b.
        """
        print(f"Calculation type:{cls.calculation_type}")
        return a * b

if __name__ == "__main__":
    calculator = Calculator()

    result1 = Calculator.add(10, 5)
    print(f"Addition result: {result1}")

    result2 = Calculator.multiply(10, 5)
    print(f"Multiplication result: {result2}")


