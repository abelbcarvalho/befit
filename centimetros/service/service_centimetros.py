from centimetros.service.i_service_centimetros import IServiceCentimetros
from centimetros.model.Centimetros import Centimetros
from core.data.data import Data
from tools.data_check import DataCheck
from tools.general import is_int_positive, is_none_empty, instance
from tools.general import is_small_equal, tira_espacos_inicio_final


class ServiceCentimetros(IServiceCentimetros):
    """Regra de Negócio para Centimetros.

    Args:
        IServiceCentimetros (abstract): interface.
    """

    def __init__(self) -> None:
        """Novo service de Centimetros.
        """
        super().__init__()

    def create_Centimetros(self, centimetros: Centimetros) -> bool:
        """Registra novo Centimetros.

        Args:
            centimetros (Centimetros): Centimetros instance.

        Returns:
            bool: True se centimetros registrado.
        """
        if not instance(objeto=centimetros, classe=Centimetros):
            return False
        centimetros.comment = tira_espacos_inicio_final(word=centimetros.comment)
        dt = Data()
        dt.dia = centimetros.dia
        dt.mes = centimetros.mes
        dt.ano = centimetros.ano
        dc = DataCheck()
        if not dc.is_valid_data(data=dt):
            return False
        elif not centimetros.fk > 0:
            return False
        elif is_none_empty(word=centimetros.comment):
            return False
        elif not is_small_equal(word=centimetros.comment, size=50):
            return False
        elif is_int_positive(inter=centimetros.cintura):
            return False
        return True

    def read_Centimetros(self, sql='select * from tbCentimetros', **kwargs):
        """Realiza busca na base de dados.

        Args:
            sql (str): SQL query. Defaults to 'select * from tbPerson'
            kwargs (dict): valores.
        """
        keys = tuple(i for i in kwargs.keys())
        if keys:
            sql += ' where '
            for i in keys:
                sql += i + '=? '
            else:
                sql = tira_espacos_inicio_final(word=sql)
        return 'true'

    def delete_centimetros(self, centimetros) -> bool:
        """Deleta um derterminado registro de centimetros pelo id.

        Args:
            centimetros (Centimetros): Centimetros instance.

        Returns:
            bool: True se deletado.
        """
        if not instance(objeto=centimetros, classe=Centimetros):
            return False
        return False if not centimetros.id > 0 else True

    def delete_all(self, fk=0) -> bool:
        """Deleta todos os registros de uma pessoa.

        Args:
            fk (int, optional): chave estrangeira. Defaults to 0.

        Returns:
            bool: True se tudo deletado.
        """
        return False if not fk > 0 else True
