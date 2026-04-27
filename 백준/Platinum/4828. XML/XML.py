from re import compile

TOKEN = compile(
    r"<(?P<self>[a-z0-9]+)/>"
    r"|</(?P<close>[a-z0-9]+)>"
    r"|<(?P<open>[a-z0-9]+)>"
    r"|&(?:lt|gt|amp);"
    r"|&x(?P<hex>[0-9A-Fa-f]+);"
    r"|(?P<text>[^<>&]+)"
)

def parser(line):
    if not line:
        return True

    stack = []
    total = 0

    for i in TOKEN.finditer(line):
        total += len(i.group())
        d = i.lastgroup

        if d == "open":
            stack.append(i[d])
            
        elif d == "close":
            if not stack or stack[-1] != i[d]:
                return False
            stack.pop()
            
        elif d == "hex" and len(i[d]) % 2:
            return False
        
        elif d == "text" and not i[d].isascii():
            return False

    return total == len(line) and not stack

for i in open(0):
    print("valid" if parser(i.rstrip("\n")) else "invalid")
    