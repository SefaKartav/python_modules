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
    def __init__(self):
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            flag = False
            for pc in self._processors:
                if pc.validate(item):
                    pc.ingest(item)
                    flag = True
                    break

            if not flag:
                print(f"DataStream error - Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data\n")

        for proc in self._processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            count = proc._rank_counter
            remaining = len(proc._queue)
            print(f"{name}: total {count} items processed, " 
                  f"remaining {remaining} on processor")





if __name__ == "__main__":
    testNumeric = NumericProcessor()

    print("=== Code Nexus - Data Stream ===\n")
    print("\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()
    print("Registering Numeric Processor")
    stream.register_processor(testNumeric)
    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]

    print(f"\nSend first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()
    print("\nRegistering other data processors")
    testText = TextProcessor()
    testLog = LogProcessor()
    stream.register_processor(testText)
    stream.register_processor(testLog)
    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()
    print("\nConsume some elements from the data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3): testNumeric.output()
    for _ in range(2): testText.output()
    for _ in range(1): testLog.output()

    stream.print_processors_stats()


    
