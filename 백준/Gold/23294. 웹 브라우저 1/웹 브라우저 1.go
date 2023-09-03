package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const MAX = 2001

var cap [MAX]int

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)

	var n, q, c int
	scanner.Scan()
	n, _ = strconv.Atoi(scanner.Text())
	scanner.Scan()
	q, _ = strconv.Atoi(scanner.Text())
	scanner.Scan()
	c, _ = strconv.Atoi(scanner.Text())

	for i := 1; i <= n; i++ {
		scanner.Scan()
		cap[i], _ = strconv.Atoi(scanner.Text())
	}

	page := 0
	cache := 0
	back := make([]int, 0)
	front := make([]int, 0)

	for q > 0 {
		scanner.Scan()
		work := scanner.Text()

		switch work {
		case "B":
			if len(back) > 0 {
				front = append(front, page)
				page = back[len(back)-1]
				cache -= cap[page]
				back = back[:len(back)-1]
			}

		case "F":
			if len(front) > 0 {
				back = append(back, page)
				cache += cap[page]
				page = front[len(front)-1]
				front = front[:len(front)-1]
			}

		case "A":
			scanner.Scan()
			i, _ := strconv.Atoi(scanner.Text())

			front = front[:0]

			cache += cap[page]
			if page != 0 {
				back = append(back, page)
			}
			page = i

			for cache+cap[page] > c {
				cache -= cap[back[0]]
				back = back[1:]
			}

		case "C":
			if len(back) == 0 {
				break
			}

			tmp := make([]int, 0)
			tmp = append(tmp, back[0])
			cache = cap[back[0]]
			for i := 1; i < len(back); i++ {
				if back[i] != back[i-1] {
					tmp = append(tmp, back[i])
					cache += cap[back[i]]
				}
			}
			back = tmp
		}

		q--
	}

	fmt.Println(page)

	if len(back) > 0 {
		for i := len(back) - 1; i >= 0; i-- {
			fmt.Printf("%d ", back[i])
		}
		fmt.Println()
	} else {
		fmt.Println(-1)
	}

	if len(front) > 0 {
		for i := len(front) - 1; i >= 0; i-- {
			fmt.Printf("%d ", front[i])
		}
		fmt.Println()
	} else {
		fmt.Println(-1)
	}
}
