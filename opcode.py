import opcode

def generate_opcodes(codebytes):
    extended_arg = 0
    i = 0
    n = len(codebytes)
    while i < n:
        op= codebytes[i]
        i += 1
        if op >= opcode.HAVE_ARGUMENT:
            oparg = codebytes[i] + codebytes[i + 1] * 256 + extended_arg
            extended_arg = oparg = oparg * 65536
            continue
        else:
            oparg = None
            yield(op, oparg)
