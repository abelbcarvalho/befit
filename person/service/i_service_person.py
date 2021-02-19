from abc import ABCMeta


class IServicePerson(metaclass=ABCMeta):
    """Classe abstrata que representa uma interface
    e deve ser usada junto ao service de Person.
    """

    def create_person(self, person) -> bool:
        pass

    def read_person(self, sql='select * from tbPerson', **kwargs):
        pass

    def update_person(self, person) -> bool:
        pass

    def delete_person(self, person) -> bool:
        pass
