class Message:
    """Classe com todas as mensagens da aplicação.
    """

    def __init__(self) -> None:
        """Nova Messagem.
        """
        self._msg = ''

    def success(self, key: str) -> None:
        """Insere mensagem de sucesso.

        Args:
            key (str): chave para mensagem.
        """
        self.msg = self._messages_sucesso(key=key)

    def error(self, key: str) -> None:
        """Insere mensagem de sucesso.

        Args:
            key (str): chave para mensagem.
        """
        self.msg = self._messages_erro(key=key)

    def _messages_sucesso(self, key=''):
        """Retorna uma mensagem de sucesso

        Args:
            key (str, optional): Chave para busca. Defaults to ''.
        """
        info = {
            'person-cre': 'Sucesso: Pessoa Registrada.',
            'person-upd': 'Sucesso: Pessoa Atualizada.',
            'person-del': 'Sucesso: Pessoa Deletada.',
            'peso-cre': 'Sucesso: Peso Registrado',
            'peso-del': 'Sucesso: Peso Deletado',
            'peso-del-all': 'Sucesso: Pesos de Pessoa Deletados.',
            'cent-cre': 'Sucesso: Centimetros Registrado.',
            'cent-del': 'Sucesso: Centimetros Deletado',
            'cent-del-all': 'Sucesso: Centimentros de Pessoa Deletados.',
        }
        return info[key] if key in info.keys() else ''

    def _messages_erro(self, key=''):
        """Retorna a mensagem equivalente a chave enviada.

        Args:
            key (str, optional): chave. Defaults to ''.
        """
        info = {
            'instance': 'Erro: Intância Inválida.',
            'str-none-empty': 'Erro: String Nula ou Vazia.',
            'str-invalid-size': 'Erro: String com Tamanho Invalido.',
            'peso-invalid': 'Erro: Peso Inválido.',
            'altura-invalid': 'Erro: Altura Inválida.',
            'sexo-invalid': 'Erro: Sexo Inválido.',
            'nome-invalid': 'Erro: Nome Inválido.',
            'comment-invalid': 'Erro: Comentário Inválido.',
            'cent-invalid': 'Erro: Centimetros Inválido.',
            'id-invalid': 'Erro: ID Não Encontrado.',
            'fk-invalid': 'Erro: ID Origem Não Encontrado.',
            'person-error': 'Erro: Pessoa Não Registrada',
            'person-update': 'Erro: Pessoa Não Atualizada',
            'person-found': 'Erro: Pessoa Não Encontrada',
            'dont-delete': 'Erro: Registro Não Deletado',
            'erase': 'Erro: Registros Não Deletados.',
            'peso-found': 'Erro: Peso Não Encontrado',
            'peso-erro': 'Erro: Peso Não Registrado.',
            'cent-erro': 'Erro: Centimetros Não Registrados.',
            'cent-found': 'Erro: Centimetros Não Encontrados',
            'data-erro': 'Erro: Data Inválida.',
        }
        return info[key] if key in info.keys() else ''

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        self._msg = msg
