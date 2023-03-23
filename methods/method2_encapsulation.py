class Circle:
    """
    A class representing a circle with a given radius.
    """
    def __init__(self, radius):
        """
        Initializes the Circle instance with the given radius.

        Parameters:
        radius (float): The radius of the circle.
        """
        self._radius = radius
        
    @property
    def diameter(self):
        """
        Computes and returns the diameter of the circle based on the current radius.

        Returns:
        float: The diameter of the circle.
        """
        return 2 * self._radius
    
    @diameter.setter
    def diameter(self, value):
        """
        Updates the radius of the circle based on the new diameter value.

        Parameters:
        value (float): The new diameter value assigned to the diameter attribute.
        """
        self._radius = value/2
        
    def get_radius(self):
        """
        Returns the current radius value of the circle.

        Returns:
        float: The current radius value of the circle.
        """
        return self._radius
        
# Create an instance of Circle with radius 5
circle = Circle(5)

# Print the diameter of the circle
print(circle.diameter)

# Change the diameter to 20 and print the new radius
circle.diameter = 20
print(circle.get_radius())