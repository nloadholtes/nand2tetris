class Parser(object):
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
        operation = operation_mappings.get(tokens[0])
        if operation:
            for arg in tokens[1:]:
                operation.args.append(arg)
        print(f"tokens: {tokens}")
        return operation

    def parse(self, filename):
        print("Starting parsing")
        lines = self.read_file(filename)
        for line in lines:
            # print(f"  Looking at: {line}")
            tokens = self.split_line(line)
            operation = self.translate_operation(tokens)
            if operation:
                self.operations.append(operation)
        print("Parsing complete")
        return self.operations


class Operation(object):
    command = None
    args = []

    def __init__(self, command):
        self.command = command
    
    def __repr__(self) -> str:
        return f"{self.command} --> {self.args}"
 

class CodeWriter(object):
    def write_code(self, program_name, code):
        print(f"Number of ops in code: %s" % len(code))
        program = []
        # Next steps: For each operation write out command and args in hack format
        for op in code:
            print(op)
            # Translate 
        # Write out
        with open(program_name+".output", "w") as f:
            f.write("\n".join(program))

operation_mappings = {
    "push": Operation("push"),
    "add": Operation("add"),
}

if __name__ == "__main__":
    parser = Parser()
    # TODO: Read from commandline
    code = parser.parse("StackArithmetic/SimpleAdd/SimpleAdd.vm")
    cwriter = CodeWriter()
    cwriter.write_code("test_program", code)