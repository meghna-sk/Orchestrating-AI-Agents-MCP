from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, name, stance):
        self.name = name
        self.stance = stance

    @abstractmethod
    def generate_response(self, message_history):
        pass
