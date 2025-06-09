while True:
    n = input()
    if n == "0":
        break
    if int(n) % 42 == 0:
        print("PREMIADO")
    else:
        print("TENTE NOVAMENTE")
