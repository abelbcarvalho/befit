from peso.dao.i_dao_peso import IDAOPeso
from core.dao.dao_base import DAOBase


class DAOPeso(IDAOPeso):
    """DAO para Peso.

    Args:
        IDAOPeso: interface
    """

    def __init__(self) -> None:
        """Novo DAO Peso.
        """
        super().__init__()
        self._dao = DAOBase()

    def create_peso(self, peso) -> bool:
        """Registra um novo peso.

        Args:
            peso (Peso): Peso instance.

        Returns:
            bool: True se peso registrado.
        """
        sql = 'insert into tbPeso (id,peso,comment,dia,mes,'
        sql += 'ano,id_person) values (?,?,?,?,?,?,?)'
        return self._dao.create(
            sql,
            peso.peso,
            peso.comment,
            peso.dia,
            peso.mes,
            peso.ano,
            peso.fk,
        )

    def read_peso(self, sql='select * from tbPeso', **kwargs):
        """Realiza busca na base de dados.

        Args:
            sql (str): SQL query. Defaults to 'select * from tbPerson'
            kwargs (dict): valores.
        """
        val = tuple(i for i in kwargs.values())
        return self.read_person(sql, val)

    def delete_peso(self, peso) -> bool:
        """Deleta um derterminado registro de peso pelo id.

        Args:
            peso (Peso): Peso instance.

        Returns:
            bool: True se deletado.
        """
        sql = 'delete from tbPeso where id=?'
        return self._dao.delete(sql=sql, id=peso.id)

    def delete_all_peso(self, fk=0) -> bool:
        """Deleta todos os registros de uma pessoa.

        Args:
            fk (int, optional): chave estrangeira. Defaults to 0.

        Returns:
            bool: True se tudo deletado.
        """
        sql = 'delete from tbPeso where id_person=?'
        return self._dao.delete(sql=sql, id=fk)
