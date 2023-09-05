package main

import (
	"fmt"
	"math"
)

func main() {
	var S, P int
	fmt.Scan(&S, &P)

	if S == P {
		fmt.Println(1)
		return
	}

	if math.Pow(math.E, float64(S)/math.E) < float64(P) {
		fmt.Println(-1)
		return
	}

	var prv float64 = -1
	for i := 2; ; i++ {
		cur := math.Pow(float64(S)/float64(i), float64(i))
		if prv > cur {
			fmt.Println(-1)
			return
		}
		if cur >= float64(P) {
			fmt.Println(i)
			return
		}
		prv = cur
	}
}
