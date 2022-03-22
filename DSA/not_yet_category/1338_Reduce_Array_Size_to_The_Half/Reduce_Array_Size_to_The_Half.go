package main
import (
	// "fmt"
    "sort"
)

func minSetSize(arr []int) int {
	countDict := make(map[int]int)
    maxCount := 0
    for _, val := range arr {
        countDict[val]++ //maintain a map based on val : count of this val
        maxCount = max(maxCount, countDict[val]) //track the max count
    }
    //get value & sort slice
    bucket := make([]int, 0, len(countDict))
    for _, val := range countDict {
        bucket = append(bucket, val)
    }
    sort.Ints(bucket)

    res := 0
    removed := 0
    half := len(arr)/2                  //總長度的一半
    for removed < half {
        res += 1    
        removed += bucket[len(bucket)-1] //加上最後一個元素
        bucket = bucket[:len(bucket)-1]  //刪除最後一個元素
    }
    // fmt.Println(res)
	return res
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
    // sort.Ints(bucket)
    // fmt.Println(bucket)
    // keys := make([]int, 0, len(countDict))
    // for k := range countDict {
	// 	keys = append(keys, k)
	// 	fmt.Println(keys)
    // }

    // for key, value := range countDict {
    //     fmt.Println("key:", key, "value::",value)
    // }
    