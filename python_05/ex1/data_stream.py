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

    def ingest(self, data: int | float |
               list[int | float]) -> None:
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
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return len(data) > 0 and all(isinstance(x, str)
                                         for x in data)

        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Invalid text data provided")

        if isinstance(data, list):
            for item in data:
                self._queue += [(self._rank_counter, str(item))]
                self._rank_counter += 1

        else:
            self._queue += [(self._rank_counter, str(data))]
            self._rank_counter += 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return len(data) > 0 and all(isinstance(x, str)
                                         and isinstance(y, str)
                                         for x, y in data.items())

        if isinstance(data, list):
            if len(data) == 0:
                return False

            for item in data:
                if not isinstance(item, dict):
                    return False
                if not all(isinstance(x, str) and
                           isinstance(y, str)
                           for x, y in item.items()):
                    return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Invalid log data provided")

        if isinstance(data, list):
            for item in data:
                self._queue += [(self._rank_counter, str(item))]
                self._rank_counter += 1
        else:
            self._queue += [(self._rank_counter, str(data))]
            self._rank_counter += 1


class DataStream:
    



if __name__ == "__main__":
    testNumeric = NumericProcessor()
    testText = TextProcessor()
    testLog = LogProcessor()

    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")

    trying = testNumeric.validate(42)
    trying1 = testNumeric.validate("Hello")
    print(f"Trying to validate input '42': {trying}")
    print(f"Trying to validate input 'Hello': {trying1}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        testNumeric.ingest("foo")
    except Exception as e:
        print(f"Got exception: {e}")
    num_data = [1, 2, 3, 4]
    print(f"Processing data: {num_data}")
    testNumeric.ingest(num_data)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = testNumeric.output()

        print(f"Numeric value {rank}: {val}")

    print("\nTesting Text Processor...")
    trying2 = testText.validate(42)
    print(f"Trying to validate input '42: {trying2}'")
    text_data = ["Hello", "Nexus", "World"]
    testText.ingest(text_data)
    print(f"Processing data: {text_data}")
    print("Extracting 1 values...")
    rank, val = testText.output()
    print(f"Text value {rank}: {val}")

    print("\nTesting Log Processor...")
    trying3 = testLog.validate("Hello")
    print(f"Trying to validate input 'Hello': {trying3}")
    log_data = [{'log_level': 'NOTICE',
                'log_message': 'Connection to server'},
                {'log_level': 'ERROR',
                 'log_message': 'Unauthorized access!!'}]
    print(f"Processing data: {log_data}")
    testLog.ingest(log_data)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = testLog.output()
        print(f"Log entry {rank}: {val}")
