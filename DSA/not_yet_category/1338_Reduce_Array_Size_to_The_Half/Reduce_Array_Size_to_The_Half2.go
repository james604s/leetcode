package main

import (
	fmt
)

func minSetSize(arr []int) int {
    countDict := make(map[int]int) 
    maxCount := 0
    for _, val := range arr {
        countDict[val]++ //maintain a map based on val : count of this val
        maxCount = max(maxCount, countDict[val]) //track the max count
    }
	fmt.Println(countDict)
    
    //maintain a bucket from idx 0, 1, 2 ... maxCount
    //for example bucket[2] = 3
    //stands for there are 3 integers in arr repeated 2 times
    bucket := make([]int, maxCount + 1)
    for _, val := range countDict {
        bucket[val]++ 
    }

    sum := 0
    res := 0
    //iterate the bucket from maxCount to 0
    for i := len(bucket) - 1; i >= 0; i-- {
        //on each idx, iterate the report times
        for j := 0; j < bucket[i]; j++ {
            if sum * 2 < len(arr) {
                //calculate sum and result
                sum += i
                res++
            } else {
                return res
            }
        }
    }
    return res
}

func max(a, b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}