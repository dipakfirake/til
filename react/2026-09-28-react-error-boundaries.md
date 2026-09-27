# React Error Boundaries

> _2026-09-28_ | Category: **react**

Catch render errors gracefully.

```jsx
class ErrorBoundary extends React.Component {
  state = { hasError: false, error: null };
  
  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }
  
  componentDidCatch(error, info) {
    logErrorToService(error, info.componentStack);
  }
  
  render() {
    if (this.state.hasError) {
      return (
        <div className="error-fallback">
          <h2>Something went wrong</h2>
          <p>{this.state.error?.message}</p>
          <button onClick={() => this.setState({hasError:false})}>Try Again</button>
        </div>
      );
    }
    return this.props.children;
  }
}

// Usage
<ErrorBoundary>
  <UserProfile />  {/* If this crashes, fallback UI shows */}
</ErrorBoundary>
```

**Key Takeaway**: Error boundaries only catch rendering errors. They do NOT catch errors in event handlers, async code, or server-side rendering.
