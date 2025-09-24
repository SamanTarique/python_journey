class Temp:

    def __init__(self, temp):
        self._temp = temp

    @property
    def _temp(self):
        return self._temp

    @_temp.setter
    def _temp(self, temp):
        self._temp = temp

