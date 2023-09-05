package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func gcd(a, b int) bool {
	if a%b == 0 {
		return true
	} else if a-b < b {
		return !gcd(b, a-b)
	} else {
		return true
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	for {
		line, _ := reader.ReadString('\n')
		values := strings.Fields(line)

		a, _ := strconv.Atoi(values[0])
		b, _ := strconv.Atoi(values[1])

		if a == 0 {
			break
		} else if a < b {
			a, b = b, a
		}

		if gcd(a, b) {
			fmt.Println("A wins")
		} else {
			fmt.Println("B wins")
		}
	}
}
