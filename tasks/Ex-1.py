class Signal_information:
    def __init__(self, signal_power: float, path: list):

        if not isinstance(signal_power, float):
            raise TypeError("The input for signal_power should be as float type")
        if not isinstance(path, list) or not all(isinstance(node, str) for node in path):
            raise TypeError("The input for path should be a list of strings")

        self._signal_power = signal_power
        self._noise_power = 0.0
        self._latency = 0.0
        self._path = path

    @property
    def signal_power(self):
        return self._signal_power
    @property
    def noise_power(self):
        return self._noise_power

    @property
    def latency(self):
        return self._latency

    @property
    def path(self):
        return self._path

    @signal_power.setter
    def signal_power(self, increment: float):
        if not isinstance(increment, float):
            raise TypeError("The input for signal_power should be as float type")
        else:
            self._signal_power += increment

    @noise_power.setter
    def noise_power(self, increment: float):
        if not isinstance(increment, float):
            raise TypeError("The input for noise_power should be as float type")
        else:
            self._noise_power += increment

    @latency.setter
    def latency(self, increment: float):
        if not isinstance(increment, float):
            raise TypeError("The input for latency should be as float type")
        else:
            self.latency += increment

    @path.setter
    def path(self, node: str):
        if not isinstance(node, str):
            raise TypeError("The input for node should be a string type")
        else:
            self._path.append(node)

signall = Signal_information(23., ['a','3'])


print(signall.signal_power)

signall.signal_power = 1.12

print(signall.latency)

