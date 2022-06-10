package main

import "fmt"

func main() {
	firstNumber := 234.345
	secondNumber := 45.698
	fmt.Printf("%.6f - %.6f\n", firstNumber, secondNumber)
	fmt.Printf("%.0f - %.0f\n", firstNumber, secondNumber)
	fmt.Printf("%.1f - %.1f\n", firstNumber, secondNumber)
	fmt.Printf("%.2f - %.2f\n", firstNumber, secondNumber)
	fmt.Printf("%.3f - %.3f\n", firstNumber, secondNumber)
	fmt.Printf("%e - %e\n", firstNumber, secondNumber)
	fmt.Printf("%E - %E\n", firstNumber, secondNumber)
	fmt.Printf("%.3f - %.3f\n", firstNumber, secondNumber)
	fmt.Printf("%.3f - %.3f\n", firstNumber, secondNumber)
}
