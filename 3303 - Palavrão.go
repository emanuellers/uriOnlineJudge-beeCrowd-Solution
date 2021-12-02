package main

import (
	"fmt"
)

func main() {
	var word string
	fmt.Scan(&word)

	booleanTest := len(word) >= 10

	if booleanTest {
		fmt.Println("palavrao")
	} else {
		fmt.Println("palavrinha")
	}

}
