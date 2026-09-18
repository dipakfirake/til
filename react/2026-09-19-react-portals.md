# React Portals

> _2026-09-19_ | Category: **react**

Render components outside the DOM hierarchy.

```jsx
import { createPortal } from 'react-dom';

function Modal({ isOpen, onClose, children }) {
  if (!isOpen) return null;
  
  return createPortal(
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}>
        <button className="modal-close" onClick={onClose}>&times;</button>
        {children}
      </div>
    </div>,
    document.getElementById('modal-root') // renders here, not in parent
  );
}

// Usage
function App() {
  const [showModal, setShowModal] = useState(false);
  return (
    <div style={{ overflow: 'hidden' }}> {/* overflow won't clip modal! */}
      <button onClick={() => setShowModal(true)}>Open Modal</button>
      <Modal isOpen={showModal} onClose={() => setShowModal(false)}>
        <h2>I'm rendered outside the parent!</h2>
      </Modal>
    </div>
  );
}
```

**Key Takeaway**: Portals are essential for modals, tooltips, and dropdowns. The component stays in React tree (events bubble up) but renders elsewhere in DOM.
