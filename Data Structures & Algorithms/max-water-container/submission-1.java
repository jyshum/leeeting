class Solution {
    public int maxArea(int[] heights) {
        // two pointers (left and right, calcualting the water they can hold)
        // keep track of the water as the pointers move towards each other
        // the pointers objective is to find the highest bar of both
        // so if left is smaller than right, we aim for left to be bigger -> move left
        // vice versa with right

        int left = 0;
        int right = heights.length - 1;
        int water = 0;
        // water is the output of (right-left) * min(value of left, value of right)
        

        while (left < right) {
            water = Math.max(water, (right-left) * Math.min(heights[left], heights[right]));
            if (heights[left] < heights[right]) {
                left ++;
            } else {
                right --;
            }
        }
        return water;
    }
}
