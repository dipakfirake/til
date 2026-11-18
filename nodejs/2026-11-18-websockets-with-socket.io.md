# WebSockets with Socket.io

> _2026-11-18_ | Category: **nodejs**

Real-time bidirectional communication.

```javascript
// Server
const { Server } = require('socket.io');
const io = new Server(httpServer, { cors: { origin: "*" } });

io.on('connection', (socket) => {
  console.log(`User connected: ${socket.id}`);
  
  socket.on('join-room', (room) => { socket.join(room); });
  
  socket.on('chat-message', ({ room, message, user }) => {
    io.to(room).emit('new-message', { message, user, time: new Date() });
  });
  
  socket.on('typing', ({ room, user }) => {
    socket.to(room).emit('user-typing', user);
  });
  
  socket.on('disconnect', () => {
    console.log(`User disconnected: ${socket.id}`);
  });
});

// Client
const socket = io('http://localhost:3000');
socket.emit('join-room', 'general');
socket.emit('chat-message', { room: 'general', message: 'Hello!', user: 'Dipak' });
socket.on('new-message', (data) => displayMessage(data));
```

**Key Takeaway**: Socket.io handles reconnection, fallback transports, and rooms automatically. Use namespaces for different features (chat, notifications).
