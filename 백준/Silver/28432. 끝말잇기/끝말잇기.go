package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)

	S := make([]string, N)
	q := -1

	for i := 0; i < N; i++ {
		fmt.Scan(&S[i])
		if S[i] == "?" && q == -1 {
			q = i
		}
	}

	var M int
	fmt.Scan(&M)

	for i := 0; i < M; i++ {
		var a string
		fmt.Scan(&a)

		found := false
		for _, val := range S {
			if val == a {
				found = true
				break
			}
		}

		if found {
			continue
		}
		
		if (q == 0 || S[q-1][len(S[q-1])-1] == a[0]) && (q == N-1 || a[len(a)-1] == S[q+1][0]) {
			fmt.Println(a)
		}
	}
}
