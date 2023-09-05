package main

import (
	"fmt"
	"math"
)

func distance(x1, y1, x2, y2 int) float64 {
	return math.Sqrt(float64((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)))
}

func factorial(n int) int {
	v := 1
	for i := 1; i <= n; i++ {
		v *= i
	}
	return v
}

func main() {
	var N int
	fmt.Scan(&N) 

	pos := make([][2]int, N+1) 
	pos[0] = [2]int{0, 0}
	for i := 1; i <= N; i++ {
		var x, y int
		fmt.Scan(&x, &y)
		pos[i] = [2]int{x, y}
	}

	v := 0.0
	for i := 1; i < N; i++ {
		for j := i + 1; j <= N; j++ {
			v += distance(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
		}
	}

	fmt.Println((v * 2) / float64(N))
}
