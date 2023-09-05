package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)

	D := make([]int, 1001)
	D[1] = 1
	D[2] = 2

	for i := 3; i <= N; i++ {
		D[i] = (D[i-1] + D[i-2]) % 10007
	}
	fmt.Println(D[N])
}
