# React State Management with Redux Toolkit

> _2026-06-21_ | Category: **react**

Modern Redux with less boilerplate.

```jsx
import { createSlice, configureStore } from '@reduxjs/toolkit';

const cartSlice = createSlice({
  name: 'cart',
  initialState: { items: [], total: 0 },
  reducers: {
    addItem: (state, action) => {
      state.items.push(action.payload); // Immer handles immutability!
      state.total += action.payload.price;
    },
    removeItem: (state, action) => {
      const idx = state.items.findIndex(i => i.id === action.payload);
      state.total -= state.items[idx].price;
      state.items.splice(idx, 1);
    },
    clearCart: (state) => { state.items = []; state.total = 0; }
  }
});

export const { addItem, removeItem, clearCart } = cartSlice.actions;
const store = configureStore({ reducer: { cart: cartSlice.reducer } });

// Component
function Cart() {
  const { items, total } = useSelector(state => state.cart);
  const dispatch = useDispatch();
  return <button onClick={() => dispatch(addItem(product))}>Add to Cart</button>;
}
```
