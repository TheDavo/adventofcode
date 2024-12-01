package day01

import (
	"sort"
	"strconv"
	"strings"
)

func Part1(input string) int {
	leftList := []int{}
	rightList := []int{}
	for _, line := range strings.Split(input, "\n") {
		// strings.Fields skips whitespaces and returns a slice
		// of all the other content
		locationIds := strings.Fields(line)
		leftId, _ := strconv.Atoi(locationIds[0])
		rightId, _ := strconv.Atoi(locationIds[1])
		leftList = append(leftList, leftId)
		rightList = append(rightList, rightId)
	}
	sort.Ints(leftList)
	sort.Ints(rightList)
	distances := make([]int, len(leftList))
	for i := range leftList {
		distances[i] = leftList[i] - rightList[i]
		// math.Abs is a float64 function, so this is a
		// simple workaround to not typecast back and forth
		if distances[i] < 0 {
			distances[i] *= -1
		}
	}
	distanceTotal := 0
	for _, distance := range distances {
		distanceTotal += distance
	}
	return distanceTotal
}

func Part2(input string) int {
	leftMap := make(map[int]int)
	rightMap := make(map[int]int)
	lines := strings.Split(input, "\n")
	rightIds := make([]int, len(lines))
	for i, line := range lines {
		// strings.Fields skips whitespaces and returns a slice
		// of all the other content
		locations := strings.Fields(line)
		leftId, _ := strconv.Atoi(locations[0])
		rightId, _ := strconv.Atoi(locations[1])
		rightIds[i] = rightId

		if _, ok := leftMap[leftId]; !ok {
			leftMap[leftId] = 0
		}
		if _, ok := rightMap[rightId]; !ok {
			rightMap[rightId] = 0
		}
		leftMap[leftId]++
		rightMap[rightId]++
	}
	similarity := 0
	for id, countLeft := range leftMap {
		if countRight, ok := rightMap[id]; ok {
			similarity += id * countLeft * countRight

		}
	}
	return similarity
}
