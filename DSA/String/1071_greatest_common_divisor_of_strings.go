func gcdOfStrings(str1 string, str2 string) string {
	// 檢查 str1 + str2 是否等於 str2 + str1
	if str1+str2 != str2+str1 {
		return ""
	}
	// 如果兩個字符串長度相等，則返回 str1（因為此時 str1 和 str2 一樣）
	if len(str1) == len(str2) {
		return str1
	}
	// 如果 str1 比 str2 長，遞迴呼叫並刪去 str1 前面相等部分
	if len(str1) > len(str2) {
		return gcdOfStrings(str1[len(str2):], str2)
	}
	// 如果 str2 比 str1 長，遞迴呼叫並刪去 str2 前面相等部分
	return gcdOfStrings(str1, str2[len(str1):])
}