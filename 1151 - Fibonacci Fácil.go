package main

import "fmt"

func main() {
	var number int
	fmt.Scanln(&number)
	x := 0
	z := 1
	y := 0
	for i := 0; i < number; i++ {
		if i != number-1 {
			fmt.Printf("%d ", x)
		} else {
			fmt.Printf("%d", x)
		}
		x = z
		z += y
		y = x
	}
	fmt.Print("\n")
}
