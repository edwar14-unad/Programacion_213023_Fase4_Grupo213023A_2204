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
| `README.md` | Documentación general del proyecto e instrucciones de ejecución. | John Eyder Cano Chavez (`jecanounad`) |
| `main.py` | Controlador principal y ejecución secuencial de las operaciones de prueba. | John Eyder Cano Chavez (`jecanounad`) |
| `excepciones_y_logs.py` | Jerarquía de excepciones personalizadas y gestor de registros. | Eduar Andres Osorio (`edwar14-unad`) |
| `modelos_base.py` | Clase abstracta `EntidadBase` y clase `Cliente`, con sus respectivas validaciones. | Eduar Andres Osorio (`edwar14-unad`) |
| `servicios.py` | Clase `Servicio` y servicios especializados: `ReservaSala`, `AlquilerEquipo` y `AsesoriaEspecializada`. | Eduar Andres Osorio (`edwar14-unad`) |
| `reservas.py` | Clase `Reserva`, con gestión de estados, confirmación, cancelación y procesamiento. | Eduar Andres Osorio (`edwar14-unad`) |

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

El desarrollo del proyecto contó con la participación de dos integrantes.

**John Eyder Cano Chavez** desarrolló el archivo `main.py`, encargado de la ejecución y coordinación de las operaciones del sistema, y elaboró la documentación del proyecto mediante el archivo `README.md`.

**Eduar Andres Osorio** realizó el desarrollo de los módulos `excepciones_y_logs.py`, `modelos_base.py`, `servicios.py` y `reservas.py`, implementando la gestión de excepciones, los modelos de clientes, los servicios especializados y el manejo de reservas.
