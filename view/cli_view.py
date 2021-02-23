from os import system
from person.model.person import Person
from core.singleton.sing_facade import SingFacade
from core.singleton.sing_message import SingMessage


class CliView:
    """Interface de Linha de Comando.
    """

    def __init__(self) -> None:
        """Nova interface de Linha de Comando.
        """
        self._choose = 0

    def main(self) -> None:
        """Onde tudo começa.
        """
        while True:
            self._first_desc()
            try:
                self.choose = int(
                    input(
                        self._color(key='red')+'>:Sua Escolha:> ' +
                        self._color(key='yellow')
                    )
                )
                if 2 < self.choose < 4:
                    ex = self._color(
                        key='red') + 'Você Escolheu Sair!!!' + self._color('default')
                    print(self._stars(color='default'))
                    print(ex)
                    print(self._stars(color='blue'))
                    ex = input('continue...')
                    quit()
                elif 1 < self.choose < 3:
                    self._person_manage()
                elif 0 < self.choose < 2:
                    self._create_person()
                else:
                    pass
            except ValueError:
                pass
            finally:
                print(self._color(key='default'), end='')

    def _first_desc(self) -> None:
        """Primeira parte.
        """
        self._clear()
        print(self._stars(color='blue'))
        print('Escolha Uma das Alternativas' + self._chars(char='|', times=20))
        print(self._stars(color='blue'))
        print(self._color('yellow')+'[1] ' +
              self._color('default')+'Registrar Pessoa')
        print(self._color('yellow')+'[2] ' +
              self._color('default')+'Gerenciar Pessoa')
        print(self._color('yellow')+'[3] ' +
              self._color('default')+'Sair da Aplicação')
        print(self._stars(color='green'))

    def _color(self, key='') -> str:
        """Escolha uma cor.
        - red;
        - green;
        - blue;
        - yellow;
        - grey;
        - default;

        Args:
            key (str, optional): nome da cor. Defaults to ''.

        Returns:
            str: codigo ansi.
        """
        color = {
            'red': '\033[31m',
            'green': '\033[32m',
            'blue': '\033[34m',
            'yellow': '\033[33m',
            'grey': '\033[37m',
            'default': '\033[0m'
        }
        return color[key] if key in color.keys() else ''

    def _chars(self, char='', times=0) -> str:
        """Retorna um caractere determinado número de vezes.

        Args:
            char (str, optional): caractere. Defaults to ''.
            times (int, optional): número de repetições. Defaults to 0.

        Returns:
            str: caracteres repetidos.
        """
        return char * times

    def _clear(self) -> None:
        """Limpa tela.
        """
        system('clear')

    def _stars(self, color='') -> str:
        """Retorna char * x 48.

        Args:
            color (str, optional): cor da estrela. Defaults to ''.

        Returns:
            str: 48 x estrela com cor enviada.
        """
        return self._color(key=color) + self._chars(char='*', times=48) + \
            self._color(key='default')

    @property
    def choose(self) -> int:
        return self._choose

    @choose.setter
    def choose(self, choose) -> None:
        self._choose = choose

    def _create_person(self) -> None:
        """Metodo para criar uma pessoa.
        """
        self._clear()
        print(self._stars(color='green'))
        print('Registrando Nova Pessoa' + self._chars(char='|', times=25))
        print(self._stars(color='green'))
        print('Registre Uma Pessoa!')
        print(self._stars(color='green'))
        person = Person()

        person.nome = input('Nome: '+self._color(key='yellow'))
        print(self._color(key='default'), end='')

        while True:
            try:
                print('Sexo:\n[1] Masculino\n[2] Feminino')
                a = int(input('Escolha: '+self._color(key='yellow')))
                if a == 1:
                    person.sexo = 'masculino'
                    break
                elif a == 2:
                    person.sexo = 'feminino'
                    break
            except ValueError:
                pass
            finally:
                print(self._color(key='default'), end='')

        print('Data de Nascimento')
        while True:
            try:
                person.data.dia = int(
                    input(self._color(key='default')+'Dia: '+self._color(key='yellow')))
                person.data.mes = int(
                    input(self._color(key='default')+'Mês: '+self._color(key='yellow')))
                person.data.ano = int(
                    input(self._color(key='default')+'Ano: '+self._color(key='yellow')))
                break
            except ValueError:
                pass

        # altura
        while True:
            try:
                f = self._color(key='default')
                f += 'Altura: '
                f += self._color(key='yellow')
                person.altura = float(input(f))
                if person.altura > 0:
                    break
            except ValueError:
                pass
            finally:
                print(self._color(key='default'), end='')

        # peso inicial
        while True:
            try:
                f = self._color(key='default')
                f += 'Peso Inicial: '
                f += self._color(key='yellow')
                person.peso_inicial = float(input(f))
                if person.peso_inicial > 0:
                    break
            except ValueError:
                pass
            finally:
                print(self._color(key='default'), end='')
        
        # centimetros iniciais
        while True:
            try:
                f = self._color(key='default')
                f += 'Cintura Inicial: '
                f += self._color(key='yellow')
                person.cent_inicial = int(input(f))
                if person.altura > 0:
                    break
            except ValueError:
                pass
            finally:
                print(self._color(key='default'), end='')
        SingFacade.facade().create_person(person=person)
        print(self._stars(color='grey'))
        a = SingMessage.messages().msg
        if 'Erro' in a:
            print(self._color(key='red')+a)
        else:
            print(self._color(key='blue')+a)
        print(self._stars(color='grey'))
        a = input('pause')

    def _person_manage(self) -> None:
        """Aqui é possível gerenciar uma pessoa
        que está a emagrecer.
        """
        self._clear()
        print(self._stars(color='red'))
        print('Gerenciando Pessoa' + self._chars(char='|', times=30))
        print(self._stars(color='red'))
        tc = self._color(key='yellow') + '[{}] ' + self._color(key='default')
        print(tc.format(1) + 'Lista de Pessoas')
        print(tc.format(2) + 'Gerenciar Peso')
        print(tc.format(3) + 'Gerenciar Centimetros')
        print(tc.format(4) + 'Calcular IMC')
        print(tc.format(5) + 'Voltar')
        while True:
            try:
                tc = ':>Sua Escolha:> ' + self._color(key='yellow')
                op = int(input(tc))
                if 4 < op < 6:
                    return self.main()
                elif 3 < op < 5:
                    pass
                elif 2 < op < 3:
                    pass
                elif 1 < op < 2:
                    pass
                elif 0 < op < 2:
                    self._list_all_persons()
                else:
                    pass
            except ValueError:
                pass
            finally:
                print(self._color(key='default'), end='')

    def _list_all_persons(self) -> None:
        """Lista de todas as pessoas registradas
        """
        self._clear()
        pers = SingFacade.facade().read_all_person()
        if not pers:
            print(self._color(key='red') + SingMessage.messages().msg)
            a = input(self._color(key='default') + 'pause')
            return self._person_manage()
        tc = self._color(key='blue') + '{}' + self._color(key='default')
        print(self._stars('yellow'))
        print('Listagem de Pessoas')
        print(self._stars('yellow'))
        for per in pers:
            print(tc.format('ID: '), per.id)
            print(tc.format('Nome: '), per.nome)
            print(tc.format('Sexo: '), per.sexo)
            print(tc.format('Data Nas: '), per.data)
            print(tc.format('Altura: '), per.altura)
            print(tc.format('Peso Inicial: '), per.peso_inicial)
            print(tc.format('Peso Atual: '), per.peso_atual)
            print(tc.format('Cintura Inicial: '), per.cent_inicial)
            print(tc.format('Cintura Atual: '), per.cent_atual)
            print(self._chars(char='-', times=48))
        per = input('Voltar...')
        self._person_manage()
