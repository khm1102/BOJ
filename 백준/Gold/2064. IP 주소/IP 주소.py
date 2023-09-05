def print_ip(ip):
    bit_mask = (1 << 8) - 1 << 24
    temp = 0
    order = 3
    result = ""

    for i in range(4):
        temp = ip & bit_mask

        for j in range(order, 0, -1):
            temp = temp >> 8

        result += str(temp)
        if i != 3:
            result += "."

        bit_mask = bit_mask >> 8
        order -= 1

    print(result)

if __name__ == "__main__":
    computer_num = int(input())
    computer_ips = []

    for i in range(computer_num):
        temp_str = input()
        temp_str += "."

        ip_num = 0
        start_idx = 0

        for idx in range(len(temp_str)):
            if temp_str[idx] == ".":
                sub = temp_str[start_idx:idx]
                ip_num = (ip_num << 8)
                temp_num = int(sub)
                ip_num += temp_num
                start_idx = idx + 1

        computer_ips.append(ip_num)

    network_ip, network_mask = 0, 0
    total_and = computer_ips[0]
    bit = 0
    is_broken = False

    for bit_order in range(31, -1, -1):
        bit = 1 << bit_order
        is_broken = False

        for idx in range(1, computer_num):
            if (computer_ips[0] & bit) != (computer_ips[idx] & bit):
                is_broken = True
                break

        if is_broken:
            break
        else:
            network_mask |= bit

    print_ip(computer_ips[0] & network_mask)
    print_ip(network_mask)
