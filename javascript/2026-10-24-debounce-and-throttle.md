# Debounce and Throttle

> _2026-10-24_ | Category: **javascript**

Control function execution frequency.

```javascript
// Debounce: wait for pause in calls
function debounce(fn, delay) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

// Throttle: limit to once per interval
function throttle(fn, limit) {
  let throttled = false;
  return (...args) => {
    if (!throttled) {
      fn(...args);
      throttled = true;
      setTimeout(() => throttled = false, limit);
    }
  };
}

// Usage
searchInput.addEventListener('input', debounce(fetchResults, 300));
window.addEventListener('scroll', throttle(updatePosition, 100));
```

| | Debounce | Throttle |
|:---|:---|:---|
| Fires | After silence | At intervals |
| Use case | Search input, resize | Scroll, mousemove |
