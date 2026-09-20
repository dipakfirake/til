# React Testing with Jest and RTL

> _2026-09-21_ | Category: **react**

Test components from the user's perspective.

```jsx
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('shows search results', async () => {
  render(<SearchPage />);
  
  const input = screen.getByPlaceholderText('Search...');
  await userEvent.type(input, 'React');
  
  const button = screen.getByRole('button', { name: /search/i });
  fireEvent.click(button);
  
  // Wait for async results
  await waitFor(() => {
    expect(screen.getByText('React Hooks Guide')).toBeInTheDocument();
  });
  
  expect(screen.getAllByRole('listitem')).toHaveLength(5);
  expect(screen.queryByText('No results')).not.toBeInTheDocument();
});
```

**Testing Library Philosophy**: 
- Query by role, label, text (what users see)
- NOT by className, testId (implementation details)

**Key Takeaway**: Test behavior, not implementation. "The more your tests resemble the way your software is used, the more confidence they give you."
