package main

import "fmt"

func main() {
	for {
		var number int
		fmt.Scan(&number)
		if number == -1 {
			break
		}
		total := 0
		chargeTimes := 0
		for i := 0; i < number; i++ {
			var ticketPrice int
			fmt.Scan(&ticketPrice)
			total += ticketPrice
			if total%100 == 0 {
				chargeTimes++
			}
		}
		fmt.Println(chargeTimes)
	}
}
