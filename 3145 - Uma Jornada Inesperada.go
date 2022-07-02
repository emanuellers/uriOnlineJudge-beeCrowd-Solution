package main

import (
	"fmt"
)

func main() {
	var guests float64
	fmt.Scan(&guests)
	var kilometers float64
	fmt.Scan(&kilometers)
	fmt.Printf("%.2f\n", kilometers/(guests+2))
}
