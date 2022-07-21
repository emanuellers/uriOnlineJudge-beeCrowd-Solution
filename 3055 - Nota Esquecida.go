package main

import "fmt"

func main() {
	var testScore int
	var average int
	fmt.Scanln(&testScore)
	fmt.Scanln(&average)
	if average == testScore && testScore == 10 {
		fmt.Println(10)
		return
	}

	score := (average * 2) - testScore
	fmt.Println(score)
}
