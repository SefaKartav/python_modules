import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self):
        self._queue: list[tuple[int, str]] = []
        self._rank_counter: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._queue:
            raise Exception("No data found to extract.")
        return self._queue.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, bool):
            return False

        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            return all(isinstance(x, (int, float))
                       and not isinstance(x, bool) for x in data)

        return False


    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
 
        if isinstance(data, list):
            for item in data:
                self._queue += [(self._rank_counter, str(item))]
                self._rank_counter += 1
    
        else:
            self._queue += [(self._rank_counter, str(data))]
            self._rank_counter += 1
                

class TextProcessor(DataProcessor):

