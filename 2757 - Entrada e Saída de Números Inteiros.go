package main

import (
	"fmt"
	"strconv"
)

func main() {
	var firstNumber string
	var array []string
	for i := 0; i < 3; i++ {
		fmt.Scanln(&firstNumber)
		array = append(array, firstNumber)
	}
	one, _ := strconv.Atoi(array[0])
	two, _ := strconv.Atoi(array[1])
	three, _ := strconv.Atoi(array[2])

	fmt.Printf("A = %d, B = %d, C = %d\n", one, two, three)
	fmt.Printf("A = %10v, B = %10v, C = %10v\n", one, two, three)
	fmt.Printf("A = %010d, B = %010d, C = %010d\n", one, two, three)
	fmt.Printf("A = %-10v, B = %-10v, C = %-10v\n", one, two, three)
}
