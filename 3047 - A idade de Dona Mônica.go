package main

import "fmt"

func main() {
	var motherAge int
	var son1Age int
	var son2Age int
	fmt.Scanln(&motherAge)
	fmt.Scanln(&son1Age)
	max := son1Age
	fmt.Scanln(&son2Age)
	if son2Age > max {
		max = son2Age
	}
	son3Age := motherAge - (son1Age + son2Age)
	if son3Age > max {
		max = son3Age
	}
	fmt.Printf("%d\n", max)
}
