from sqlite3 import connect


class Connect:
    """Classe que abre e fecha
    conexão com banco de dados.
    """

    _conexao = None
    _cursor = None

    @classmethod
    def create_tables(cls):
        """Esse metodo verifica ou cria tabelas
        na base de dados.

        Returns:
            None: Sem Retorno.
        """
        sql = 'create table if not exists {} ('
        person = sql + 11 * '{},'
        person = person[:-1]
        person += ');'
        person = person.format(
            'tbPerson',
            'id integer not null primary key autoincrement',
            'nome varchar(70) not null',
            'sexo varchar(25) not null',
            'dia integer not null',
            'mes integer not null',
            'ano integer not null',
            'altura float not null',
            'peso_inicial float not null',
            'peso_atual float not null',
            'cent_inicial integer not null',
            'cent_atual integer not null'
        )
        peso = sql + 8 * '{},'
        peso = peso[:-1]
        peso += ');'
        peso = peso.format(
            'tbPeso',
            'id integer not null primary key autoincrement',
            'peso float not null',
            'comment varchar(70) not null',
            'dia integer not null',
            'mes integer not null',
            'ano integer not null',
            'id_person integer not null',
            'foreign key (id_person) references tbPerson(id)'
        )
        cent = sql + 8 * '{},'
        cent = cent[:-1]
        cent += ');'
        cent = cent.format(
            'tbCentimetros',
            'id integer not null primary key autoincrement',
            'centimetros integer not null',
            'comment varchar(70) not null',
            'dia integer not null',
            'mes integer not null',
            'ano integer not null',
            'id_person integer not null',
            'foreign key (id_person) references tbPerson(id)'
        )
        try:
            cls.open_connect()
            cls.open_cursor()
            cls.cursor().execute(person)
            cls.cursor().execute(peso)
            cls.cursor().execute(cent)
            cls.commit()
        except Exception:
            pass
        finally:
            cls.close_connect()

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
    def open_cursor(cls):
        """Cursor da conexão.

        Returns:
            Cursor: cursor da conexão.
        """
        cls._cursor = None if not cls.conexao() else cls.conexao().cursor()

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

    @classmethod
    def cursor(cls):
        return cls._cursor
