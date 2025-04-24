class Vector:
    def __init__(self, components):
        self.components = components

    def __str__(self):
        return f"Vector({self.components})"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of same dimension to add")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of same dimension to find dot product")
        dot_product = sum(a * b for a, b in zip(self.components, other.components))
        return dot_product

# Example usage:
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("v1 + v2 =", v1 + v2)           # Vector addition
print("v1 . v2 =", v1 * v2)           # Dot product
