func findMaxAverage(nums []int, k int) float64 {
	// 計算第一個窗口的總和
	windowSum := 0
	for i := 0; i < k; i++ {
		windowSum += nums[i]
	}
	maxSum := windowSum
	// 使用滑動窗口方法遍歷陣列
	for i := k; i < len(nums); i++ {
		// 更新窗口總和
		windowSum = windowSum + nums[i] - nums[i-k]
		if windowSum > maxSum {
			maxSum = windowSum
		}
	}
	// 計算最大平均值
	return float64(maxSum) / float64(k)
}