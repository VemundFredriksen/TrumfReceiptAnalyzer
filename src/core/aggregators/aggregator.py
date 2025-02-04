from typing import List
from abc import ABC, abstractmethod

class Aggregator[T](ABC):
    
    @abstractmethod
    def aggregate(t) -> List[T]:
        pass