# ==============================================================================
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA - UNAD
# Curso: Programacion (213023) - Fase 4
# Modulo: servicios.py
# Descripcion: Gestion de servicios especializados de Software FJ.
# ===============================================================================

from abc import ABC, abstractmethod
import math

from excepciones_y_logs import ErrorServicio, ErrorValidacion


class Servicio(ABC):
    """Clase abstracta que representa un servicio general."""

    def __init__(self, identificador, nombre, tarifa_base):
        if not isinstance(identificador, str) or not identificador.strip():
            raise ErrorValidacion(
                "El identificador del servicio es obligatorio.",
                "ID_SERVICIO_INVALIDO"
            )
        if not isinstance(nombre, str) or len(nombre.strip()) < 3:
            raise ErrorServicio(
                "El nombre del servicio debe tener al menos tres caracteres.",
                "NOMBRE_SERVICIO_INVALIDO"
            )
        try:
            tarifa = float(tarifa_base)
        except (ValueError, TypeError) as error:
            raise ErrorServicio(
                "La tarifa debe ser un valor numerico.",
                "TARIFA_INVALIDA"
            ) from error
        if not math.isfinite(tarifa) or tarifa <= 0:
            raise ErrorServicio(
                "La tarifa debe ser un valor finito mayor que cero.",
                "TARIFA_INVALIDA"
            )

        self._identificador = identificador.strip()
        self._nombre = nombre.strip()
        self._tarifa_base = tarifa
        self._disponible = True

    @property
    def identificador(self):
        return self._identificador

    @property
    def nombre(self):
        return self._nombre

    @property
    def tarifa_base(self):
        return self._tarifa_base

    @property
    def disponible(self):
        return self._disponible

    def cambiar_disponibilidad(self, estado):
        """Modifica la disponibilidad del servicio."""
        if not isinstance(estado, bool):
            raise ErrorValidacion(
                "La disponibilidad debe ser verdadera o falsa.",
                "ESTADO_INVALIDO"
            )
        self._disponible = estado

    @abstractmethod
    def calcular_costo(self, horas, descuento=0.0, impuesto=0.0):
        """Calcula el costo del servicio segun sus caracteristicas."""
        pass

    @abstractmethod
    def describir_servicio(self):
        """Describe las caracteristicas particulares del servicio."""
        pass

    def obtener_resumen(self):
        return (
            f"{self._nombre} | ID: {self._identificador} | "
            f"Tarifa: ${self._tarifa_base:,.2f} | "
            f"Disponible: {'Si' if self._disponible else 'No'}"
        )


class ReservaSala(Servicio):
    """Servicio especializado en reserva de salas."""

    def __init__(self, identificador, nombre, tarifa_base, capacidad,
                 tiene_proyector=False):
        super().__init__(identificador, nombre, tarifa_base)
        if isinstance(capacidad, bool) or not isinstance(capacidad, int) or capacidad <= 0:
            raise ErrorServicio(
                "La capacidad de la sala debe ser un entero positivo.",
                "CAPACIDAD_INVALIDA"
            )
        if not isinstance(tiene_proyector, bool):
            raise ErrorServicio(
                "El proyector debe indicarse como verdadero o falso.",
                "PROYECTOR_INVALIDO"
            )
        self._capacidad = capacidad
        self._tiene_proyector = tiene_proyector

    @property
    def capacidad(self):
        return self._capacidad

    @property
    def tiene_proyector(self):
        return self._tiene_proyector

    def calcular_costo(self, horas, descuento=0.0, impuesto=0.0):
        if (isinstance(horas, bool) or not isinstance(horas, (int, float))
                or not math.isfinite(horas) or horas <= 0):
            raise ErrorValidacion(
                "La cantidad de horas debe ser un valor finito positivo.",
                "DURACION_INVALIDA"
            )
        return _calcular_total(self._tarifa_base, horas, descuento, impuesto)

    def describir_servicio(self):
        proyector = "Si" if self._tiene_proyector else "No"
        return (
            f"Sala: {self._nombre} | Capacidad: {self._capacidad} personas | "
            f"Proyector: {proyector}"
        )

    def obtener_resumen(self):
        return (
            f"{super().obtener_resumen()} | Capacidad: {self._capacidad} | "
            f"Proyector: {'Si' if self._tiene_proyector else 'No'}"
        )


class AlquilerEquipo(Servicio):
    """Servicio especializado en alquiler de equipos tecnologicos."""

    def __init__(self, identificador, nombre, tarifa_base, gama,
                 incluye_seguro=False):
        super().__init__(identificador, nombre, tarifa_base)
        if not isinstance(gama, str) or not gama.strip():
            raise ErrorServicio(
                "La gama del equipo es obligatoria.",
                "GAMA_INVALIDA"
            )
        if not isinstance(incluye_seguro, bool):
            raise ErrorServicio(
                "El seguro debe indicarse como verdadero o falso.",
                "SEGURO_INVALIDO"
            )
        self._gama = gama.strip().upper()
        self._incluye_seguro = incluye_seguro

    @property
    def gama(self):
        return self._gama

    @property
    def incluye_seguro(self):
        return self._incluye_seguro

    def calcular_costo(self, horas, descuento=0.0, impuesto=0.0):
        if (isinstance(horas, bool) or not isinstance(horas, (int, float))
                or not math.isfinite(horas) or horas <= 0):
            raise ErrorValidacion(
                "Las horas de alquiler deben ser un valor finito positivo.",
                "DURACION_INVALIDA"
            )
        tarifa = self._tarifa_base
        if self._incluye_seguro:
            tarifa *= 1.10
        return _calcular_total(tarifa, horas, descuento, impuesto)

    def describir_servicio(self):
        seguro = "Incluido" if self._incluye_seguro else "No incluido"
        return f"Equipo: {self._nombre} | Gama: {self._gama} | Seguro: {seguro}"

    def obtener_resumen(self):
        return (
            f"{super().obtener_resumen()} | Gama: {self._gama} | "
            f"Seguro: {'Si' if self._incluye_seguro else 'No'}"
        )


class AsesoriaEspecializada(Servicio):
    """Servicio de asesorias profesionales especializadas."""

    def __init__(self, identificador, nombre, tarifa_base, especialidad,
                 es_urgente=False):
        super().__init__(identificador, nombre, tarifa_base)
        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ErrorServicio(
                "La especialidad de la asesoria es obligatoria.",
                "ESPECIALIDAD_INVALIDA"
            )
        if not isinstance(es_urgente, bool):
            raise ErrorServicio(
                "La urgencia debe indicarse como verdadero o falso.",
                "URGENCIA_INVALIDA"
            )
        self._especialidad = especialidad.strip()
        self._es_urgente = es_urgente

    @property
    def especialidad(self):
        return self._especialidad

    @property
    def es_urgente(self):
        return self._es_urgente

    def calcular_costo(self, horas, descuento=0.0, impuesto=0.0):
        if (isinstance(horas, bool) or not isinstance(horas, (int, float))
                or not math.isfinite(horas) or horas <= 0):
            raise ErrorValidacion(
                "Las horas de asesoria deben ser un valor finito positivo.",
                "DURACION_INVALIDA"
            )
        tarifa = self._tarifa_base
        if self._es_urgente:
            tarifa *= 1.25
        return _calcular_total(tarifa, horas, descuento, impuesto)

    def describir_servicio(self):
        urgencia = "Si" if self._es_urgente else "No"
        return (
            f"Asesoria: {self._nombre} | Especialidad: {self._especialidad} | "
            f"Urgente: {urgencia}"
        )

    def obtener_resumen(self):
        return (
            f"{super().obtener_resumen()} | Especialidad: {self._especialidad} | "
            f"Urgente: {'Si' if self._es_urgente else 'No'}"
        )


def _calcular_total(tarifa, horas, descuento=0.0, impuesto=0.0):
    """Realiza el calculo general del costo con descuento e impuesto."""
    if (isinstance(descuento, bool) or not isinstance(descuento, (int, float))
            or not math.isfinite(descuento)):
        raise ErrorValidacion(
            "El descuento debe ser un numero finito.",
            "DESCUENTO_INVALIDO"
        )
    if (isinstance(impuesto, bool) or not isinstance(impuesto, (int, float))
            or not math.isfinite(impuesto)):
        raise ErrorValidacion(
            "El impuesto debe ser un numero finito.",
            "IMPUESTO_INVALIDO"
        )
    if not 0 <= descuento <= 1:
        raise ErrorValidacion(
            "El descuento debe estar entre 0 y 1.",
            "DESCUENTO_INVALIDO"
        )
    if impuesto < 0:
        raise ErrorValidacion(
            "El impuesto no puede ser negativo.",
            "IMPUESTO_INVALIDO"
        )

    subtotal = tarifa * horas
    subtotal -= subtotal * descuento
    total = subtotal * (1 + impuesto)
    if not math.isfinite(total):
        raise ErrorValidacion(
            "El costo calculado excede el rango permitido.",
            "COSTO_INVALIDO"
        )
    return total
