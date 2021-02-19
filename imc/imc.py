class IMC:
    """Classe que calcula o indice de massa
    corporal.
    """

    def __init__(self) -> None:
        """Novo calculo IMC.
        """
        self._altura = 0.0
        self._peso = 0.0
        self._imc = 0.0

    def __str__(self) -> str:
        """Retorna a classificação do IMC.

        Returns:
            str: que nível de IMC.
        """
        # ------amarelo-----verde-------azul--------vermelho----reverter
        cor = ('\033[33m', '\033[32m', '\033[34m', '\033[31m', '\033[0m')
        the_imc = 'Classificação IMC\nAltura: {}\nPeso: {}\n'
        the_imc = the_imc.format(
            cor[0] + str(self.altura) + cor[4],
            cor[0] + str(self.peso) + cor[4]
        )
        the_imc += 'IMC Calculado: {}\nClassificação: {}'
        data = []
        data.append(cor[0] + str(
            '%.2f'%(self.imc)
        ) + cor[4])
        data.append(self._classifica())
        if 'Magreza' in data[1]:
            data[1] = cor[1] + data[1] + cor[4]
        elif 'Adequado' in data[1]:
            data[1] = cor[2] + data[1] + cor[4]
        elif 'Acima' in data[1] or 'Obesidade' in data[1]:
            data[1] = cor[3] + data[1] + cor[4]
        data = tuple(data)
        the_imc = the_imc.format(data[0], data[1])
        return the_imc

    def _classe(self, key='') -> str:
        """Pega o tipo de classificação.

        Args:
            key (str, optional): chave para o switch. Defaults to ''.

        Returns:
            str: tipo de classficação.
        """
        info = {
            'magro-3': 'Magreza Grau III',
            'magro-2': 'Magreza Grau II',
            'magro-1': 'Magreza Grau I',
            'adequado': 'Peso Ideal e Adequado',
            'pre-obeso': 'Acima do Peso',
            'obeso-1': 'Obesidade Grau I',
            'obeso-2': 'Obesidade Grau II',
            'obeso-3': 'Obesidade grau III',
        }
        return info[key] if key in info.keys() else ''

    def _classifica(self) -> str:
        """Verifica e retorna a classificação do imc.

        Returns:
            str: classificação do imc.
        """
        the_imc = ''
        if self.imc < 16:
            the_imc = self._classe('magro-3')
        elif 16 <= self.imc <= 16.9:
            the_imc = self._classe('magro-2')
        elif 17 <= self.imc <= 18.4:
            the_imc = self._classe('magro-1')
        elif 18.5 <= self.imc <= 24.9:
            the_imc = self._classe('adequado')
        elif 25 <= self.imc <= 29.9:
            the_imc = self._classe('pre-obeso')
        elif 30 <= self.imc <= 34.9:
            the_imc = self._classe('obeso-1')
        elif 35 <= self.imc <= 39.9:
            the_imc = self._classe('obeso-2')
        else:
            the_imc = self._classe('obeso-3')
        return the_imc

    def calc_imc(self):
        """Realiza o cálculo do IMC.
        """
        self.imc = self.peso / self.altura ** 2

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, altura: float) -> None:
        if not isinstance(altura, float):
            return None
        elif altura < 0:
            return None
        self._altura = altura

    @property
    def peso(self) -> float:
        return self._peso

    @peso.setter
    def peso(self, peso: float) -> None:
        if not isinstance(peso, float):
            return None
        elif peso < 0:
            return None
        self._peso = peso

    @property
    def imc(self):
        return self._imc

    @imc.setter
    def imc(self, imc: float):
        self._imc = imc
