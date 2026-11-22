
# ==============================================================================
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA - UNAD
# Curso: Programacion (213023) - Fase 4
# Modulo: modelos_base.py
# Descripcion: Modelos generales y gestion de clientes.
# ==============================================================================

from abc import ABC, abstractmethod
import re

from excepciones_y_logs import ErrorValidacion, ErrorCliente


class EntidadBase(ABC):
    """Clase abstracta que representa una entidad general del sistema."""

    def __init__(self, identificador):
        if not isinstance(identificador, str) or not identificador.strip():
            raise ErrorValidacion(
                "El identificador no puede estar vacio.",
                "ID_INVALIDO"
            )

        self._identificador = identificador.strip()

    @property
    def identificador(self):
        """Permite consultar el identificador de forma controlada."""
        return self._identificador

    @abstractmethod
    def obtener_resumen(self):
        """Define el metodo que deben implementar las clases derivadas."""
        pass


class Cliente(EntidadBase):
    """Representa un cliente con datos personales encapsulados."""

    def __init__(self, id_c, nombre, doc, correo, tel):
        super().__init__(id_c)

        self._nombre = self._validar_nombre(nombre)
        self._documento = self._validar_documento(doc)
        self._correo = self._validar_correo(correo)
        self._telefono = self._validar_telefono(tel)

    def _validar_nombre(self, nombre):
        """Comprueba que el nombre tenga un formato valido."""

        if not isinstance(nombre, str) or len(nombre.strip()) < 3:
            raise ErrorCliente(
                "El nombre debe contener al menos tres caracteres.",
                "NOMBRE_INVALIDO"
            )

        return nombre.strip()

    def _validar_documento(self, documento):
        """Valida que el documento contenga entre 6 y 15 digitos."""

        if not isinstance(documento, str):
            documento = str(documento)

        documento = documento.strip()

        if not documento.isdigit() or not 6 <= len(documento) <= 15:
            raise ErrorCliente(
                "El documento debe contener entre 6 y 15 digitos.",
                "DOCUMENTO_INVALIDO"
            )

        return documento

    def _validar_correo(self, correo):
        """Verifica el formato basico de una direccion de correo."""

        if not isinstance(correo, str):
            raise ErrorCliente(
                "El correo debe ser una cadena de texto.",
                "CORREO_INVALIDO"
            )

        correo = correo.strip()

        patron = r"^[\w.+-]+@[\w-]+(?:\.[\w-]+)+$"

        if not re.match(patron, correo):
            raise ErrorCliente(
                "La direccion de correo electronico no es valida.",
                "CORREO_INVALIDO"
            )

        return correo.lower()

    def _validar_telefono(self, telefono):
        """Valida que el telefono contenga entre 7 y 15 digitos."""

        if not isinstance(telefono, str):
            telefono = str(telefono)

        telefono = telefono.strip()

        if not telefono.isdigit() or not 7 <= len(telefono) <= 15:
            raise ErrorCliente(
                "El telefono debe contener entre 7 y 15 digitos.",
                "TELEFONO_INVALIDO"
            )

        return telefono

    @property
    def nombre(self):
        return self._nombre

    @property
    def documento(self):
        return self._documento

    @property
    def correo(self):
        return self._correo

    @property
    def telefono(self):
        return self._telefono

    def obtener_resumen(self):
        """Devuelve un resumen de la informacion del cliente."""

        return (
            f"Cliente: {self._nombre} | "
            f"ID: {self.identificador} | "
            f"Documento: {self._documento} | "
            f"Correo: {self._correo} | "
            f"Telefono: {self._telefono}"
        )