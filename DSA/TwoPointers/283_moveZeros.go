func moveZeroes(nums []int) {
	left := 0 // 指向非零元素的索引

	// 遍歷數組
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			// 將非零元素交換到左側
			nums[left], nums[i] = nums[i], nums[left]
			left++
		}
	}
}

/*
運作原理:
left 指針初始指向索引 0。
遍歷數組，當遇到非零元素時，將其與 left 指針指向的元素交換，然後 left 指針向右移動一位。
遍歷結束後，所有非零元素都被移動到數組左側，而右側則自動填充為 0。 */