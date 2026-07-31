import abc
import typing


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        print("CSV Output:")
        print(",".join([val for _, val in data]))


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        print("JSON Output:")
        items = [f'"item_{rank}": "{val}"' for rank, val in data]
        print("{" + ", ".join(items) + "}")


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
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
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return len(data) > 0 and all(isinstance(x, str) for x in data)

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
                formatted_log = (f"{item['log_level']}: "
                                 f"{item['log_message']}")
                self._queue += [(self._rank_counter, formatted_log)]
                self._rank_counter += 1
        else:
            formatted_log = (f"{data['log_level']}: "
                             f"{data['log_message']}")
            self._queue += [(self._rank_counter, formatted_log)]
            self._rank_counter += 1


class DataStream:
    def __init__(self) -> None:
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
                print(f"DataStream error - "
                      f"Can't process element in stream: {item}")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            extracted_data = []
            count = min(nb, len(proc._queue))
            if count > 0:
                for _ in range(count):
                    extracted_data.append(proc.output())
                plugin.process_output(extracted_data)

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
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("Registering Processors")
    testNumeric = NumericProcessor()
    testText = TextProcessor()
    testLog = LogProcessor()

    stream.register_processor(testNumeric)
    stream.register_processor(testText)
    stream.register_processor(testLog)

    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message':
          'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message':
          'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]

    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    csv_plugin = CSVPlugin()
    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, csv_plugin)
    stream.print_processors_stats()

    batch2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE', 'log_message':
          'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]

    print(f"Send another batch of data: {batch2}")
    stream.process_stream(batch2)
    stream.print_processors_stats()

    json_plugin = JSONPlugin()
    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, json_plugin)
    stream.print_processors_stats()
