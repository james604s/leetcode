package main

import (
	"fmt"
)

func twoSum(nums []int, target int) []int {
	valMap := make(map[int]int)
	for k, v := range nums {
		idx, ok := valMap[target-v]
		if ok {
			fmt.Println([]int{idx, k})
			return []int{idx, k}
		}
		valMap[v] = k
	}
	return nil
}

func main() {
	arr := []int{15, 11, 7, 2}
	twoSum(arr, 9)
}
