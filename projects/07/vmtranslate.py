#
#
import logging
import argparse

logging.basicConfig(level=logging.WARNING)

class Parser:
    operation = None

    def __init__(self) -> None:
        self.operations = []

    def read_file(self, filename):
        with open(filename, "r") as f:
            for line in f.readlines():
                yield line

    def split_line(self, line):
        return line.strip().split(" ")

    def translate_operation(self, tokens):
        if not tokens:
            raise Exception("No tokens suppled")
        if tokens[0] in ["//", "\n", ""]:
            return None
        operation = Operation(tokens[0])
        if operation:
            for arg in tokens[1:]:
                operation.args.append(arg)
        logging.debug("tokens: %s", tokens)
        return operation

    def parse(self, filename):
        logging.info("Starting parsing")
        lines = self.read_file(filename)
        for line in lines:
            # print(f"  Looking at: {line}")
            tokens = self.split_line(line)
            operation = self.translate_operation(tokens)
            if operation:
                self.operations.append(operation)
        logging.info("Parsing complete")
        return self.operations


class Operation:
    command = None

    def __init__(self, command):
        self.command = command
        self.args = []

    def __repr__(self) -> str:
        return f"{self.command} --> {self.args}"


class CodeWriter:
    def write_code(self, filepath, program_name, code):
        logging.info("Number of ops in code: %s", len(code))
        program = []
        # Next steps: For each operation write out command and args in hack format
        for op in code:
            logging.debug(op)
            # Translate
            program.append(f"\r\n// {op}")
            if op.command == 'push':
                if op.args[0] == 'constant':
                    program.append(f"@{op.args[1]}")
                    program.append("D=A")
                continue
            # no-argument operations
            if op.command in ["lt", "gt", "add", "and", "eq", "sub", "neg", "or", "not", "end"]:
                program.append(op.command)
                continue
            # If this line gets hit, then you have missed something
            logging.error("Unhandled token: %s", op)
        # Write out
        with open(filepath + "/" + program_name + ".asm", "w") as f:
            f.write("\r\n".join(program))

operation_mappings = {
    "push": Operation("push"),
    "add": Operation("add"),
}

if __name__ == "__main__":
    parser = Parser()
    import sys
    if len(sys.argv) < 2:
        raise Exception("No file specified")

    input_file = sys.argv[1]
    filename = ".".join(input_file.split("/")[-1].split(".")[:-1])
    filepath = "/".join(input_file.split("/")[:-1])
    code = parser.parse(input_file)
    cwriter = CodeWriter()
    cwriter.write_code(filepath, filename, code)
