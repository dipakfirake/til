# Destructuring and Spread

> _2026-07-25_ | Category: **javascript**

Extract values and merge objects/arrays.

```javascript
// Object destructuring
const { name, age, address: { city } } = user;
const { role = 'user', theme = 'dark' } = settings; // defaults
const { name: userName, id: oderId } = response; // rename

// Array destructuring
const [first, second, ...rest] = [1, 2, 3, 4, 5];
// first=1, second=2, rest=[3,4,5]

// Spread
const merged = { ...defaults, ...userPrefs, timestamp: Date.now() };
const newArr = [...oldArr, newItem];
const clone = { ...original }; // shallow clone

// Function params
function createUser({ name, email, role = 'user' }) {
  return { name, email, role, createdAt: new Date() };
}
createUser({ name: 'Dipak', email: 'd@test.com' });
```

**Key Takeaway**: Spread creates shallow copies. For deep clone use `structuredClone()` (modern) or `JSON.parse(JSON.stringify())`.
