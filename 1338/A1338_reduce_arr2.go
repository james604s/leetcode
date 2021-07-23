package main
import (
	"fmt"
)

func minSetSize(arr []int) int {
	countDict := make(map[int]int)
	fmt.Println(countDict)
    maxCount := 0
    for _, val := range arr {
        countDict[val]++ //maintain a map based on val : count of this val
		fmt.Println(countDict)
        maxCount = max(maxCount, countDict[val]) //track the max count
    }
	fmt.Println(countDict)

    keys := make([]int, 0, len(countDict))
    for k := range countDict {
		keys = append(keys, k)
		fmt.Println(keys)
    }

    bucket := make([]int, 0, len(countDict))
    for _, val := range countDict {
        // bucket[val]++ 
		bucket = append(bucket, val)
		fmt.Println(bucket)
    }

	return 1
}

func max(a, b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}

func main(){
	arr := []int{5,5,1,3,4,4,5,2}
	minSetSize(arr)
}