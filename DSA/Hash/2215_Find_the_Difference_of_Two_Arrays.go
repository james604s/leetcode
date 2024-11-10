package main

func findDifference(nums1 []int, nums2 []int) [][]int {
	a, b := uniq(nums1), uniq(nums2)
	var ans [][]int
	ans = make([][]int, 2)
	ans[0] = inOneNotInTwo(a, b)
	ans[1] = inOneNotInTwo(b, a)
	return ans
}

func uniq(x []int) map[int]bool {
	ans := make(map[int]bool)
	for _, v := range x {
		ans[v] = true
	}
	return ans
}

func inOneNotInTwo(a, b map[int]bool) []int {
	ans := make([]int, 0)
	for k, _ := range a {
		if _, ok := b[k]; !ok {
			ans = append(ans, k)
		}
	}
	return ans
}
