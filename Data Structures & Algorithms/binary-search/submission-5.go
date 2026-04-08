func search(nums []int, target int) int {
    left := 0
    right := len(nums) - 1
    
    for left<=right {
        mid := left + (right - left)/2
        if target == nums[mid]{
            return mid
        }else if nums[mid]< target { 
            left = mid + 1 
        } else {
            right = right - 1 
        }
    }
    return -1
}