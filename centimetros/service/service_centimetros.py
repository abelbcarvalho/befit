from centimetros.service.i_service_centimetros import IServiceCentimetros
from centimetros.model.centimetros import Centimetros
from centimetros.dao.dao_centimetros import DAOCentimetros
from core.data.data import Data
from tools.data_check import DataCheck
from tools.general import is_int_positive, is_none_empty, instance
from tools.general import is_small_equal, tira_espacos_inicio_final
from core.singleton.sing_message import SingMessage


class ServiceCentimetros(IServiceCentimetros):
    """Regra de Negócio para Centimetros.

    Args:
        IServiceCentimetros (abstract): interface.
    """

    def __init__(self) -> None:
        """Novo service de Centimetros.
        """
        super().__init__()
        self._msg = SingMessage()
        self._dao = DAOCentimetros()

    def create_centimetros(self, centimetros) -> bool:
        """Registra novo Centimetros.

        Args:
            centimetros (Centimetros): Centimetros instance.

        Returns:
            bool: True se centimetros registrado.
        """
        if not instance(objeto=centimetros, classe=Centimetros):
            SingMessage.messages().error(key='instance')
            return False
        centimetros.comment = tira_espacos_inicio_final(word=centimetros.comment)
        dt = Data()
        dt.dia = centimetros.dia
        dt.mes = centimetros.mes
        dt.ano = centimetros.ano
        dc = DataCheck()
        if not dc.is_valid_data(data=dt):
            SingMessage.messages().error(key='data-erro')
            return False
        elif not centimetros.fk > 0:
            SingMessage.messages().error(key='fk-invalid')
            return False
        elif is_none_empty(word=centimetros.comment):
            SingMessage.messages().error(key='str-none-empty')
            return False
        elif not is_small_equal(word=centimetros.comment, size=50):
            SingMessage.messages().error(key='str-invalid-size')
            return False
        elif self._dao.create_centimetros(centimetros=centimetros):
            SingMessage.messages().success(key='cent-cre')
            return True
        else:
            SingMessage.messages().error(key='cent-erro')
            return False

    def read_centimetros(self, sql='select * from tbCentimetros', **kwargs):
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
        data = self._dao.read_centimetros(sql, **kwargs)
        if not data:
            SingMessage.messages().error(key='cent-found')
            return None
        else:
            cent = []
            for ce in data:
                cen = Centimetros()
                cen.id = ce[0]
                cen.cintura = ce[1]
                cen.comment = ce[2]
                cen.dia = ce[3]
                cen.mes = ce[4]
                cen.ano = ce[5]
                cen.fk = ce[6]
                cent.append(cen)
            return cent

    def delete_centimetros(self, centimetros) -> bool:
        """Deleta um derterminado registro de centimetros pelo id.

        Args:
            centimetros (Centimetros): Centimetros instance.

        Returns:
            bool: True se deletado.
        """
        if not instance(objeto=centimetros, classe=Centimetros):
            SingMessage.messages().error(key='instance')
            return False
        elif not centimetros.id > 0:
            SingMessage.messages().error(key='id-invalid')
            return False
        elif self._dao.delete_centimetros(centimetros=centimetros):
            SingMessage.messages().success(key='cent-del')
            return True
        else:
            SingMessage.messages().error(key='dont-delete')
            return False

    def delete_all_centimetros(self, fk=0) -> bool:
        """Deleta todos os registros de uma pessoa.

        Args:
            fk (int, optional): chave estrangeira. Defaults to 0.

        Returns:
            bool: True se tudo deletado.
        """
        if not fk > 0:
            SingMessage.messages().error(key='fk-invalid')
            return False
        elif self._dao.delete_all_centimetros(fk=fk):
            SingMessage.messages().success(key='cent-del-all')
            return True
        else:
            SingMessage.messages().error(key='erase')
            return False
