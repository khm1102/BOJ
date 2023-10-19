package main

import (
	"fmt"
)

func main() {
	var d int64
	fmt.Scan(&d)

	powersOfTen := make([]int64, 18)
	powersOfTen[0] = 1
	for i := 1; i < 18; i++ {
		powersOfTen[i] = powersOfTen[i-1] * 10
	}

	for i := 2; i <= 18; i++ {
		halfLength := i / 2
		prefix := make([]int64, 0)
		suffix := make([]int64, 0)
		remaining := d

		for j := 0; j < halfLength; j++ {
			prefix = append(prefix, (powersOfTen[i-j-1]-powersOfTen[j])/powersOfTen[j])
		}

		for j := 0; j < halfLength; j++ {
			var a int64
			if remaining >= 0 {
				a = (10 - remaining%10) % 10
			} else {
				a = (-10 - remaining%10) % 10
			}
			suffix = append(suffix, a)
			remaining = (remaining - a*prefix[j]) / 10
		}

		if remaining == 0 {
			var result int64
			for j := 0; j < halfLength; j++ {
				if suffix[j] == 0 && j == 0 {
					result += powersOfTen[i-1] + powersOfTen[0]
				}
				if suffix[j] > 0 {
					result += powersOfTen[i-1-j] * suffix[j]
				}
				if suffix[j] < 0 {
					result -= powersOfTen[j] * suffix[j]
				}
			}
			fmt.Println(result)
			return
		}
	}
	fmt.Println("-1")
}
