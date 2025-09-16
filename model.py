
class ContadorModel:
    """
    El Modelo se encarga de los datos de la aplicación.
    No sabe nada sobre cómo se mostrarán estos datos.
    """
    def __init__(self):
        self._contador = 0

    @property
    def contador(self):
        """Devuelve el valor actual del contador."""
        return self._contador

    def incrementar(self):
        """Incrementa el contador en uno."""
        self._contador += 1