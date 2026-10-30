# JavaScript Design Patterns - Module

> _2026-10-31_ | Category: **javascript**

Organize code with encapsulation.

```javascript
// Revealing Module Pattern
const ShoppingCart = (() => {
  let items = []; // private
  
  function addItem(item) { items.push(item); }
  function removeItem(id) { items = items.filter(i => i.id !== id); }
  function getTotal() { return items.reduce((sum, i) => sum + i.price, 0); }
  function getItems() { return [...items]; } // return copy
  
  return { addItem, removeItem, getTotal, getItems }; // public API
})();

ShoppingCart.addItem({ id: 1, name: 'Laptop', price: 999 });
ShoppingCart.getTotal(); // 999
ShoppingCart.items; // undefined (private!)

// Observer Pattern
class EventEmitter {
  #handlers = {};
  on(event, fn) { (this.#handlers[event] ??= []).push(fn); }
  off(event, fn) { this.#handlers[event] = this.#handlers[event]?.filter(f => f !== fn); }
  emit(event, ...args) { this.#handlers[event]?.forEach(fn => fn(...args)); }
}

const bus = new EventEmitter();
bus.on('login', (user) => console.log(`Welcome ${user}`));
bus.emit('login', 'Dipak');
```
