# Two Pointer Technique

> _2026-06-23_ | Category: **dsa**

Solve array problems in O(n) instead of O(n²).

```java
// Pattern 1: Opposite ends (sorted array)
public int[] twoSum(int[] nums, int target) {
    int l = 0, r = nums.length - 1;
    while (l < r) {
        int sum = nums[l] + nums[r];
        if (sum == target) return new int[]{l, r};
        else if (sum < target) l++;
        else r--;
    }
    return new int[]{-1, -1};
}

// Pattern 2: Fast & Slow
public int removeDuplicates(int[] nums) {
    int slow = 0;
    for (int fast = 1; fast < nums.length; fast++)
        if (nums[fast] != nums[slow]) nums[++slow] = nums[fast];
    return slow + 1;
}
```

**Use when**: Sorted arrays, pair finding, palindrome check, container with most water.
