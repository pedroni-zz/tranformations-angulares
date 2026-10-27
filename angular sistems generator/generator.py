import random
from .angles import AngularSystem

class AngleGenerator:
    """Generador de ángulos aleatorios en diferentes rangos y sistemas."""
    
    @staticmethod
    def random_angle(min_deg=0.0, max_deg=360.0, decimals=2) -> AngularSystem:
        """Genera un ángulo aleatorio dentro de un rango sexagesimal."""
        deg = round(random.uniform(min_deg, max_deg), decimals)
        return AngularSystem(deg, system='sexagesimal')

    @staticmethod
    def batch_generate(count=5, min_deg=0.0, max_deg=360.0) -> list:
        """Genera una lista de múltiples ángulos convertidos a todos los sistemas."""
        return [AngleGenerator.random_angle(min_deg, max_deg) for _ in range(count)]