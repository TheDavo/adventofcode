package day02

import (
	"strconv"
	"strings"
)

func Part1(input string) int {
	var safeReports int
	for _, line := range strings.Split(input, "\n") {

		report := strings.Fields(line)
		intReport := make([]int, len(report))
		for i, level := range report {
			intReport[i], _ = strconv.Atoi(level)
		}

		if isReportSafe(intReport) {
			safeReports++
		}

	}
	return safeReports
}

func Part2(input string) int {
	var safeReports int
	for _, line := range strings.Split(input, "\n") {

		report := strings.Fields(line)
		intReport := make([]int, len(report))
		for i, level := range report {
			intReport[i], _ = strconv.Atoi(level)
		}

		if isReportSafe(intReport) {
			safeReports++
		} else {
			// not a safe report by default, let's check if removing a value
			// can create a good report
			for i := range intReport {
				modifiedReport := removeFromReport(intReport, i)
				if isReportSafe(modifiedReport) {
					safeReports++
					break
				}
			}
		}

	}
	return safeReports
}

// isReportSafe returns whether a report is safe from the readings
// of the Red-Nosed reactor
// A report is safe if:
//  1. The levels are either all increasing or decreasing
//  2. Any two adjacent levels differ by at least one and at most
//     three
func isReportSafe(report []int) bool {
	// handle a report of length 2
	if len(report) == 2 {
		diffReport := report[0] - report[1]
		if diffReport < 0 {
			diffReport *= -1
		}
		if diffReport >= 1 && diffReport <= 3 {
			return true
		}
		return false
	}
	increasing := report[0] < report[1]
	for i := 0; i < len(report)-1; i++ {
		j := i + 1
		// check monotonacity
		if increasing && report[i] > report[j] {
			return false
		}
		if !increasing && report[i] < report[j] {
			return false
		}
		diffReport := report[i] - report[j]
		if diffReport < 0 {
			diffReport *= -1
		}
		if !(diffReport >= 1 && diffReport <= 3) {
			return false
		}
	}
	return true
}

// removeFromReport returns a report with a specified element removed
// returns a new slice
// WARNING: does not perform bounds checking or error checking
func removeFromReport(report []int, index int) []int {
	removed := make([]int, len(report)-1)
	removedIdx := 0
	for i, val := range report {
		if i != index {
			removed[removedIdx] = val
			removedIdx++
		}
	}

	return removed
}
