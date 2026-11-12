# React Code Splitting and Lazy Loading

> _2026-11-12_ | Category: **react**

Load components on demand for faster initial load.

```jsx
import { lazy, Suspense } from 'react';

const Dashboard = lazy(() => import('./pages/Dashboard'));
const Settings = lazy(() => import('./pages/Settings'));
const Analytics = lazy(() => import('./pages/Analytics'));

function App() {
  return (
    <Suspense fallback={<LoadingSpinner />}>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/settings" element={<Settings />} />
        <Route path="/analytics" element={<Analytics />} />
      </Routes>
    </Suspense>
  );
}
```

**Before**: One 500KB bundle loaded upfront
**After**: 100KB initial + load pages on demand

**Key Takeaway**: Lazy load route-level components. Use `Suspense` for loading fallbacks. This can reduce initial bundle size by 60%+.
