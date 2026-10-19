class Solution {
    public int search(int[] nums, int target) {
        int left = 0; // first
        int right = nums.length - 1; //last

        while (left <= right) { // keep going even when left = right (check that last value if it comes down to it)
            int middle = (left + right) / 2;
            if (target == nums[middle]) {
                return middle;
            } else if (target < nums[middle]) {
                // target is in the left side
                right = middle - 1;
            } else if (target > nums[middle]) {
                // target in the right
                left = middle + 1;
            } // we skip middle when != nums[middle], because we know the target isnt at the middle -> check after it
        }
        return -1; // if we never return nums[middle], target not in list
    }
}
