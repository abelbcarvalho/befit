from abc import ABCMeta


class IServicePeso(metaclass=ABCMeta):
    """Classe abstrata que simula o uso de interface.
    Deve ser usado com o service de Peso.
    """

    def create_peso(self, peso) -> bool:
        pass

    def read_peso(self, sql='select * from tbPeso', **kwargs):
        pass

    def delete_peso(self, peso) -> bool:
        pass

    def delete_all_peso(self, fk=0) -> bool:
        pass
