# Kadane's Algorithm - Maximum Subarray

> _2026-10-02_ | Category: **dsa**

Find max sum contiguous subarray in O(n).

```java
public int maxSubArray(int[] nums) {
    int maxSum = nums[0];
    int currentSum = nums[0];
    
    for (int i = 1; i < nums.length; i++) {
        // Either extend current subarray or start new
        currentSum = Math.max(nums[i], currentSum + nums[i]);
        maxSum = Math.max(maxSum, currentSum);
    }
    return maxSum;
}

// Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
// maxSubArray = [4, -1, 2, 1] = 6
```

**Logic**: At each element, decide: "Is it better to extend the previous subarray or start fresh?"

**Key Takeaway**: Classic DP problem. Extend if `currentSum + nums[i] > nums[i]`, otherwise start new subarray.
