class Parser(object):
    operation = None

    def __init__(self) -> None:
        self.operations = []

    def read_file(self, filename):
        with open(filename, "r") as f:
            for line in f.readlines():
                yield line

    def split_line(self, line):
        return 

    def translate_operation(self, tokens):
        pass

    def parse(self, filename):
        print("Starting parsing")
        lines = self.read_file(filename)
        for line in lines:
            print(f"  Looking at: {line}")
            tokens = self.split_line(line)
            operation = self.translate_operation(tokens)
            self.operations.append(operation)
        print("Parsing complete")
        return self.operations


class Operation(object):
    command = None
    arg1 = None
    arg2 = None


class CodeWriter(object):
    def write_code(self, code):
        print(f"Number of ops in code: %s" % len(code))
        raise NotImplementedError("Need to do this")


if __name__ == "__main__":
    parser = Parser()
    # TODO: Read from commandline
    code = parser.parse("StackArithmetic/SimpleAdd/SimpleAdd.vm")
    cwriter = CodeWriter()
    cwriter.write_code(code)