from sqlite3 import connect


class Connect:
    """Classe que abre e fecha
    conexão com banco de dados.
    """

    _conexao = None

    @classmethod
    def create_tables(cls):
        """Esse metodo verifica ou cria tabelas
        na base de dados.

        Returns:
            None: Sem Retorno.
        """
        sql = 'create table if not exists {} ('
        person = sql + 10 * '{}'
        person += ')'
        person = person.format(
            'tbPerson',
            'id int not null primary key autoincrement',
            'nome varchar(70) not null',
            'sexo varchar(25) not null',
            'dia int not null',
            'mes int not null',
            'ano int not null',
            'peso_inicial float not null',
            'peso_atual float not null',
            'cent_inicial int not null',
            'cent_atual int not null'
        )
        peso = sql + 5 * '{}'
        peso += ')'
        peso = peso.format(
            'tbPeso',
            'id int not null primary key autoincrement',
            'peso float not null',
            'comment varchar(70) not null',
            'dia int not null',
            'mes int not null',
            'ano int not null',
            'id_person int not null',
            'foreign key (id_person) references tbPerson(id)'
        )
        cent = sql + 5 * '{}'
        cent += ')'
        cent = cent.format(
            'tbCentimetros',
            'id int not null primary key autoincrement',
            'centimetros int not null',
            'comment varchar(70) not null',
            'dia int not null',
            'mes int not null',
            'ano int not null',
            'id_person int not null',
            'foreign key (id_person) references tbPerson(id)'
        )
        try:
            Connect.open_connect()
            Connect.cursor().execute(person)
            Connect.cursor().execute(peso)
            Connect.cursor().execute(cent)
        except Exception:
            pass
        finally:
            Connect.close_connect()

    @classmethod
    def open_connect(cls):
        """Abre Conexão com base de Dados.

        Returns:
            connect: conexão.
        """
        if cls.conexao():
            return None
        else:
            cls._conexao = connect('database/befit.db')

    @classmethod
    def close_connect(cls):
        """Fecha a conexao.

        Returns:
            None: Sem retorno.
        """
        if not cls.conexao():
            return None
        cls.conexao().close()
        cls._conexao = None

    @classmethod
    def cursor(cls):
        """Cursor da conexão.

        Returns:
            Cursor: cursor da conexão.
        """
        return None if not cls.conexao() else cls.conexao().cursor()

    @classmethod
    def commit(cls):
        """Oficializa a operação.

        Returns:
            None: Sem Retorno
        """
        if not cls.conexao():
            return None
        cls.conexao().commit()

    @classmethod
    def conexao(cls):
        return cls._conexao
