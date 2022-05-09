class Parser(object):
    operation = None

    def __init__(self) -> None:
        self.operations = []

    def read_file(self, filename):
        with open(filename, "r") as f:
            yield f.readline()

    def split_line(self, line):
        return 

    def translate_operation(self, tokens):
        pass

    def parse(self, filename):
        print("Starting parsing")
        line = self.read_file(filename)
        while line:
            tokens = self.split_line()
            operation = self.translate_operation(tokens)
            self.operations.append(operation)
        print("Parsing complete")


class Operation(object):
    command = None
    arg1 = None
    arg2 = None


class CodeWriter(object):
    def write_code(self, code):
        raise NotImplementedError("Need to do this")


if __name__ == "__main__":
    parser = Parser()
    # TODO: Read from commandline
    code = parser.parse()
    cwriter = CodeWriter()
    cwriter.write_code(code)