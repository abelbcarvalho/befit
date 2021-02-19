from centimetros.dao.i_dao_centimetros import IDAOCentimetros
from core.dao.dao_base import DAOBase


class DAOCentimetros(IDAOCentimetros):
    """DAO para Centimetros.

    Args:
        IDAOcentimetros: interface
    """

    def __init__(self) -> None:
        """Novo DAO Centimetros.
        """
        super().__init__()
        self._dao = DAOBase()

    def create_centimetros(self, centimetros) -> bool:
        """Registra um novo Centimetros.

        Args:
            centimetros (Centimetros): Centimetros instance.

        Returns:
            bool: True se Centimetros registrado.
        """
        sql = 'insert into tbCentimetros (id,centimetros,comment,dia,mes,'
        sql += 'ano,id_person) values (?,?,?,?,?,?,?)'
        return self._dao.create(
            sql,
            centimetros.centimetros,
            centimetros.comment,
            centimetros.dia,
            centimetros.mes,
            centimetros.ano,
            centimetros.fk,
        )

    def read_centimetros(self, sql='select * from tbCentimetros', **kwargs):
        """Realiza busca na base de dados.

        Args:
            sql (str): SQL query. Defaults to 'select * from tbCentimetros'
            kwargs (dict): valores.
        """
        val = tuple(i for i in kwargs.values())
        return self._dao.read(sql, val)

    def delete_centimetros(self, centimetros) -> bool:
        """Deleta um derterminado registro de Centimetros pelo id.

        Args:
            centimetros (Centimetros): Centimetros instance.

        Returns:
            bool: True se deletado.
        """
        sql = 'delete from tbCentimetros where id=?'
        return self._dao.delete(sql=sql, id=centimetros.id)

    def delete_all_centimetros(self, fk=0) -> bool:
        """Deleta todos os registros de uma pessoa.

        Args:
            fk (int, optional): chave estrangeira. Defaults to 0.

        Returns:
            bool: True se tudo deletado.
        """
        sql = 'delete from tbCentimetros where id_person=?'
        return self._dao.delete(sql=sql, id=fk)
