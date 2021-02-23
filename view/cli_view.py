from datetime import datetime
from os import system
from peso.model.peso import Peso
from centimetros.model.centimetros import Centimetros
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
                elif 2 < op < 4:
                    self._geren_cent()
                    pass
                elif 1 < op < 3:
                    self._geren_peso()
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

    def _geren_peso(self) -> None:
        """Esse metodo gerencia o peso.
        """
        self._clear()
        print(self._stars(color='red'))
        print('Gerenciando Peso' + self._chars(char='|', times=32))
        print(self._stars(color='red'))
        persons = SingFacade.facade().read_all_person()
        if not persons:
            print(self._stars(color='red'))
            print(SingMessage.messages().msg)
            print(self._stars(color='red'))
            a = input('voltar...')
            return self._person_manage()
        print('Selecione uma Pessoa')
        print(self._chars(char='-', times=48))
        tc = self._color(key='yellow') + '[{}] ' + self._color(key='default')
        for i in range(persons.__len__() + 1):
            try:
                print(tc.format(i + 1) + persons[i].nome)
            except IndexError:
                print(tc.format(i + 1) + 'Voltar')
        else:
            tc = self._color(key='blue') + ':>Sua Escolha:> ' + \
                self._color(key='yellow')
            i += 1
        while True:
            try:
                op = int(input(tc))
                if 0 > op or op > i:
                    continue
                elif op == i:
                    return self._person_manage()
                persons = persons[op-1]
                break
            except ValueError:
                pass
            finally:
                print(self._color(key='default'), end='')
        tc = self._color(key='yellow') + \
            '[{}] ' + self._color(key='default')
        print(self._stars(color='yellow'))
        print('Escolha Entre:')
        print(':> ' + self._color(key='green') +
              persons.nome + self._color(key='default'))
        print(tc.format(1) + 'Atualizar Peso')
        print(tc.format(2) + 'Voltar')
        tc = self._color(key='blue') + ':>Sua Escolha:> ' + \
            self._color(key='yellow')
        while True:
            try:
                op = int(input(tc))
                if op == 2:
                    return self._geren_peso()
                elif op == 1:
                    break
            except ValueError:
                pass
            finally:
                print(self._color(key='default'), end='')
        print(self._stars(color='blue'))
        print(':> ' + self._color(key='red') +
              persons.nome + self._color(key='default'))
        tc = self._color(key='green') + ':>Peso Atual:> ' + \
            self._color(key='yellow')
        i = persons.peso_atual
        print(':>Antigo Peso:> ' + self._color('yellow') +
              str(i) + self._color(key='default'))
        while True:
            try:
                persons.peso_atual = float(input(tc))
                if persons.peso_atual > 0:
                    break
            except ValueError:
                pass
            finally:
                print(self._color(key='default'), end='')
        if not SingFacade.facade().update_person(person=persons):
            print(self._stars(color='red'))
            print(SingMessage.messages().msg)
            print(self._stars(color='red'))
            a = input('continue...')
            return self._person_manage()
        peso = Peso()
        peso.fk = persons.id
        peso.peso = persons.peso_atual - i
        tc = self._color(key='green') + ':>Comentário:> ' + \
            self._color('yellow')
        peso.comment = input(tc)
        peso.dia = datetime.now().day
        peso.mes = datetime.now().month
        peso.ano = datetime.now().year
        print(self._stars(color='default'))
        if SingFacade.facade().create_peso(peso=peso):
            tc = self._color('blue')
            tc += SingMessage.messages().msg
            tc += self._color('default')
            print(tc)
            print(self._stars(color='default'))
            a = input('continue...')
        else:
            tc = self._color('red')
            tc += SingMessage.messages().msg
            tc += self._color('default')
            print(tc)
            print(self._stars(color='default'))
            a = input('continue...')
        return self._geren_peso()

    def _geren_cent(self) -> None:
        """Esse metodo gerencia o peso.
        """
        self._clear()
        print(self._stars(color='blue'))
        print('Gerenciando Centimetros' + self._chars(char='|', times=25))
        print(self._stars(color='blue'))
        persons = SingFacade.facade().read_all_person()
        if not persons:
            print(self._stars(color='default'))
            print(SingMessage.messages().msg)
            print(self._stars(color='default'))
            a = input('voltar...')
            return self._person_manage()
        print('Selecione uma Pessoa')
        print(self._chars(char='-', times=48))
        tc = self._color(key='yellow') + '[{}] ' + self._color(key='default')
        for i in range(persons.__len__() + 1):
            try:
                print(tc.format(i + 1) + persons[i].nome)
            except IndexError:
                print(tc.format(i + 1) + 'Voltar')
        else:
            tc = self._color(key='red') + ':>Sua Escolha:> ' + \
                self._color(key='yellow')
            i += 1
        while True:
            try:
                op = int(input(tc))
                if 0 > op or op > i:
                    continue
                elif op == i:
                    return self._person_manage()
                persons = persons[op-1]
                break
            except ValueError:
                pass
            finally:
                print(self._color(key='default'), end='')
        tc = self._color(key='yellow') + \
            '[{}] ' + self._color(key='default')
        print(self._stars(color='yellow'))
        print('Escolha Entre:')
        print(':> ' + self._color(key='red') +
              persons.nome + self._color(key='default'))
        print(tc.format(1) + 'Atualizar Cintura')
        print(tc.format(2) + 'Voltar')
        tc = self._color(key='blue') + ':>Sua Escolha:> ' + \
            self._color(key='yellow')
        while True:
            try:
                op = int(input(tc))
                if op == 2:
                    return self._geren_cent()
                elif op == 1:
                    break
            except ValueError:
                pass
            finally:
                print(self._color(key='default'), end='')
        print(self._stars(color='green'))
        print(':> ' + self._color(key='red') +
              persons.nome + self._color(key='default'))
        tc = self._color(key='blue') + ':>Cintura Atual:> ' + \
            self._color(key='yellow')
        i = persons.cent_atual
        print(':>Antiga Cintura:> ' + self._color('yellow') +
              str(i) + self._color(key='default'))
        while True:
            try:
                persons.cent_atual = float(input(tc))
                if persons.peso_atual > 0:
                    break
            except ValueError:
                pass
            finally:
                print(self._color(key='default'), end='')
        if not SingFacade.facade().update_person(person=persons):
            print(self._stars(color='red'))
            print(SingMessage.messages().msg)
            print(self._stars(color='red'))
            a = input('continue...')
            return self._person_manage()
        cent = Centimetros()
        cent.fk = persons.id
        cent.cintura = persons.cent_atual - i
        tc = self._color(key='green') + ':>Comentário:> ' + \
            self._color('yellow')
        cent.comment = input(tc)
        cent.dia = datetime.now().day
        cent.mes = datetime.now().month
        cent.ano = datetime.now().year
        print(self._stars(color='default'))
        if SingFacade.facade().create_centimetros(centimetros=cent):
            tc = self._color('blue')
            tc += SingMessage.messages().msg
            tc += self._color('default')
            print(tc)
            print(self._stars(color='default'))
            a = input('continue...')
        else:
            tc = self._color('red')
            tc += SingMessage.messages().msg
            tc += self._color('default')
            print(tc)
            print(self._stars(color='default'))
            a = input('continue...')
        return self._geren_cent()
