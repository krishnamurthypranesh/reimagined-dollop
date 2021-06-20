package main

import (
	"fmt"
	"math"
)

// problem: Subarray Division
func birthday(s []int32, d int32, m int32) int32 {
	var (
		i       int32 = 0
		j       int32 = 0
		counter int32 = 0
	)

	if m == 1 && d == s[0] {
		return int32(1)
	}

	for int(i) < len(s)-1 {
		j = i + 1
		for j-i < m && int(j) < len(s) {
			fmt.Printf("inner loop s[%v],s[%v]=%v,%v\n", i, j, s[i], s[j])
			sum := int32(0)
			for k := i; k <= j; k++ {
				sum += s[k]
			}
			if sum == d && j-i+1 == m {
				fmt.Println("Incrementing counter")
				counter++
			}
			j++
		}
		i++
	}
	return counter
}

func dayOfTheProgrammer(year int32) string {
	// if the year is 1918, then do something
	// for all other years:
	// check if julian or gregorian
	// check leap year
	// return value

	if year == 1918 {
		return "it's 1918"
	} else if year < 1918 {
		if year%4 == 0 {
			return fmt.Sprintf("12-09-%v", year)
		} else {
			return fmt.Sprintf("13-09-%v", year)
		}
	} else {
		if year%4 != 0 {
			return fmt.Sprintf("13-09-%v", year)
		} else {
			if year%100 != 0 {
				return fmt.Sprintf("12-09-%v", year)
			} else if year%400 != 0 {
				return fmt.Sprintf("13-09-%v", year)
			}
		}
	}
	return ""
}

// problem: Drawing Book
func pageCount(n, p int32) int32 {
	var (
		book       [][]int32
		pages      []int32
		page       int32
		tupleCount int32
		i          int32 = 0
		finalPage  int32
		fromFront  int32
		fromBack   int32
	)

	for i <= n {
		if i == p {
			page = tupleCount
		}

		if i == n {
			finalPage = tupleCount
		}

		pages = append(pages, i)
		if len(pages) == 2 {
			book = append(book, pages)
			tupleCount++
			pages = make([]int32, 0)
		}

		i++
	}

	fromFront = page - 0
	fromBack = finalPage - page

	if fromBack < fromFront {
		return fromBack
	}
	return fromFront
}

// problem: magic square
func formingMagicSquare(s [][]int32) int32 {
	// var (
	// 	threeTuples [][]int32
	// 	highestSum  int32
	// 	i           int32
	// 	j           int32
	// )

	// for i < 3 {
	// 	for j < 3 {
	// 	}
	// }
	return int32(0)
}

// electronics shop
func getMoneySpent(keyboards []int32, drives []int32, b int32) int32 {
	var (
		maxSpend int32 = -1
	)
	for _, kb := range keyboards {
		for _, d := range drives {
			if kb+d <= b && kb+d > maxSpend {
				maxSpend = kb + d
			}
		}
	}
	return maxSpend
}

func abs(x int32) int32 {
	if x < 0 {
		return -x
	}
	return x
}

// cats and a mouse
func catAndMouse(x int32, y int32, z int32) string {
	if abs(z-x) < abs(z-y) {
		return "Cat A"
	} else if abs(z-y) < abs(z-x) {
		return "Cat B"
	} else {
		return "Mouse C"
	}
	return ""
}

func climbingLeaderboard(ranked []int32, player []int32) []int32 {
	// remove duplicates from the list
	// for each score of the player, find out what the rankings will be
	// will the lists be sorted? Assume yes
	var (
		newRanked []int32
		ranks     []int32
		i         int32
		highest   int32 = 0
		lowest    int32 = 9999999
	)

	// removing duplicates

	ranksMap := make(map[int32]int32)

	// remove duplicates while maintaining ordering
	i = 1
	for _, score := range ranked {
		if _, ok := ranksMap[score]; !ok {
			ranksMap[score] = i
			newRanked = append(newRanked, score)
			if score > highest {
				highest = score
			} else if score < lowest {
				lowest = score
			}
			i++
		}
	}

	fmt.Printf("%v, %d, %d\n", newRanked, highest, lowest)

	for _, p := range player {
		i = 1
		if p > highest {
			i = 1
		} else if p < lowest {
			i = ranksMap[lowest] + 1
		} else if v, ok := ranksMap[p]; ok {
			i = v
		} else {
			j := 1
			for j < len(newRanked)-2 {
				if p > newRanked[j] {
					i = int32(j)
					break
				}
				j++
			}
		}
		ranks = append(ranks, i)
	}

	return ranks
}

func climbingLeaderboardOrig(ranked []int32, player []int32) []int32 {
	// remove duplicates from the list
	// for each score of the player, find out what the rankings will be
	// will the lists be sorted? Assume yes
	var (
		newRanked []int32
		ranks     []int32
		i         int32
	)

	// removing duplicates

	ranksMap := make(map[int32]int32)

	// remove duplicates while maintaining ordering
	i = 1
	for _, score := range ranked {
		if _, ok := ranksMap[score]; !ok {
			ranksMap[score] = i
			newRanked = append(newRanked, score)
			i++
		}
	}

	i = 1
	for _, p := range player {
		i = 1
		for _, r := range newRanked {
			if p >= r {
				break
			}
			i++
		}
		ranks = append(ranks, i)
	}

	return ranks
}

func pickingNumbers(a []int32) int32 {
	var (
		maxLength int32 = 0
		counter   int32 = 1
		i         int32 = 0
		pivot     int32 = 0
	)

	for i < int32(len(a)) {
		fmt.Println("Before", i, pivot, counter, maxLength)
		if a[pivot]-a[i] <= 1 && a[pivot]-a[i] >= -1 {
			counter++
		} else {
			fmt.Println("Changing pivot")
			counter--
			pivot = i
			continue
		}
		i++
		fmt.Println("After", i, pivot, counter, maxLength)
	}

	fmt.Println("The last frontier: ", i, pivot, counter, maxLength)

	if counter > maxLength {
		maxLength = counter
	}
	return maxLength
}

func encryption(s string) string {
	var (
		lenStripped int = len(s)
		row         int = int(math.Floor(math.Sqrt(float64(lenStripped))))
		col         int = row + 1
	)

	if row*col < lenStripped {
		fmt.Println("Incrementing row")
		row++
	} else if row*col >= lenStripped && row*(col-1) >= lenStripped {
		fmt.Println("Decrementing col")
		col--
	}

	fmt.Println(lenStripped, row, col)

	// place the texts rows first
	i := 0
	grid := make([][]string, 0)
	line := make([]string, 0)

	for i < lenStripped {
		line = append(line, string(s[i]))
		if len(line) == col {
			grid = append(grid, line)
			line = make([]string, 0)
		}
		i++
	}
	if len(line) > 0 {
		diff := col - len(line)
		i = 0
		for i < diff {
			line = append(line, "")
			i++
		}
		grid = append(grid, line)
	}

	fmt.Println(grid)

	printable := ""
	i, j := 0, 0
	for j < col {
		i = 0
		for i < row {
			printable = printable + grid[i][j]
			i++
		}
		printable = printable + " "
		j++
	}

	return printable
}

func hurdleRace(k int32, height []int32) int32 {
	var (
		maxHeight int32 = 0
	)

	for _, v := range height {
		if v > maxHeight {
			maxHeight = v
		}
	}

	if maxHeight <= k {
		return 0
	}

	return maxHeight - k
}

func designerPdfViewer(h []int32, word string) int32 {
	var (
		letters    []string = []string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
		wordLength int32    = 0
		maxHeight  int32    = 0
	)
	hMap := make(map[string]int32)

	for idx, l := range letters {
		if _, ok := hMap[l]; !ok {
			hMap[l] = h[idx]
		}
	}

	for wordLength < int32(len(word)) {
		if maxHeight < hMap[string(word[wordLength])] {
			maxHeight = hMap[string(word[wordLength])]
		}
		wordLength++
	}

	return maxHeight * wordLength
}

func nimbleGame(s []int32) string {
	// find out the total coins in the square
	var (
		start     int32  = 0
		playerOne string = "First"
		playerTwo string = "Second"
	)

	for idx, v := range s {
		fmt.Printf("v: %d, Start: %d, idx: %d\n", v, start, idx)
		if v%2 != 0 {
			start = start ^ int32(idx)
			fmt.Printf("\tIn if start: %d\n", start)
		} else {
			fmt.Printf("\tIn else start: %d\n", start)
		}
	}

	if start > 0 {
		return playerOne
	}
	return playerTwo
}

func main() {
	var (
		s []int32 = []int32{161, 274, 545, 681, 705, 84, 326, 806, 186, 508, 146, 870, 792, 737, 406, 327, 917, 178, 194, 336, 793, 934, 929, 175, 282, 955, 658, 224, 252, 189, 785, 413, 815, 330, 94, 521, 766, 773, 679, 305, 633, 825, 527, 778, 914, 933, 105, 832, 112, 652, 520, 257, 938, 449, 432, 221, 757, 442, 797, 9, 631, 582}
	)

	fmt.Printf("nimbleGame(%v): %v\n", s, nimbleGame(s))
}
