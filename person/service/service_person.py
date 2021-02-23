from person.model.person import Person
from tools.general import instance, is_none_empty, is_small_equal
from tools.general import tira_espacos_inicio_final
from tools.general import is_int_positive, is_float_positive
from person.service.i_service_person import IServicePerson
from person.dao.dao_person import DAOPerson
from tools.data_check import DataCheck
from core.singleton.sing_message import SingMessage


class ServicePerson(IServicePerson):
    """Regra de Negócio para registro de Person.

    Args:
        IServicePerson (abstract): interface.
    """

    def __init__(self) -> None:
        """Novo Service de Person.
        """
        super().__init__()
        self._dat = DataCheck()
        self._dao = DAOPerson()

    def create_person(self, person) -> bool:
        """Registrar Nova Pessoa.

        Args:
            person (Person): Instancia com
            atributos de pessoa.

        Returns:
            bool: True se a pessoa foi registrada.
        """
        person.nome = tira_espacos_inicio_final(word=person.nome)
        person.sexo = tira_espacos_inicio_final(word=person.sexo)
        if not instance(objeto=person, classe=Person):
            SingMessage.messages().error(key='instance')
            return False
        elif not self._dat.is_valid_data(data=person.data):
            SingMessage.messages().error(key='data-erro')
            return False
        elif is_none_empty(word=person.nome):
            SingMessage.messages().error(key='str-none-empty')
            return False
        elif is_none_empty(word=person.sexo):
            SingMessage.messages().error(key='str-none-empty')
            return False
        elif not person.sexo.lower().__eq__('masculino')\
                and not person.sexo.lower().__eq__('feminino'):
            SingMessage.messages().error(key='sexo-invalid')
            return False
        elif not is_small_equal(word=person.nome, size=70):
            SingMessage.messages().error(key='str-invalid-size')
            return False
        elif not is_float_positive(point=person.altura):
            SingMessage.messages().error(key='altura-invalid')
            return False
        elif not is_float_positive(point=person.peso_inicial):
            SingMessage.messages().error(key='peso-invalid')
            return False
        elif not is_int_positive(inter=person.cent_inicial):
            SingMessage.messages().error(key='cent-invalid')
            return False
        person.peso_atual = person.peso_inicial
        person.cent_atual = person.cent_inicial
        if self._dao.create_person(person=person):
            SingMessage.messages().success(key='person-cre')
            return True
        else:
            SingMessage.messages().error(key='person-error')
            return False

    def read_person(self, sql='select * from tbPerson', **kwargs):
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
        data = self._dao.read_person(sql=sql, **kwargs)
        if not data:
            SingMessage.messages().error(key='person-found')
            return None
        else:
            persons = []
            for i in data:
                per = Person()
                per.id = i[0]
                per.nome = i[1]
                per.sexo = i[2]
                per.data.dia = i[3]
                per.data.mes = i[4]
                per.data.ano = i[5]
                per.altura = i[6]
                per.peso_inicial = i[7]
                per.peso_atual = i[8]
                per.cent_inicial = i[9]
                per.cent_atual = i[10]
                persons.append(per)
            return persons

    def update_person(self, person) -> bool:
        """Esse metódo irá atualizar informações de
        Person. Ele deverá atualizar:
        - nome;
        - altura;
        - peso atual;
        - centimetro atual;

        Args:
            person (Peson): Person instance.

        Returns:
            bool: True se atualizado.
        """
        person.nome = tira_espacos_inicio_final(word=person.nome)
        if not instance(objeto=person, classe=Person):
            SingMessage.messages().error(key='instance')
            return False
        elif not person.id > 0:
            SingMessage.messages().error(key='id-invalid')
            return False
        elif is_none_empty(word=person.nome):
            SingMessage.messages().error(key='str-none-empty')
            return False
        elif not is_float_positive(point=person.altura):
            SingMessage.messages().error(key='altura-invalid')
            return False
        elif not is_small_equal(word=person.nome, size=70):
            SingMessage.messages().error(key='str-invalid-size')
            return False
        elif not is_float_positive(point=person.peso_atual):
            SingMessage.messages().error(key='peso-invalid')
            return False
        elif not is_int_positive(inter=person.cent_atual):
            SingMessage.messages().error(key='cent-invalid')
            return False
        elif self._dao.update_person(person=person):
            SingMessage.messages().error(key='person-upd')
            return True
        else:
            SingMessage.messages().error(key='person-update')
            return False

    def delete_person(self, person) -> bool:
        """Deleta uma pessoa.

        Args:
            person (Person): instancia de Person.

        Returns:
            bool: True se Person deletada.
        """
        if not instance(objeto=person, classe=Person):
            SingMessage.messages().error(key='instance')
            return False
        elif not person.id > 0:
            SingMessage.messages().error(key='id-invalid')
            return False
        elif self._dao.delete_person(person=person):
            SingMessage.messages().success(key='person-del')
            return True
        else:
            SingMessage.messages().error(key='dont-delete')
            return False


    def read_all_person(self, sql='select * from tbPerson'):
        """Busca todas as pessoas.

        Args:
            sql (str, optional): sql query. Defaults to 'select * from tbPerson'.

        Returns:
            list: Person instances.
        """
        data = self._dao.read_all_person(sql=sql)
        if not data:
            SingMessage.messages().error(key='person-found')
            return None
        persons = []
        for i in data:
            per = Person()
            per.id = i[0]
            per.nome = i[1]
            per.sexo = i[2]
            per.data.dia = i[3]
            per.data.mes = i[4]
            per.data.ano = i[5]
            per.altura = i[6]
            per.peso_inicial = i[7]
            per.peso_atual = i[8]
            per.cent_inicial = i[9]
            per.cent_atual = i[10]
            persons.append(per)
        return persons
