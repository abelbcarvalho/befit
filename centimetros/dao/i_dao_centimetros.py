from abc import ABCMeta


class IDAOCentimetros(metaclass=ABCMeta):
    """Classe abstrata que simula interface
    para DAOCentimetros.
    """

    def create_centimetros(self, centimetros) -> bool:
        pass

    def read_centimetros(self, sql='select * from tbPeso', **kwargs):
        pass

    def delete_centimetros(self, centimetros) -> bool:
        pass

    def delete_all_centimetros(self, fk=0) -> bool:
        pass
