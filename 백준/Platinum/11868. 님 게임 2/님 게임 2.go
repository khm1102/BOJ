package main
import (
	"fmt"
)
func main() {
	var n int
	fmt.Scan(&n)
	v := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Scan(&v[i])
	}

	res := v[0]
	for i := 1; i < n; i++ {
		res ^= v[i]
	}
	if res == 0 {fmt.Println("cubelover")}else {fmt.Println("koosaga")}
}