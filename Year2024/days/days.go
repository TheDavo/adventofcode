package days

import (
	"aoc/days/day01"
)

type dayFunc func(string) int

var DayFuncs = map[string]dayFunc{
	"1_1": day01.Part1,
	"1_2": day01.Part2,
}
