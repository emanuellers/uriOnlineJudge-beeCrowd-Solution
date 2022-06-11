package main

import (
	"fmt"
	"strconv"
)

func main() {
	var number string
	for {
		fmt.Scanln(&number)
		if number == "0" {
			break
		}

		value := 0
		for i := len(number); i >= 1; i-- {
			n, _ := strconv.Atoi(string(number[len(number)-i]))
			factorial := 1
			for x := i; x >= 1; x-- {
				factorial *= x
			}
			value += n * factorial
		}
		fmt.Println(value)
	}
}
