
# ==============================================================================
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA - UNAD
# Curso: Programacion (213023) - Fase 4
# Modulo: excepciones_y_logs.py
# Descripcion: Manejo de excepciones personalizadas y registro de eventos.
# ==============================================================================

import logging


class SoftwareFJError(Exception):
    """Excepcion base para los errores controlados del sistema."""

    def __init__(self, mensaje, codigo_error="ERROR_GENERAL"):
        self.codigo_error = codigo_error
        super().__init__(mensaje)


class ErrorValidacion(SoftwareFJError):
    """Se genera cuando los datos ingresados no cumplen las validaciones."""
    pass


class ErrorCliente(SoftwareFJError):
    """Se genera cuando ocurre un error relacionado con un cliente."""
    pass


class ErrorServicio(SoftwareFJError):
    """Se genera cuando un servicio presenta datos o parametros incorrectos."""
    pass


class ServicioNoDisponible(SoftwareFJError):
    """Se genera cuando un servicio no puede ser reservado."""
    pass


class ErrorReserva(SoftwareFJError):
    """Se genera cuando una reserva presenta algun inconveniente."""
    pass


class OperacionNoPermitida(SoftwareFJError):
    """Se genera cuando se intenta realizar una operacion no permitida."""
    pass


class GestorLogs:
    """Administra el registro de eventos y errores del sistema."""

    def __init__(self, nombre_archivo="sistema_fj.log"):
        """Configura el archivo donde se almacenaran los registros."""

        self.nombre_archivo = nombre_archivo

        self.logger = logging.getLogger(
            f"SoftwareFJ_{nombre_archivo}"
        )

        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

        # Evita agregar varios manejadores al mismo registro.
        if not self.logger.handlers:
            manejador = logging.FileHandler(
                nombre_archivo,
                encoding="utf-8"
            )

            formato = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            manejador.setFormatter(formato)
            self.logger.addHandler(manejador)

    def registrar_evento(self, nivel, modulo, mensaje, error=None):
        """Registra eventos informativos y errores del sistema."""

        niveles = {
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL
        }

        nivel_registro = niveles.get(
            str(nivel).upper(),
            logging.INFO
        )

        detalle = f"[{modulo}] {mensaje}"

        if error is not None:
            detalle += (
                f" | Tipo de error: {type(error).__name__}"
                f" | Detalle: {error}"
            )

        self.logger.log(nivel_registro, detalle)

        # Conserva la informacion completa del error cuando existe
        # una excepcion activa.
        if error is not None:
            self.logger.debug(
                "Detalle tecnico de la excepcion",
                exc_info=(
                    type(error),
                    error,
                    error.__traceback__
                )
            )