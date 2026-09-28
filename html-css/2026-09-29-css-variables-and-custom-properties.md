# CSS Variables and Custom Properties

> _2026-09-29_ | Category: **html-css**

Dynamic, reusable values in CSS.

```css
:root {
  /* Colors */
  --primary: #6366f1;
  --primary-light: #818cf8;
  --bg-dark: #0f172a;
  --text: #e2e8f0;
  
  /* Spacing */
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 32px;
  
  /* Typography */
  --font-sans: 'Inter', system-ui, sans-serif;
  --font-mono: 'Fira Code', monospace;
  
  /* Shadows */
  --shadow: 0 4px 6px -1px rgba(0,0,0,0.3);
  --radius: 12px;
}

.card {
  background: var(--bg-dark);
  color: var(--text);
  padding: var(--space-md);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  font-family: var(--font-sans);
}

/* Override in context */
.card:hover { --shadow: 0 8px 16px rgba(99,102,241,0.3); }

/* Dark/Light theme toggle */
[data-theme="light"] {
  --bg-dark: #ffffff;
  --text: #1e293b;
}
```

**Key Takeaway**: CSS variables enable theming (dark/light mode) with a single attribute change. They cascade and can be changed via JavaScript.
