from person.model.person import Person
from tools.general import instance, is_none_empty, is_small_equal
from tools.general import tira_espacos_inicio_final
from tools.general import is_int_positive, is_float_positive
from person.service.i_service_person import IServicePerson
from tools.data_check import DataCheck
from core.message.message import Message


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
        self._msg = Message()

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
            self._msg.error(key='instance')
            return False
        elif not self._dat.is_valid_data(data=person.data):
            self._msg.error(key='data-erro')
            return False
        elif is_none_empty(word=person.nome):
            self._msg.error(key='str-none-empty')
            return False
        elif is_none_empty(word=person.sexo):
            self._msg.error(key='str-none-empty')
            return False
        elif not is_small_equal(word=person.nome, size=70):
            self._msg.error(key='str-invalid-size')
            return False
        elif not is_float_positive(point=person.altura):
            self._msg.error(key='altura-invalid')
            return False
        elif not is_float_positive(point=person.peso_inicial):
            self._msg.error(key='peso-invalid')
            return False
        elif not is_int_positive(inter=person.cent_inicial):
            self._msg.error(key='cent-invalid')
            return False
        person.peso_atual = person.peso_inicial
        person.cent_atual = person.cent_inicial
        return True

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
        return 'true'

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
        person.nome = tira_espacos_inicio_final(word=person.nome)
        if not instance(objeto=person, classe=Person):
            self._msg.error(key='instance')
            return False
        elif not person.id > 0:
            self._msg.error(key='id-invalid')
            return False
        elif is_none_empty(word=person.nome):
            self._msg.error(key='str-none-empty')
            return False
        elif not is_small_equal(word=person.nome, size=70):
            self._msg.error(key='str-invalid-size')
            return False
        elif not is_float_positive(point=person.peso_atual):
            self._msg.error(key='peso-invalid')
            return False
        elif not is_int_positive(inter=person.cent_atual):
            self._msg.error(key='cent-invalid')
            return False
        return True

    def delete_person(self, person) -> bool:
        """Deleta uma pessoa.

        Args:
            person (Person): instancia de Person.

        Returns:
            bool: True se Person deletada.
        """
        if not instance(objeto=person, classe=Person):
            self._msg.error(key='instance')
            return False
        elif not person.id > 0:
            self._msg.error(key='id-invalid')
            return False
        return True
