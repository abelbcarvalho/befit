from core.facade.facade import Facade


class SingFacade:
    """Singleton para Facade.
    """

    _instance = None

    def __init__(self) -> None:
        """Novo Singleton Facade.
        """
        pass

    @classmethod
    def facade(cls) -> Facade:
        """Verifica se existe Facade instanciado.

        Returns:
            Facade: A instancia de facade.
        """
        if not cls._instance:
            cls._instance = Facade()
        return cls._instance
