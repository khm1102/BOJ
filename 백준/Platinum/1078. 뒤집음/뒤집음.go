package main

import (
    "fmt"
)

func main() {
    var d int64
    fmt.Scan(&d)

    result := findSpecial(d)
    fmt.Println(result)
}

func findSpecial(d int64) int64 {
    powers := make([]int64, 18)
    powers[0] = 1
    for i := int64(1); i < 18; i++ {
        powers[i] = powers[i-1] * 10
    }

    for i := int64(2); i <= 18; i++ {
        half := i / 2
        pref := make([]int64, 0)
        suff := make([]int64, 0)
        remain := d

        for j := int64(0); j < half; j++ {
            pref = append(pref, (powers[i-j-1]-powers[j])/powers[j])
        }

        for j := int64(0); j < half; j++ {
            var a int64
            if remain >= 0 {
                a = (10 - remain%10) % 10
            } else {
                a = (-10 - remain%10) % 10
            }
            suff = append(suff, a)
            remain = (remain - a*pref[j]) / 10
        }

        if remain == 0 {
            var result int64
            for j := int64(0); j < half; j++ {
                if suff[j] == 0 && j == 0 {
                    result += powers[i-1] + powers[0]
                }
                if suff[j] > 0 {
                    result += powers[i-1-j] * suff[j]
                }
                if suff[j] < 0 {
                    result -= powers[j] * suff[j]
                }
            }
            return result
        }
    }
    return -1
}
