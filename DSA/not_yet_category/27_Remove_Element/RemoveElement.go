package main

import (
	"fmt"
)

func removeElement(nums []int, val int) int {
	ptr := 0
	for i:=0; i < len(nums); i++{
		if nums[i] != val {
			nums[ptr] = nums[i]
			ptr++
		}
	}
	return ptr
}
// 	if nums == nil {
// 		return 0
// 	}
// 	ptr := 0
// 	for i := 0; i < len(nums); i++{
// 		if nums[i] != val {
// 			if i != ptr {
// 				nums[i], nums[j] = nums[j], nums[i]
// 				ptr ++
// 			} else {
// 				ptr ++
// 			}
// 		}
// 	}
// 	return ptr
// }
