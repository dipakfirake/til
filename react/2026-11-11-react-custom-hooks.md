# React Custom Hooks

> _2026-11-11_ | Category: **react**

Extract reusable logic into custom hooks.

```jsx
// useFetch — reusable data fetching
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const controller = new AbortController();
    setLoading(true);
    fetch(url, { signal: controller.signal })
      .then(res => res.json())
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false));
    return () => controller.abort();
  }, [url]);

  return { data, loading, error };
}

// Usage in any component
function Products() {
  const { data, loading, error } = useFetch('/api/products');
  if (loading) return <Spinner />;
  if (error) return <Error message={error} />;
  return <ProductList items={data} />;
}
```

**Rules**: Name starts with `use`. Can call other hooks. Each call gets its own isolated state.
