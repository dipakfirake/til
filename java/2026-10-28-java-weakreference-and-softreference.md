# Java WeakReference and SoftReference

> _2026-10-28_ | Category: **java**

Control garbage collection behavior.

```java
// Strong reference — never GC'd while reachable
Object obj = new Object();

// Weak reference — GC'd at next collection
WeakReference<BigObject> weak = new WeakReference<>(new BigObject());
BigObject obj = weak.get(); // may return null!

// Soft reference — GC'd only when memory is low
SoftReference<byte[]> cache = new SoftReference<>(loadLargeData());

// WeakHashMap — entries removed when key is GC'd
Map<Key, Value> cache = new WeakHashMap<>();
// Perfect for caches that shouldn't prevent GC

// Example: image cache
private final Map<String, SoftReference<BufferedImage>> imageCache = new HashMap<>();

public BufferedImage getImage(String path) {
    SoftReference<BufferedImage> ref = imageCache.get(path);
    BufferedImage img = (ref != null) ? ref.get() : null;
    if (img == null) {
        img = loadImage(path);
        imageCache.put(path, new SoftReference<>(img));
    }
    return img;
}
```

**Key Takeaway**: WeakReference = temporary associations. SoftReference = memory-sensitive caches. Both help prevent memory leaks.
