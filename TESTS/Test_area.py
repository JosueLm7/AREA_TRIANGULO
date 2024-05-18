import unittest

class TestAreaTriangulo(unittest.TestCase):
    def area_triangulo(self, base, altura):
        """Calcula el área de un triángulo."""
        return (base * altura) / 2

    def test_cases(self):
        """Ejecuta todos los casos de prueba para el cálculo del área de un triángulo."""
        cases = [
            (5, 8, 20),
            (10, 12, 60),
            (7, 3, 10.5),
            (15, 6, 45),
            (20, 9, 90),
            (6, 4, 12),
            (12, 15, 90),
            (8, 20, 80),
            (18, 7, 63),
            (25, 10, 125)
        ]

        for i, (base, altura, expected) in enumerate(cases, 1):
            with self.subTest(case=i):
                result = self.area_triangulo(base, altura)
                self.assertEqual(result, expected, f"Failed on case {i}: area_triangulo({base}, {altura}) = {result}, expected {expected}")

if __name__ == '__main__':
    unittest.main()