package main

import "fmt"

func main() {
	scores := "---------------------------------------"
	fmt.Println(scores)
	fmt.Println("|  decimal  |  octal  |  Hexadecimal  |")
	fmt.Println(scores)
	for i := 0; i < 16; i++ {
		if i < 10 && i != 8 && i != 9 {
			fmt.Printf("|%6v%d%-4v|%4v%o%-4v|%7v%X%-7v|\n", "", i, "", "", i, "", "", i, "")
		} else if i >= 8 && i <= 9 {
			fmt.Printf("|%6v%d%-4v|%3v%o%-4v|%7v%X%-7v|\n", "", i, "", "", i, "", "", i, "")
		} else {
			fmt.Printf("|%5v%d%-4v|%3v%o%-4v|%7v%X%-7v|\n", "", i, "", "", i, "", "", i, "")
		}
	}
	fmt.Println(scores)
}
