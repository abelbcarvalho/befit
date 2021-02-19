from peso.service.i_service_peso import IServicePeso
from peso.model.peso import Peso
from core.data.data import Data
from tools.data_check import DataCheck
from tools.general import is_float_positive, is_none_empty, instance
from tools.general import is_small_equal, tira_espacos_inicio_final
from core.message.message import Message


class ServicePeso(IServicePeso):
    """Regra de Negócio para Peso.

    Args:
        IServicePeso (abstract): interface.
    """

    def __init__(self) -> None:
        """Novo service de Peso.
        """
        super().__init__()
        self._msg = Message()

    def create_peso(self, peso) -> bool:
        """Registra um novo peso.

        Args:
            peso (Peso): Peso instance.

        Returns:
            bool: True se peso registrado.
        """
        if not instance(objeto=peso, classe=Peso):
            self._msg.error(key='instance')
            return False
        peso.comment = tira_espacos_inicio_final(word=peso.comment)
        dt = Data()
        dt.dia = peso.dia
        dt.mes = peso.mes
        dt.ano = peso.ano
        dc = DataCheck()
        if not dc.is_valid_data(data=dt):
            self._msg.error(key='data-erro')
            return False
        elif not peso.fk > 0:
            self._msg.error(key='fk-invalid')
            return False
        elif is_none_empty(word=peso.comment):
            self._msg.error(key='str-none-empty')
            return False
        elif not is_small_equal(word=peso.comment, size=50):
            self._msg.error(key='str-invalid-size')
            return False
        elif not is_float_positive(point=peso.peso):
            self._msg.error(key='peso-invalid')
            return False
        return True

    def read_peso(self, sql='select * from tbPeso', **kwargs):
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

    def delete_peso(self, peso) -> bool:
        """Deleta um derterminado registro de peso pelo id.

        Args:
            peso (Peso): Peso instance.

        Returns:
            bool: True se deletado.
        """
        if not instance(objeto=peso, classe=peso):
            self._msg.error(key='instance')
            return False
        elif not peso.id > 0:
            self._msg.error(key='id-invalid')
            return False
        return True

    def delete_all_peso(self, fk=0) -> bool:
        """Deleta todos os registros de uma pessoa.

        Args:
            fk (int, optional): chave estrangeira. Defaults to 0.

        Returns:
            bool: True se tudo deletado.
        """
        if not fk > 0:
            self._msg.error(key='fk-invalid')
            return False
        return True
