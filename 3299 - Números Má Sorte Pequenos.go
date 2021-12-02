package main

import (
	"fmt"
	"strings"
)

func main() {
	var number string
	fmt.Scan(&number)

	if strings.Contains(number, "13") {
		fmt.Println(number, "es de Mala Suerte")
	} else {
		fmt.Println(number, "NO es de Mala Suerte")
	}

}
