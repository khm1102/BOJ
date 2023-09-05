def solve_n_queen(N):
    def backtrack(row, col_mask, left_diag_mask, right_diag_mask):
        nonlocal total_count

        if row == N:
            total_count += 1
            return

        available_positions = ~(col_mask | left_diag_mask | right_diag_mask) & ((1 << N) - 1)

        while available_positions:
            position = available_positions & -available_positions  
            available_positions ^= position  

            backtrack(row + 1, col_mask | position, (left_diag_mask | position) << 1, (right_diag_mask | position) >> 1)

    total_count = 0
    backtrack(0, 0, 0, 0)
    return total_count

if __name__ == "__main__":
    N = int(input())
    if 1 <= N < 15:
        result = solve_n_queen(N)
        print(result)
    else:
        print("N should be between 1 and 14 (inclusive).")
