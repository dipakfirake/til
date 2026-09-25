# Map Set and WeakMap

> _2026-09-26_ | Category: **javascript**

Modern collection types beyond Object and Array.

```javascript
// Map: any type as key, ordered, iterable
const cache = new Map();
cache.set(userObj, 'cached data');    // object as key!
cache.set(42, 'number key');
cache.get(userObj);  // 'cached data'
cache.has(42);       // true
cache.size;          // 2

// Set: unique values
const set = new Set([1, 2, 3, 2, 1]); // Set(3) {1, 2, 3}
const unique = [...new Set(array)];     // remove duplicates

// Set operations
const a = new Set([1,2,3]), b = new Set([2,3,4]);
const union = new Set([...a, ...b]);                    // {1,2,3,4}
const intersection = new Set([...a].filter(x => b.has(x))); // {2,3}

// WeakMap: garbage-collectible keys
const metadata = new WeakMap();
metadata.set(element, { clicks: 0 }); // auto-removed when element is GC'd
```

**Key Takeaway**: Use Map over Object when keys aren't strings. Use Set for unique collections. WeakMap for caches that shouldn't prevent GC.
