
class Parser(object):
    operation = None

    def __init__(self) -> None:
        self.operation = []

    def read_file(self, filname):
        pass

    def split_line(self, line):
        pass

    def translate_operation(self, tokens):
        pass


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