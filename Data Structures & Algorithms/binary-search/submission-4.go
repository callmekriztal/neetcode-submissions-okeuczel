func search(nums []int, target int) int {
    left := 0
    right := len(nums) - 1
    
    for left<=right {
        mid := (right + left)/2
        if target == nums[mid]{
            return mid
        }else if target < nums[mid]{
            right = right - 1
        } else {
            left = left + 1 
        }
    }
    return -1
}