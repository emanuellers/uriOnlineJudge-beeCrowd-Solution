package main

import "fmt"

func main() {
	scores := "---------------------------------------"
	x := "x = 35"

	fmt.Println(scores)
	fmt.Printf("|%s%-31v|\n", x, "")
	fmt.Printf("|%-37v|\n", "")
	fmt.Printf("|%15v%s%-16v|\n", "", x, "")
	fmt.Printf("|%-37v|\n", "")
	fmt.Printf("|%31v%s|\n", "", x)
	fmt.Println(scores)
}
