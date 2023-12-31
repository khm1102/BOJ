package main

import (
	"fmt"
	"strings"
)

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func findPrime(n int) int {
	for !isPrime(n) {
		n--
	}
	return n
}

func lcs(a, b string) int {
	dp := make([]int, len(b)+1)
	for i := 0; i < len(a); i++ {
		prev := 0
		for j := 0; j < len(b); j++ {
			temp := dp[j+1]
			if a[i] == b[j] {
				dp[j+1] = prev + 1
			} else {
				dp[j+1] = max(dp[j+1], dp[j])
			}
			prev = temp
		}
	}
	return dp[len(b)]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func solve(oa, ob string, x, y rune) int {
	a := strings.ReplaceAll(oa, string(y), "")
	b := strings.ReplaceAll(ob, string(y), "")

	aidx := strings.IndexRune(a, x)
	bidx := strings.IndexRune(b, x)

	if aidx == -1 || bidx == -1 {
		return -1
	}

	rst := lcs(a[:aidx], b[:bidx]) + lcs(a[aidx:], b[bidx:])
	if rst < 2 {
		return -1
	}
	return findPrime(rst)
}

func main() {
	var oa, ob, x, y string
	fmt.Scanln(&oa)
	fmt.Scanln(&ob)
	fmt.Scanln(&x)
	fmt.Scanln(&y)

	result := solve(oa, ob, rune(x[0]), rune(y[0]))
	fmt.Println(result)
}

