package days

import (
	"aoc/days/day01"
	"aoc/days/day02"
)

type dayFunc func(string) int

var DayFuncs = map[string]dayFunc{
	"1_1": day01.Part1,
	"1_2": day01.Part2,
	"2_1": day02.Part1,
	"2_2": day02.Part2,
}
