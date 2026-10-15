# QuickSort with Partition

> _2026-10-16_ | Category: **dsa**

Efficient in-place sorting.

```java
public void quickSort(int[] arr, int low, int high) {
    if (low < high) {
        int pivot = partition(arr, low, high);
        quickSort(arr, low, pivot - 1);
        quickSort(arr, pivot + 1, high);
    }
}

private int partition(int[] arr, int low, int high) {
    int pivot = arr[high]; // last element as pivot
    int i = low - 1;       // pointer for smaller elements
    
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr, i, j);
        }
    }
    swap(arr, i + 1, high);
    return i + 1;
}

// Optimization: random pivot to avoid O(n²) worst case
int randomPivot = low + random.nextInt(high - low + 1);
swap(arr, randomPivot, high); // move to end, then partition normally
```

**Key Takeaway**: QuickSort is fastest in practice (cache-friendly, in-place). Use random pivot to avoid worst-case O(n²) on sorted input.
