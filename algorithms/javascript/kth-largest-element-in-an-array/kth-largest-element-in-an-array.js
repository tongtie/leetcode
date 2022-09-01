/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    return quickSelect(nums, k, 0, nums.length - 1);
};

const quickSelect = (nums, k, left, right) => {
    if (left === right) {
        return nums[left];
    }
    let pivot = partition(nums, left, right);
    if (pivot === k - 1) {
        return nums[pivot];
    }
    if (pivot < k - 1) {
        return quickSelect(nums, k, pivot + 1, right);
    } else {
        return quickSelect(nums, k, left, pivot - 1);
    }
}

const swap = (nums, i, j) => {
    let temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}

const partition = (nums, left, right) => {
    let pivot = Math.floor(Math.random() * (right - left + 1) + left);
    swap(nums, pivot, right);
    let i = left;
    for (let j = left; j < right; j++) {
        if (nums[j] > nums[right]) {
            swap(nums, i, j);
            i++;
        }
    }
    swap(nums, i, right);
    return i;
}