package day01

import (
	"testing"
)

func TestDay1(t *testing.T) {
	input := `3   4
4   3
2   5
1   3
3   9
3   3`

	wants := []int{11, 31}
	gots := []int{Part1(input), Part2(input)}

	for i := range wants {
		if wants[i] != gots[i] {
			t.Fatalf("test[%d] failed\nwant: %d, got %d",
				i, wants[i], gots[i])
		}
	}
}
