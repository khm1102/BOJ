package main

import (
    "fmt"
)

func main() {
    var n int
    fmt.Scan(&n)
    a := make([]int, n)
    for i := 0; i < n; i++ {
        fmt.Scan(&a[i])
    }
    s := 0
    for i := 0; i < n; i++ {
        s += a[i]
    }
    res := 0
    b := make([]int, n+1)
    for i := 0; i < n; i++ {
        a = append(a, a[i])
    }
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            b[j+1] = b[j] + a[i+j]
            if b[j+1] < 0 {
                res += (-b[j+1] + s - 1) / s
            }
        }
    }
    fmt.Println(res)
}
