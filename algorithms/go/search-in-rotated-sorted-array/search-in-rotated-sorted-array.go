func search(nums []int, target int) int {
	var left, right int = 0, len(nums) - 1
	for left < right {
		var mid int = (left + right) / 2
		if nums[mid] < nums[right] {
			right = mid
		} else {
			left = mid + 1
		}
	}
	var rot = left
	left, right = 0, len(nums)-1
	for left <= right {
		var mid = (left + right) / 2
		var realMid = (mid + rot) % len(nums)
		if nums[realMid] == target {
			return realMid
		} else if nums[realMid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return -1
}