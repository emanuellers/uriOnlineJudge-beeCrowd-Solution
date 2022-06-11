package main

import (
	"fmt"
)

func main() {
	var inputs int
	fmt.Scanln(&inputs)

	var number int
	for i := 0; i < inputs; i++ {
		fmt.Scanln(&number)
		total := 0
		for j := 1; j <= number; j++ {
			divisors := 0
			for x := 1; x <= j; x++ {
				if j%x == 0 {
					divisors += 1
				}
			}
			if j != 1 && divisors%2 == 0 {
				total += 1
			}
		}
		fmt.Println(total)
	}
}
