# Sliding Window

> _2026-10-10_ | Category: **dsa**

Find optimal subarray/substring in O(n).

```java
// Fixed window: max sum of k elements
public int maxSum(int[] arr, int k) {
    int sum = 0, max = 0;
    for (int i = 0; i < arr.length; i++) {
        sum += arr[i];
        if (i >= k) sum -= arr[i - k];
        if (i >= k - 1) max = Math.max(max, sum);
    }
    return max;
}

// Variable window: longest substring without repeating
public int lengthOfLongestSubstring(String s) {
    Set<Character> set = new HashSet<>();
    int l = 0, max = 0;
    for (int r = 0; r < s.length(); r++) {
        while (set.contains(s.charAt(r))) set.remove(s.charAt(l++));
        set.add(s.charAt(r));
        max = Math.max(max, r - l + 1);
    }
    return max;
}
```

**Pattern**: Expand right, shrink left when constraint violated.
