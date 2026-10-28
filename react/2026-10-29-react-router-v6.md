# React Router v6

> _2026-10-29_ | Category: **react**

Client-side routing for SPAs.

```jsx
import { BrowserRouter, Routes, Route, Link, useParams, useNavigate, Navigate } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/products">Products</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/products" element={<Products />} />
        <Route path="/products/:id" element={<ProductDetail />} />
        <Route path="/admin" element={
          isAuth ? <Admin /> : <Navigate to="/login" replace />
        } />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

function ProductDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  return (
    <div>
      <h1>Product {id}</h1>
      <button onClick={() => navigate(-1)}>Back</button>
    </div>
  );
}
```
