from abc import ABCMeta, abstractmethod


class IAbstractBreakpoint(metaclass=ABCMeta):

    def __init__(self, config, counter):
        pass

    @abstractmethod
    def return_run(self, lm, state):
        pass
