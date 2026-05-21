from abc import abstractmethod,ABC
from partituras.modelo.errores import (
    ContieneNumero,
    ContieneCaracterInvalido,
    SinNotas,
    EspacioMultiple,
    EspacioBordes,
)

class ReglaTransformacion(ABC):
    def __init__(self, token:int):
        self.token:int = token

    @abstractmethod
    def transformar(self,partitura: str) -> str:
        ...
    @abstractmethod
    def revertir(self,partitura: str) -> str:
        ...
    @abstractmethod
    def partitura_valida(self, partitura: str) -> bool:
        ...
    def encontrar_numeros_partitura(self):
        ...
    def encontrar_caracteres_invalidos(self):
        ...


class ReglaTransposicion(ReglaTransformacion):
    def partitura_valida(self, partitura: str) -> bool:
        pass

    def revertir(self, partitura: str) -> str:
        pass

    def transformar(self, partitura: str) -> str:
        pass

class ReglaFrecuencia(ReglaTransformacion):
    def partitura_valida(self, partitura: str) -> bool:
        pass

    def revertir(self, partitura: str) -> str:
        pass

    def transformar(self, partitura: str) -> str:
        pass

class Compositor:

    def __init__(self, interprete: ReglaTransformacion):
        self.interprete = interprete

    def transformar(self, partitura: str) -> str:
        pass

    def revertir(self, partitura: str) -> str:
        pass