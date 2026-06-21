# React Props and Children

> _2026-06-22_ | Category: **react**

Pass data and components to children.

```jsx
function Card({ title, children, variant = 'default', onClick }) {
  return (
    <div className={`card card-${variant}`} onClick={onClick}>
      <h3>{title}</h3>
      <div className="card-body">{children}</div>
    </div>
  );
}

// Usage
<Card title="Welcome" variant="primary" onClick={() => alert('clicked')}>
  <p>This is the card content</p>
  <button>Action</button>
</Card>

// Render prop pattern
function DataFetcher({ url, render }) {
  const [data, setData] = useState(null);
  useEffect(() => { fetch(url).then(r=>r.json()).then(setData); }, [url]);
  return render(data);
}

<DataFetcher url="/api/users" render={(users) => (
  users?.map(u => <UserCard key={u.id} user={u} />)
)} />
```

**Key Takeaway**: Props flow down (parent → child). Use `children` for composition. Render props for sharing logic.
