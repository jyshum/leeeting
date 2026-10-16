class Solution {
    public int[] twoSum(int[] nums, int target) {
        // brute force is o(n^2), loop through every element and then loop again to search for a valid pair

        // o(n) time and space
        // intialize new hashmap to keep track of elements and their indexes (value is the key, index is the value)
        HashMap<Integer, Integer>  seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int need = target - nums[i];
            if (seen.containsKey(need)) {
                return new int[] {seen.get(need), i};
            }
            seen.put(nums[i], i);
        }
        return new int[]{};


    }
}
