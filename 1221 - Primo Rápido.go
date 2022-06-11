package main

import (
	"fmt"
	"math"
)

func isPrime(number float64) bool {
	if int(number) == 1 {
		return false
	}
	squareRoot := int(math.Sqrt(number))
	for i := 2; i <= squareRoot; i++ {
		if int(number)%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	var inputs int
	fmt.Scanln(&inputs)

	var number float64
	for i := 0; i < inputs; i++ {
		fmt.Scanln(&number)
		if isPrime(number) {
			fmt.Println("Prime")
		} else {
			fmt.Println("Not Prime")
		}
	}
}
