from collections import deque

max_val = 10 ** 9
end = False
error_flag = False
order_list = []
order_num = []
deque = deque()
output = []

while True:
    order_list.clear()
    order_num.clear()
    
    while True:
        t = input().split()
        
        if t[0] == "QUIT":
            print("\n".join(output))
            exit(0)
        elif t[0] == "END":
            break
        
        if len(t) == 1:
            order_list.append(t[0])
        else:
            order_list.append(t[0])
            order_num.append(int(t[1]))
    
    n = int(input())
    
    for _ in range(n):
        error_flag = False
        deque.clear()
        tmp = int(input())
        deque.appendleft(tmp)
        
        def solve():
            order_num_cnt = 0
            
            for i in range(len(order_list)):
                order = order_list[i]
                
                if order == "NUM":
                    deque.append(order_num[order_num_cnt])
                    order_num_cnt += 1
                elif order == "POP":
                    if len(deque) == 0:
                        global error_flag
                        error_flag = True
                        break
                    deque.pop()
                elif order == "INV":
                    if len(deque) == 0:
                        error_flag = True
                        break
                    tmp = deque.pop()
                    tmp *= -1
                    deque.append(tmp)
                elif order == "DUP":
                    if len(deque) == 0:
                        error_flag = True
                        break
                    tmp = deque[-1]
                    deque.append(tmp)
                elif order == "SWP":
                    if len(deque) < 2:
                        error_flag = True
                        break
                    first = deque.pop()
                    second = deque.pop()
                    deque.append(first)
                    deque.append(second)
                elif order == "ADD":
                    if len(deque) < 2:
                        error_flag = True
                        break
                    first = deque.pop()
                    second = deque.pop()
                    total = first + second
                    if total > max_val or total < -max_val:
                        error_flag = True
                        break
                    deque.append(total)
                elif order == "SUB":
                    if len(deque) < 2:
                        error_flag = True
                        break
                    first = deque.pop()
                    second = deque.pop()
                    sub = second - first
                    if sub > max_val or sub < -max_val:
                        error_flag = True
                        break
                    deque.append(sub)
                elif order == "MUL":
                    if len(deque) < 2:
                        error_flag = True
                        break
                    first = deque.pop()
                    second = deque.pop()
                    mul = second * first
                    if mul > max_val or mul < -max_val:
                        error_flag = True
                        break
                    deque.append(mul)
                elif order == "DIV":
                    if len(deque) < 2:
                        error_flag = True
                        break
                    minus_cnt = 0
                    first = deque.pop()
                    second = deque.pop()
                    if first < 0:
                        minus_cnt += 1
                    if second < 0:
                        minus_cnt += 1
                    if first == 0:
                        error_flag = True
                        break
                    div = abs(second) // abs(first)
                    if minus_cnt == 1:
                        deque.append(div * -1)
                    else:
                        deque.append(div)
                elif order == "MOD":
                    if len(deque) < 2:
                        error_flag = True
                        break
                    first = deque.pop()
                    second = deque.pop()
                    if first == 0:
                        error_flag = True
                        break
                    mod = abs(second) % abs(first)
                    if second < 0:
                        mod *= -1
                    deque.append(mod)
        
        solve()
        
        if error_flag or len(deque) != 1:
            output.append("ERROR")
        else:
            output.append(str(deque.pop()))

    output.append("")

    _ = input()  # Reading an empty line

print("\n".join(output))
