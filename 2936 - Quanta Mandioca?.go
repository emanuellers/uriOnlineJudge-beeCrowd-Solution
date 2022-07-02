package main

import (
	"fmt"
)

func main() {
	portionMap := map[int]int{
		0: 300,
		1: 1500,
		2: 600,
		3: 1000,
		4: 150,
	}
	total := 225
	for index := 0; index < 5; index++ {
		var portion int
		fmt.Scanln(&portion)
		total += portion * portionMap[index]
	}
	fmt.Println(total)
}
