type RecentCounter struct {
	requests []int
}

func Constructor() RecentCounter {
	/*
	  初始化計數器，最近請求數為零。
	*/
	return RecentCounter{requests: make([]int, 0)}
}

func (this *RecentCounter) Ping(t int) int {
	/*
	  在時間 t 添加新的請求，其中 t 表示以毫秒為單位的時間，並返回過去 3000 毫秒內發生的請求數（包括新請求）。
	  具體來說，返回包含範圍 [t - 3000, t] 中發生的請求數。

	  Args:
	    t: 新請求的時間（以毫秒為單位）。

	  Returns:
	    過去 3000 毫秒內發生的請求數。
	*/
	this.requests = append(this.requests, t)
	left := 0
	for left < len(this.requests) && this.requests[left] < t-3000 {
		left++
	}
	this.requests = this.requests[left:]
	return len(this.requests)
}

/*ㄔㄛ 
make 是 Golang 中的一個內建函數，用於分配和初始化某些資料結構，包括切片、映射和通道。
效能: 對於某些資料結構，make 可以比使用 new 關鍵字更有效率，因為它可以預先分配記憶體空間。
*/