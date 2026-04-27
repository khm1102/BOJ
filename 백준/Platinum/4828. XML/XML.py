def is_tag(c: str) -> bool:
    return "a" <= c <= "z" or "0" <= c <= "9"


def parser(line: str) -> bool:
    if not line:
        return True
    
    stack = []
    i = 0
    n = len(line)
    while i < n:
        c = line[i]
        if c == "<":
            j = i + 1
            while j < n and line[j] != ">":
                j += 1
                
            if j >= n:
                return False
            inner = line[i + 1:j]
            
            if not inner:
                return False
            
            if inner[0] == "/":
                tag = inner[1:]
                if not tag or not all(is_tag(c) for c in tag):
                    return False
                if not stack or stack[-1] != tag:
                    return False
                stack.pop()
            elif inner[-1] == "/":
                tag = inner[:-1]
                if not tag or not all(is_tag(c) for c in tag):
                    return False
            else:
                tag = inner
                if not all(is_tag(c) for c in tag):
                    return False
                stack.append(tag)
            i = j + 1
        elif c == "&":
            j = i + 1
            while j < n and line[j] != ";":
                if line[j] == "<" or line[j] == ">":
                    return False
                j += 1
            if j >= n:
                return False
            e = line[i + 1:j]

            if e in ("lt", "gt", "amp"):
                pass

            elif e and e[0] == "x":
                h = e[1:]
                if not h:
                    return False

                if len(h) % 2 != 0:
                    return False

                try:
                    int(h, 16)
                except Exception:
                    return False

            else:
                return False
            i = j + 1

        elif c == ">":
            return False

        else:
            i += 1

    return not stack


for i in open(0):
    print("valid" if parser(i.rstrip("\n")) else "invalid")
