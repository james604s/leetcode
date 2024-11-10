import (
	"strings"
)

func reverseWords(s string) string {
	words := strings.Split(s, " ")
	var reverseWords []string
	for _, word := range words {
		if word != "" {
			reverseWords = append(reverseWords, word)
		}
	}
	// 反轉字串陣列
	for i, j := 0, len(reverseWords)-1; i < j; i, j = i+1, j-1 {
		reverseWords[i], reverseWords[j] = reverseWords[j], reverseWords[i]
	}
	return strings.Join(reverseWords, " ")
}