# CSS Flexbox Layout

> _2026-07-28_ | Category: **html-css**

One-dimensional layout (row or column).

```css
.container {
  display: flex;
  flex-direction: row;       /* row | column */
  justify-content: center;   /* main axis */
  align-items: center;       /* cross axis */
  gap: 16px;                 /* spacing between items */
  flex-wrap: wrap;           /* allow wrapping */
}

.item {
  flex: 1;                   /* grow equally */
  flex: 0 0 200px;           /* fixed width, no grow/shrink */
}

/* Common patterns */
/* Navbar: logo left, links right */
.navbar { display: flex; justify-content: space-between; align-items: center; }

/* Center anything */
.center { display: flex; justify-content: center; align-items: center; min-height: 100vh; }

/* Card grid */
.grid { display: flex; flex-wrap: wrap; gap: 20px; }
.card { flex: 1 1 300px; } /* min 300px, grow to fill */
```

**Key Takeaway**: Flexbox = 1D layout. Use `justify-content` for main axis, `align-items` for cross axis. Use Grid for 2D layouts.
