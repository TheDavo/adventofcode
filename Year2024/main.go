package main

import (
	"aoc/days"
	"fmt"
	"os"
	"strings"
)

func main() {

	if len(os.Args) == 3 {
		day := os.Args[1]
		part := os.Args[2]
		funcToCall := fmt.Sprintf("%s_%s", day, part)

		dayPadded := padDay(day)
		if dayFunc, ok := days.DayFuncs[funcToCall]; ok {
			fp := fmt.Sprintf("./days/day%s/day%s_input.txt",
				dayPadded, dayPadded)

			fmt.Println("opening file for day",
				day, "part", part, "with filepath",
				fp)
			input, err := os.ReadFile(fp)
			if err != nil {
				panic(err)
			}

			funcInput := strings.Trim(string(input), " \r\n")
			fmt.Println("Result for day", day, "part",
				part, "is:", dayFunc(string(funcInput)))
		} else {
			fmt.Printf("Day %s and part %s not found",
				day, part)
		}
	} else {
		usage := `Usage of aoc is
aoc day part`
		fmt.Println(usage)
	}
}

func padDay(day string) string {
	if len(day) == 1 {
		return "0" + day
	}

	return day
}
