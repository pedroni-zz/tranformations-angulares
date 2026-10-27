# 📐 Generador de Sistemas Angulares

Librería modular en Python para calcular, convertir y generar ángulos automáticamente entre los tres sistemas angulares fundamentales:
* **Sistema Sexagesimal** (Grados, Minutos, Segundos — DMS y grados decimales)
* **Sistema Centesimal** (Gradián / Gon — 400 gon por circunferencia)
* **Sistema Radial** (Radianes y representación en términos de $\pi$)

---

## 📂 Estructura del Proyecto

```text
angular-systems-generator/
│
├── README.md               # Documentación del repositorio
├── src/
│   ├── __init__.py         # Módulo interno de Python
│   ├── angles.py           # Clase AngularSystem (conversiones)
│   └── generator.py        # Clase AngleGenerator (aleatorios/lotes)
└── main.py                 # Script de prueba y ejecución directa
```

---

## 🚀 Uso Rápido

### 1. Conversión de Ángulos
```python
from src.angles import AngularSystem

# Crear un ángulo desde grados sexagesimales (45.5°)
angulo = AngularSystem(45.5, system='sexagesimal')
print(angulo)

# Crear un ángulo desde radianes (1.5 rad)
angulo_rad = AngularSystem(1.5, system='radian')
print(angulo_rad)
```

### 2. Generación Aleatoria
```python
from src.generator import AngleGenerator

# Generar un lote de 5 ángulos aleatorios entre 0° y 360°
lote = AngleGenerator.batch_generate(count=5)

for a in lote:
    print(a)
```

---

## 🛠️ Requisitos e Instalación

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/angular-systems-generator.git](https://github.com/tu-usuario/angular-systems-generator.git)
   ```
2. Navegar al directorio:
   ```bash
   cd angular-systems-generator
   ```
3. Ejecutar el script principal:
   ```bash
   python main.py
   ```