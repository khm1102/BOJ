// 어렵다
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)

	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())

	arr := make([]int, 100000)

	for i := 0; i < n; i++ {
		scanner.Scan()
		val, _ := strconv.Atoi(scanner.Text())
		arr[i] = val
	}

	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}

	ans := solve(n, arr, min)
	fmt.Println(ans)
}

func solve(n int, arr []int, minFunc func(int, int) int) int {
	ans, cnt := 0, 0

	for i := 0; i < n; i++ {
		if i+2 < n && arr[i+1] > arr[i+2] {
			cnt = minFunc(arr[i], arr[i+1]-arr[i+2])
			ans += 5 * cnt
			arr[i] -= cnt
			arr[i+1] -= cnt

			cnt2 := minFunc(arr[i], minFunc(arr[i+1], arr[i+2]))
			ans += 7 * cnt2
			arr[i] -= cnt2
			arr[i+1] -= cnt2
			arr[i+2] -= cnt2
		} else {
			cnt2 := minFunc(arr[i], minFunc(arr[i+1], arr[i+2]))
			ans += 7 * cnt2
			arr[i] -= cnt2
			arr[i+1] -= cnt2
			arr[i+2] -= cnt2

			cnt = minFunc(arr[i], arr[i+1])
			ans += 5 * cnt
			arr[i] -= cnt
			arr[i+1] -= cnt
		}

		ans += 3 * arr[i]
	}

	return ans
}
