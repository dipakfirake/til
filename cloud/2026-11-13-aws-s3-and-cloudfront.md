# AWS S3 and CloudFront

> _2026-11-13_ | Category: **cloud**

Storage and CDN.

**S3 (Simple Storage Service)**: Object storage (not block storage). Files are stored in Buckets with a flat structure (no real folders, just keys like `folder/file.jpg`).
- Standard: frequently accessed.
- Glacier: cheap archive, takes hours to retrieve.

**CloudFront (CDN)**: Caches S3 content at Edge Locations worldwide.
- User in India requests image -> Served from Mumbai edge location (fast!) instead of US East S3 bucket (slow).

**Key Takeaway**: Never serve static assets (images, JS, CSS) directly from your app server or raw S3. Always put a CDN in front to reduce latency and save bandwidth costs.
