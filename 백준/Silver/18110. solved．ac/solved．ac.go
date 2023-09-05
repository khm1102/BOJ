package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
)

func round45(num float64) int {
	return int(num + math.Round(num-math.Floor(num)))
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())

	if n == 0 {
		fmt.Println(0)
	} else {
		nums := make([]int, n)
		for i := 0; i < n; i++ {
			scanner.Scan()
			num, _ := strconv.Atoi(scanner.Text())
			nums[i] = num
		}

		sort.Ints(nums)

		temp := round45(float64(n) * 0.15)
		if temp > 0 {
			nums = nums[temp : n-temp]
		}

		sum := 0
		for _, num := range nums {
			sum += num
		}

		fmt.Println(round45(float64(sum) / float64(n-temp*2)))
	}
}
