func grayCode(n int) []int {
	if n <= 0 {
		return []int{0}
	}
	if n == 1 {
		return []int{0, 1}
	}
	res := []int{0, 1}
	for i := 1; i < n; i++ {
		for j := len(res) - 1; j >= 0; j-- {
			res = append(res, res[j]|(1<<i))
		}
	}
	return res
}