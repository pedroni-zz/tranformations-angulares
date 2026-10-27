from src.generator import AngleGenerator
from src.angles import AngularSystem

def main():
    print("=== Generador de Sistemas Angulares ===\n")
    
    # 1. Generar 3 ángulos aleatorios de prueba
    print("Generando ángulos aleatorios:")
    angles = AngleGenerator.batch_generate(count=3)
    for i, ang in enumerate(angles, 1):
        print(f"\n[Ángulo {i}]")
        print(ang)
        print("-" * 30)

    # 2. Conversión manual de ejemplo (ej. 1.5 radianes)
    print("\nEjemplo de conversión directa (1.5 radianes):")
    custom_angle = AngularSystem(1.5, system='radian')
    print(custom_angle)

if __name__ == "__main__":
    main()