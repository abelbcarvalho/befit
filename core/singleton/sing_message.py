from core.message.message import Message


class SingMessage:
    """Singleton Messages.
    """

    _instance = None

    def __init__(self) -> None:
        """Novo Messages Singleton.
        """
        pass

    @classmethod
    def messages(cls) -> Message:
        """Verifica se já existe Message ou instancia.

        Returns:
            Message: Message instance.
        """
        if not cls._instance:
            cls._instance = Message()
        return cls._instance
