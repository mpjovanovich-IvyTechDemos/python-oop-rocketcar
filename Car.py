"""
Car is the base class, or superclass, of all other car classes.
It has a simple interface: a constructor and one "move" method.
"""
# Reminder: 
# "superclass" = "parent class" = "base class"
# "subclass" = "child class"

class Car:
    def __init__(self, x):
        # Protected attributes (single underscore in Python)
        # These can be used by this class and any child classes,
        # but should not be accessed directly by other code that uses our car.
        self._x = x
        self._speed = 1.0
        print(f"Car created at position {self._x}")

    # This is a public method, meant to be called by any other code.
    def move(self):
        """Moves the car forward by its speed"""
        self._x += self._speed
        print(f"Position: {self._x}")

# # Example Usage - uncomment for testing
# car = Car(0)
# car.move()
# car.move()