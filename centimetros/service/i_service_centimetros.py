from abc import ABCMeta


class IServiceCentimetros(metaclass=ABCMeta):
    """Classe abstrata que simula o uso de interface.
    Deve ser usado com o service de Centimetros.
    """

    def create_centimetros(self, centimetros) -> bool:
        pass

    def read_centimetros(self, sql='select * from tbPeso', **kwargs):
        pass

    def delete_centimetros(self, centimetros) -> bool:
        pass

    def delete_all_centimetros(self, fk=0) -> bool:
        pass
