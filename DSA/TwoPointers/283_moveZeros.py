

class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        nums_new = [num for num in nums if num != 0]
        nums.clear()
        nums.extend(nums_new)
        nums.extend([0] * zero_count)


class Solution2:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        將所有 0 移動到數組的末尾。

        Args:
        nums: 包含整數的列表。
        """
        left = 0  # 指向非零元素的索引

        # 遍歷數組
        for i in range(len(nums)):
            if nums[i] != 0:
                # 將非零元素交換到左側
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
