# WebSocket vs SSE vs Polling

> _2026-08-01_ | Category: **system-design**

Real-time communication patterns.

| Method | Direction | Use Case |
|:---|:---|:---|
| Short Polling | Client → Server (repeated) | Simple status checks |
| Long Polling | Client waits for response | Chat (fallback) |
| SSE | Server → Client (one-way) | Notifications, live feed |
| WebSocket | Bidirectional | Chat, gaming, collaboration |

```javascript
// SSE (Server-Sent Events) — simple one-way streaming
// Server
app.get('/events', (req, res) => {
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  
  const interval = setInterval(() => {
    res.write(`data: ${JSON.stringify({ time: Date.now() })}\n\n`);
  }, 1000);
  
  req.on('close', () => clearInterval(interval));
});

// Client
const source = new EventSource('/events');
source.onmessage = (e) => console.log(JSON.parse(e.data));
```

**Key Takeaway**: Use SSE for server → client streaming (simpler than WebSocket). Use WebSocket only when client needs to send data too.
