# Sistema Integral de Gestión de Clientes, Servicios y Reservas – Software FJ

**Universidad Nacional Abierta y a Distancia – UNAD**  
**Programa:** Ingeniería de Sistemas  
**Curso:** Programación (Código: 213023)  
**Actividad:** Fase 4 – Componente práctico (Prácticas simuladas)  
**Grupo:** 213023A_2204  
**Tutor:** Jaider José Lineros Fragoso  

---

## Descripción del Proyecto

Aplicación desarrollada en **Python 3** bajo el paradigma de **Programación Orientada a Objetos (POO)**, sin el uso de bases de datos. La información se gestiona en memoria mediante objetos y listas. El sistema está orientado a la administración de clientes, servicios tecnológicos y reservas para la empresa **Software FJ**.

El sistema implementa:

- Clases abstractas (`EntidadBase` y `Servicio`).
- Herencia, encapsulamiento y polimorfismo.
- Validaciones mediante excepciones personalizadas.
- Manejo de errores mediante bloques `try / except`.
- Encadenamiento de excepciones mediante `raise ... from`.
- Registro de eventos y errores en el archivo `sistema_fj.log`.

---

## Estructura Modular del Repositorio

| Archivo | Descripción | Responsable |
| :--- | :--- | :--- |
| `excepciones_y_logs.py` | Jerarquía de excepciones personalizadas y gestor de registros. | Eduar Andres Osorio (`edwar14-unad`) |
| `modelos_base.py` | Clase abstracta `EntidadBase` y clase `Cliente`, con sus respectivas validaciones. | John Eyder Cano Chavez (`jecanounad`) |
| `servicios.py` | Clase `Servicio` y servicios especializados: `ReservaSala`, `AlquilerEquipo` y `AsesoriaEspecializada`. | Eduar Andres Osorio (`edwar14-unad`) |
| `reservas.py` | Clase `Reserva`, con gestión de estados, confirmación, cancelación y procesamiento. | Eduar Andres Osorio (`edwar14-unad`) |
| `main.py` | Controlador principal y ejecución secuencial de operaciones de prueba. | John Eyder Cano Chavez (`jecanounad`) |

---

## Ejecución del Proyecto

1. Clonar o descargar el repositorio.
2. Contar con **Python 3.10 o superior** instalado.
3. Abrir una terminal en la carpeta raíz del proyecto.
4. Ejecutar el archivo principal con el siguiente comando:

```bash
python main.py
```

---

## Aportes al Proyecto

Se realizaron aportes individuales en los módulos `servicios.py` y `reservas.py`, implementando la creación y validación de servicios, así como la gestión de reservas y sus respectivos estados, excepciones y registros.
