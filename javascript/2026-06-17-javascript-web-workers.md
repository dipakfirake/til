# JavaScript Web Workers

> _2026-06-17_ | Category: **javascript**

Run heavy computation off the main thread.

```javascript
// worker.js
self.onmessage = (e) => {
  const { data, type } = e.data;
  if (type === 'SORT') {
    const sorted = data.sort((a, b) => a - b); // heavy operation
    self.postMessage({ type: 'SORTED', result: sorted });
  }
};

// main.js
const worker = new Worker('worker.js');

worker.onmessage = (e) => {
  console.log('Sorted:', e.data.result); // receive result
  updateUI(e.data.result);
};

worker.onerror = (e) => console.error('Worker error:', e.message);

// Send data to worker (doesn't block UI)
const bigArray = Array.from({ length: 1000000 }, () => Math.random());
worker.postMessage({ type: 'SORT', data: bigArray });

// Terminate when done
worker.terminate();
```

**Key Takeaway**: Web Workers run in separate thread — no access to DOM. Use for sorting, image processing, crypto, parsing large JSON.
