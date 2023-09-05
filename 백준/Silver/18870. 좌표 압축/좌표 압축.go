package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {

	reader := bufio.NewReader(os.Stdin)

	var N int
	fmt.Fscanln(reader, &N)


	line, _ := reader.ReadString('\n')
	line = strings.TrimSuffix(line, "\n")
	coords := strings.Fields(line)


	x := make([]int, N)
	for i, coord := range coords {
		x[i], _ = strconv.Atoi(coord)
	}

	sortedX := make([]int, N)
	copy(sortedX, x)
	sort.Ints(sortedX)


	compressedX := make([]int, N)
	compressedMap := make(map[int]int)

	for i, val := range sortedX {
		if i == 0 {
			compressedMap[val] = 0
		} else {
			if val != sortedX[i-1] {
				compressedMap[val] = compressedMap[sortedX[i-1]] + 1
			} else {
				compressedMap[val] = compressedMap[sortedX[i-1]]
			}
		}
	}


	for i, val := range x {
		compressedX[i] = compressedMap[val]
	}


	result := make([]string, N)
	for i, val := range compressedX {
		result[i] = strconv.Itoa(val)
	}
	fmt.Println(strings.Join(result, " "))
}
