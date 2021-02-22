from core.connect.connect import Connect


class DAOBase(Connect):
    """Classe Base para o funcionamento dos DAOs.
    """

    def __init__(self) -> None:
        """Novo Base DAO.
        """
        super().__init__()
        Connect.create_tables()

    def create(self, sql='', *args) -> bool:
        """Insira na base de Dados.

        Args:
            sql (str, optional): sql query. Defaults to ''.

        Returns:
            bool: True if data inserted.
        """
        return self._create_update_delete(sql, *args)

    def read(self, sql='', *args):
        """Esse metodo faz busca dentro da base de dados.

        Args:
            sql (str, optional): sql query. Defaults to ''.
        """
        try:
            Connect.open_connect()
            Connect.cursor().execute(sql, args)
            return [i for i in Connect.cursor().fetchall()]
        except Exception:
            return None
        finally:
            Connect.close_connect()

    def update(self, sql='', *args):
        """Update na base de Dados.

        Args:
            sql (str, optional): sql query. Defaults to ''.
        """
        return self._create_update_delete(sql, *args)

    def delete(self, sql='', id=''):
        """Deletar registro.

        Args:
            sql (str, optional): SQL query. Defaults to ''.
            id (str, optional): ID para deleção. Defaults to ''.
        """
        return self._create_update_delete(sql, id)

    def _create_update_delete(self, sql='', *args):
        """Esse metodo economiza linhas, pois
        create, update e delete usam mesma
        lógica.

        Args:
            sql (str, optional): sql query. Defaults to ''.
        """
        try:
            Connect.open_connect()
            Connect.cursor().execute(sql, args)
            Connect.commit()
            return True
        except Exception:
            return False
        finally:
            Connect.close_connect()
