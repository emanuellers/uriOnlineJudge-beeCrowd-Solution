package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var number string
	fmt.Scan(&number)
	strs := strings.Split(number, ".")

	firstValue, _ := strconv.Atoi(strs[1])
	secondValue, _ := strconv.Atoi(strs[0])
	fmt.Printf("%d.%d\n", firstValue, secondValue)
}
