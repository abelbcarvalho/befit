from abc import ABCMeta


class IDAOPerson(metaclass=ABCMeta):
    """Classe abstrata para o DAO Person.
    """

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
