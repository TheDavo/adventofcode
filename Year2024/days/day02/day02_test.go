package day02

import (
	"testing"
)

func TestDay2(t *testing.T) {
	input := `7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9`

	wants := []int{2, 4}
	gots := []int{Part1(input), Part2(input)}

	for i := range wants {
		if wants[i] != gots[i] {
			t.Fatalf("test[%d] failed\nwant: %d, got %d",
				i, wants[i], gots[i])
		}
	}
}
