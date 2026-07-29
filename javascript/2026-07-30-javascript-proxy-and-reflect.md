# JavaScript Proxy and Reflect

> _2026-07-30_ | Category: **javascript**

Intercept object operations.

```javascript
const handler = {
  get(target, prop) {
    console.log(`Accessing: ${prop}`);
    return prop in target ? target[prop] : `Property ${prop} not found`;
  },
  set(target, prop, value) {
    if (prop === 'age' && (value < 0 || value > 150))
      throw new RangeError('Invalid age');
    target[prop] = value;
    return true;
  }
};

const user = new Proxy({}, handler);
user.name = 'Dipak';
user.age = 25;
user.age = -1;  // throws RangeError!

// Reactive state (Vue.js uses this!)
function reactive(obj) {
  return new Proxy(obj, {
    set(target, key, value) {
      target[key] = value;
      notifySubscribers(key, value); // trigger UI update
      return true;
    }
  });
}

const state = reactive({ count: 0 });
state.count = 1; // automatically triggers notification
```

**Key Takeaway**: Proxies enable validation, logging, reactive data binding, and API mocking. Vue 3's reactivity system is built on Proxy.
