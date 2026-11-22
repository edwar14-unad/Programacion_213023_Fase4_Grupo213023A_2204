# ==============================================================================
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA - UNAD
# Curso: Programacion (213023) - Fase 4
# Modulo: reservas.py
# Descripcion: Gestion, confirmacion y procesamiento de reservas.
# ===============================================================================

import math

from excepciones_y_logs import (
    SoftwareFJError,
    ErrorValidacion,
    ErrorReserva,
    ServicioNoDisponible,
    OperacionNoPermitida
)


class Reserva:
    """Representa una reserva realizada por un cliente."""

    def __init__(self, identificador, cliente, servicio, horas, logger=None):
        """Inicializa la reserva y valida sus datos principales."""
        if not isinstance(identificador, str) or not identificador.strip():
            raise ErrorValidacion(
                "El identificador de la reserva es obligatorio.",
                "ID_RESERVA_INVALIDO"
            )
        if cliente is None or not hasattr(cliente, "obtener_resumen"):
            raise ErrorReserva(
                "La reserva necesita un cliente valido.",
                "CLIENTE_INVALIDO"
            )
        if servicio is None or not hasattr(servicio, "calcular_costo"):
            raise ErrorReserva(
                "La reserva necesita un servicio valido.",
                "SERVICIO_INVALIDO"
            )
        if (isinstance(horas, bool) or not isinstance(horas, (int, float))
                or not math.isfinite(horas)):
            raise ErrorValidacion(
                "La duracion debe ser un numero finito.",
                "DURACION_INVALIDA"
            )
        if horas <= 0:
            raise ErrorValidacion(
                "La duracion de la reserva debe ser mayor que cero.",
                "DURACION_INVALIDA"
            )

        self._identificador = identificador.strip()
        self._cliente = cliente
        self._servicio = servicio
        self._horas = horas
        self._logger = logger
        self._estado = "PENDIENTE"
        self._costo = 0.0
        self._motivo_cancelacion = None
        self._registrar_evento(
            "INFO",
            f"Reserva {self._identificador} creada correctamente."
        )

    @property
    def identificador(self):
        return self._identificador

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def horas(self):
        return self._horas

    @property
    def estado(self):
        return self._estado

    @property
    def costo(self):
        return self._costo

    def _registrar_evento(self, nivel, mensaje, error=None):
        """Registra eventos cuando se dispone de un gestor de logs."""
        if self._logger is not None:
            self._logger.registrar_evento(nivel, "Reservas", mensaje, error)

    def confirmar(self, descuento=0.0):
        """Confirma la reserva y calcula el costo correspondiente."""
        try:
            if self._estado != "PENDIENTE":
                raise OperacionNoPermitida(
                    "Solo se pueden confirmar reservas pendientes.",
                    "ESTADO_RESERVA_INVALIDO"
                )
            if not self._servicio.disponible:
                raise ServicioNoDisponible(
                    "El servicio seleccionado no esta disponible.",
                    "SERVICIO_OCUPADO"
                )

            self._costo = self._servicio.calcular_costo(
                self._horas,
                descuento=descuento
            )
            self._servicio.cambiar_disponibilidad(False)
            self._estado = "CONFIRMADA"
            self._registrar_evento(
                "INFO",
                f"Reserva {self._identificador} confirmada. "
                f"Costo: ${self._costo:,.2f}"
            )
            return True

        except SoftwareFJError as error:
            self._registrar_evento(
                "ERROR",
                f"Error al confirmar reserva {self._identificador}.",
                error
            )
            raise

    def procesar(self):
        """Finaliza una reserva previamente confirmada."""
        if self._estado != "CONFIRMADA":
            error = OperacionNoPermitida(
                "Solo se pueden procesar reservas confirmadas.",
                "PROCESAMIENTO_NO_PERMITIDO"
            )
            self._registrar_evento(
                "ERROR",
                f"No fue posible procesar la reserva {self._identificador}.",
                error
            )
            raise error

        self._estado = "PROCESADA"
        self._registrar_evento(
            "INFO",
            f"Reserva {self._identificador} procesada correctamente."
        )
        return True

    def cancelar(self, motivo):
        """Cancela una reserva y libera el servicio cuando corresponde."""
        if self._estado == "PROCESADA":
            error = OperacionNoPermitida(
                "No se puede cancelar una reserva que ya fue procesada.",
                "CANCELACION_NO_PERMITIDA"
            )
            self._registrar_evento(
                "ERROR",
                f"Intento de cancelar reserva procesada {self._identificador}.",
                error
            )
            raise error

        if self._estado == "CANCELADA":
            raise OperacionNoPermitida(
                "La reserva ya se encuentra cancelada.",
                "RESERVA_YA_CANCELADA"
            )
        if not isinstance(motivo, str) or not motivo.strip():
            raise ErrorValidacion(
                "Debe indicar el motivo de la cancelacion.",
                "MOTIVO_INVALIDO"
            )

        if self._estado == "CONFIRMADA":
            self._servicio.cambiar_disponibilidad(True)

        self._estado = "CANCELADA"
        self._motivo_cancelacion = motivo.strip()
        self._registrar_evento(
            "WARNING",
            f"Reserva {self._identificador} cancelada. "
            f"Motivo: {self._motivo_cancelacion}"
        )
        return True

    def obtener_resumen(self):
        """Devuelve la informacion general de la reserva."""
        return (
            f"Reserva: {self._identificador} | "
            f"Cliente: {self._cliente.nombre} | "
            f"Servicio: {self._servicio.nombre} | "
            f"Duracion: {self._horas} horas | "
            f"Estado: {self._estado} | "
            f"Costo: ${self._costo:,.2f}"
        )
