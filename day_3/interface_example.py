from abc import ABC, abstractmethod


class interface_sample(ABC):
    @abstractmethod
    def sample_method(self, variable_1, variable_2):
        pass


class implementation(interface_sample):
    def __init__(self):
        pass

    def sample_method(self):
        pass


imp = implementation()
