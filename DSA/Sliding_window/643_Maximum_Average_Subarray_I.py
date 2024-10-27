class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        函數用於查找長度為 k 的最大平均值子陣列。

        Args:
        nums: 整數陣列。
        k: 子陣列的長度。

        Returns:
        最大平均值子陣列的平均值。
        """
        window_sum = sum(nums[:k])
        max_sum = window_sum
        # 使用滑動窗口方法遍歷陣列
        for i in range(k, len(nums)):
            # 更新窗口總和
            window_sum = window_sum + nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        # 計算最大平均值
        return max_sum / k