from person.service.service_person import ServicePerson
from peso.service.service_peso import ServicePeso
from centimetros.service.service_centimetros import ServiceCentimetros


class Facade:
    """Fachada do projeto, tudo passa por aqui.
    """

    _serv_person = ServicePerson()
    _serv_peso = ServicePeso()
    _serv_cent = ServiceCentimetros()

    def __init__(self) -> None:
        """Nova Fachada.
        """
        pass

    # Person

    def create_person(self, person) -> bool:
        """Registrar Nova Pessoa.

        Args:
            person (Person): Instancia com
            atributos de pessoa.

        Returns:
            bool: True se a pessoa foi registrada.
        """
        return self._serv_person.create_person(person=person)

    def read_person(self, sql='select * from tbPerson', **kwargs):
        """Realiza busca na base de dados.

        Args:
            sql (str): SQL query. Defaults to 'select * from tbPerson'
            kwargs (dict): valores.
        """
        return self._serv_person.read_person(sql=sql, **kwargs)

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
        return self._serv_person.update_person(person=person)

    def delete_person(self, person) -> bool:
        """Deleta uma pessoa.

        Args:
            person (Person): instancia de Person.

        Returns:
            bool: True se Person deletada.
        """
        return self._serv_person.delete_person(person=person)

    # Peso

    def create_peso(self, peso) -> bool:
        """Registra um novo peso.

        Args:
            peso (Peso): Peso instance.

        Returns:
            bool: True se peso registrado.
        """
        return self._serv_peso.create_peso(peso=peso)

    def read_peso(self, sql='select * from tbPeso', **kwargs):
        """Realiza busca na base de dados.

        Args:
            sql (str): SQL query. Defaults to 'select * from tbPerson'
            kwargs (dict): valores.
        """
        return self._serv_peso.read_peso(sql=sql, **kwargs)

    def delete_peso(self, peso) -> bool:
        """Deleta um derterminado registro de peso pelo id.

        Args:
            peso (Peso): Peso instance.

        Returns:
            bool: True se deletado.
        """
        return self._serv_peso.delete_peso(peso=peso)

    def delete_all_peso(self, fk=0) -> bool:
        """Deleta todos os registros de uma pessoa.

        Args:
            fk (int, optional): chave estrangeira. Defaults to 0.

        Returns:
            bool: True se tudo deletado.
        """
        return self._serv_peso.delete_all_peso(fk=fk)

    # Centimetros

    def create_centimetros(self, centimetros) -> bool:
        """Registra novo Centimetros.

        Args:
            centimetros (Centimetros): Centimetros instance.

        Returns:
            bool: True se centimetros registrado.
        """
        return self._serv_cent.create_centimetros(centimetros=centimetros)

    def read_centimetros(self, sql='select * from tbCentimetros', **kwargs):
        """Realiza busca na base de dados.

        Args:
            sql (str): SQL query. Defaults to 'select * from tbPerson'
            kwargs (dict): valores.
        """
        return self._serv_cent.read_centimetros(sql=sql, **kwargs)

    def delete_centimetros(self, centimetros) -> bool:
        """Deleta um derterminado registro de centimetros pelo id.

        Args:
            centimetros (Centimetros): Centimetros instance.

        Returns:
            bool: True se deletado.
        """
        return self._serv_cent.delete_centimetros(centimetros=centimetros)

    def delete_all_centimetros(self, fk=0) -> bool:
        """Deleta todos os registros de uma pessoa.

        Args:
            fk (int, optional): chave estrangeira. Defaults to 0.

        Returns:
            bool: True se tudo deletado.
        """
        return self._serv_cent.delete_all_centimetros(fk=fk)
