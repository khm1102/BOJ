import sys
input = sys.stdin.readline

class Node:
    def __init__(self, start, size):
        self.start = start
        self.size = size
        self.next = None

class MemoryManager:
    def __init__(self, total_size):
        self.free_list = Node(1, total_size)
        self.vars = {}

    def allocate(self, var_name, size):
        prev = None
        curr = self.free_list

        while curr:
            if curr.size >= size:
                alloc_start = curr.start
                curr.start += size
                curr.size -= size

                if curr.size == 0:
                    if prev:
                        prev.next = curr.next
                    else:
                        self.free_list = curr.next

                self.vars[var_name] = (alloc_start, size)
                return alloc_start
            prev = curr
            curr = curr.next

        self.vars[var_name] = 0
        return 0

    def deallocate(self, var_name):
        if var_name not in self.vars or self.vars[var_name] == 0:
            return

        start, size = self.vars[var_name]
        new_node = Node(start, size)
        self.vars[var_name] = 0

        if not self.free_list or self.free_list.start > start:
            new_node.next = self.free_list
            self.free_list = new_node
        else:
            curr = self.free_list
            while curr.next and curr.next.start < start:
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node

        self.merge_free_blocks()

    def merge_free_blocks(self):
        curr = self.free_list
        while curr and curr.next:
            if curr.start + curr.size == curr.next.start:
                curr.size += curr.next.size
                curr.next = curr.next.next
            else:
                curr = curr.next

    def print_address(self, var_name):
        if var_name not in self.vars or self.vars[var_name] == 0:
            print(0)
        else:
            print(self.vars[var_name][0])


mem_manager = MemoryManager(100000)

for _ in range(int(input().strip())):
    line = input().strip()
    
    if '=' in line:
        var_name, cmd = line.split('=')
        size = int(cmd.split('(')[-1].rstrip(');'))
        mem_manager.allocate(var_name.strip(), size)
    elif line.startswith('print'):
        var_name = line.split('(')[-1].rstrip(');')
        mem_manager.print_address(var_name)
    elif line.startswith('free'):
        var_name = line.split('(')[-1].rstrip(');')
        mem_manager.deallocate(var_name)
