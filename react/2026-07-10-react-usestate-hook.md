# React useState Hook

> _2026-07-10_ | Category: **react**

Manage component state with useState.

```jsx
function Counter() {
  const [count, setCount] = useState(0);
  const [user, setUser] = useState({ name: '', email: '' });

  // Functional update (when new state depends on old)
  const increment = () => setCount(prev => prev + 1);
  
  // Update object state (spread to keep other fields)
  const updateName = (name) => setUser(prev => ({ ...prev, name }));

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>+1</button>
      <input value={user.name} onChange={e => updateName(e.target.value)} />
    </div>
  );
}
```

**Key Takeaway**: `setState` is async and batched. Use functional form `prev => ...` when new state depends on old state. Never mutate state directly.
