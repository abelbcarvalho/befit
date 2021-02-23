from abc import ABCMeta


class IFacade(metaclass=ABCMeta):
    """Classe abstrata que simula o uso de uma interface.
    Pertence a Facade.
    """

    # Person

    def create_person(self, person) -> bool:
        pass

    def read_person(self, sql='select * from tbPerson', **kwargs):
        pass

    def update_person(self, person) -> bool:
        pass

    def delete_person(self, person) -> bool:
        pass

    def read_all_person(self, sql='select * from tbPerson'):
        pass

    # Peso

    def create_peso(self, peso) -> bool:
        pass

    def read_peso(self, sql='select * from tbPeso', **kwargs):
        pass

    def delete_peso(self, peso) -> bool:
        pass

    def delete_all_peso(self, fk=0) -> bool:
        pass

    # Centimetros

    def create_centimetros(self, centimetros) -> bool:
        pass

    def read_centimetros(self, sql='select * from tbPeso', **kwargs):
        pass

    def delete_centimetros(self, centimetros) -> bool:
        pass

    def delete_all_centimetros(self, fk=0) -> bool:
        pass
