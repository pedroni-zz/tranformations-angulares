import math

class AngularSystem:
    """Clase para representar y convertir ángulos entre sistemas sexagesimal, centesimal y radial."""
    
    def __init__(self, value: float, system: str = 'sexagesimal'):
        """
        value: valor numérico del ángulo.
        system: 'sexagesimal' (grados decimales), 'centesimal' (gon), o 'radian' (rad).
        """
        system = system.lower()
        if system == 'sexagesimal':
            self.degrees = float(value)
            self.grads = self.degrees * (200 / 180)
            self.radians = math.radians(self.degrees)
        elif system == 'centesimal':
            self.grads = float(value)
            self.degrees = self.grads * (180 / 200)
            self.radians = math.radians(self.degrees)
        elif system in ['radian', 'radianes']:
            self.radians = float(value)
            self.degrees = math.degrees(self.radians)
            self.grads = self.degrees * (200 / 180)
        else:
            raise ValueError("Sistema no válido. Usa 'sexagesimal', 'centesimal' o 'radian'.")

    def to_dms(self) -> tuple:
        """Convierte grados decimales a Grados, Minutos y Segundos (DMS)."""
        d = int(self.degrees)
        m_float = (self.degrees - d) * 60
        m = int(m_float)
        s = (m_float - m) * 60
        return d, m, s

    def __str__(self):
        d, m, s = self.to_dms()
        return (
            f"--- Conversión de Ángulo ---\n"
            f"  Sexagesimal (Decimal): {self.degrees:.4f}°\n"
            f"  Sexagesimal (DMS):     {d}° {m}' {s:.2f}\"\n"
            f"  Centesimal (Gon):      {self.grads:.4f} gon\n"
            f"  Radianes:              {self.radians:.4f} rad ({self.radians / math.pi:.4f}π)"
        )