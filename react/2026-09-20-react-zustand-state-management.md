# React Zustand State Management

> _2026-09-20_ | Category: **react**

Minimal, flexible state management.

```jsx
import { create } from 'zustand';
import { devtools, persist } from 'zustand/middleware';

const useStore = create(
  devtools(
    persist(
      (set, get) => ({
        cart: [],
        total: 0,
        
        addItem: (item) => set((state) => ({
          cart: [...state.cart, item],
          total: state.total + item.price
        })),
        
        removeItem: (id) => set((state) => {
          const item = state.cart.find(i => i.id === id);
          return {
            cart: state.cart.filter(i => i.id !== id),
            total: state.total - item.price
          };
        }),
        
        clearCart: () => set({ cart: [], total: 0 }),
        itemCount: () => get().cart.length,
      }),
      { name: 'cart-storage' } // localStorage persistence
    )
  )
);

// Usage in any component (no Provider needed!)
function CartIcon() {
  const total = useStore(state => state.total);
  const count = useStore(state => state.cart.length);
  return <span>Cart ({count}) - ₹{total}</span>;
}
```

**Key Takeaway**: Zustand is simpler than Redux. No providers, no reducers, no actions. Just a hook.
