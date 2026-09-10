# Docker Compose for Development

> _2026-09-11_ | Category: **devops**

Multi-container development environment.

```yaml
version: '3.8'
services:
  app:
    build: .
    ports: ["8080:8080"]
    environment:
      SPRING_DATASOURCE_URL: jdbc:mysql://db:3306/myapp
    depends_on:
      db: { condition: service_healthy }
    volumes: ["./src:/app/src"]  # hot reload
  
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: myapp
    ports: ["3306:3306"]
    volumes: ["mysql_data:/var/lib/mysql"]
    healthcheck:
      test: mysqladmin ping -h localhost
      interval: 10s
      retries: 5
  
  redis:
    image: redis:7-alpine
    ports: ["6379:6379"]

volumes:
  mysql_data:
```

```bash
docker-compose up -d     # start background
docker-compose logs -f   # follow logs
docker-compose down -v   # stop + remove volumes
```
