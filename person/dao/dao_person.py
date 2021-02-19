from core.dao.dao_base import DAOBase
from person.dao.i_dao_person import IDAOPerson
from person.model.person import Person
from core.singleton.sing_message import SingMessage


class DAOPerson(IDAOPerson):
    """DAO para person.

    Args:
        IDAOPerson (abstract): interface.
    """

    def __init__(self) -> None:
        """DAO para Person.
        """
        super().__init__()
        self._dao = DAOBase()

    def create_person(self, person) -> bool:
        """Registrar Nova Pessoa.

        Args:
            person (Person): Instancia com
            atributos de pessoa.

        Returns:
            bool: True se a pessoa foi registrada.
        """
        sql = 'insert into tbPerson ('
        sql += 'id,nome,sexo,dia,mes,ano,peso_inicial,'
        sql += 'peso_atual,cent_inicial,cent_atual) values ('
        sql += 10 * '?,'
        sql += ')'
        return self._dao.create(
            sql,
            person.id, person.nome,
            person.sexo, person.data.dia,
            person.data.mes, person.data.ano,
            person.peso_inicial, person.peso_atual,
            person.cent_inicial, person.cent_atual,
        )

    def read_person(self, sql='select * from tbPerson', **kwargs):
        """Realiza busca na base de dados.

        Args:
            sql (str): SQL query. Defaults to 'select * from tbPerson'
            kwargs (dict): valores.
        """
        val = tuple(i for i in kwargs.values())
        return self.read_person(sql, val)

    def update_person(self, person) -> bool:
        """Esse metódo irá atualizar informações de
        Person. Ele deverá atualizar:
        - nome;
        - peso atual;
        - centimetro atual;

        Args:
            person (Peson): Person instance.

        Returns:
            bool: True se atualizado.
        """
        sql = 'update tbPerson set nome=?, peso_atual=?, cent_atual=? where id=?'
        return self._dao.update(
            sql,
            person.nome,
            person.peso_atual,
            person.cent_atual,
            person.id,
        )

    def delete_person(self, person) -> bool:
        """Deleta uma pessoa.

        Args:
            person (Person): instancia de Person.

        Returns:
            bool: True se Person deletada.
        """
        sql = 'delete from tbPerson where id=?'
        return self._dao.delete(sql=sql, id=person.id)
