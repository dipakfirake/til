# GitHub Actions CI/CD

> _2026-09-17_ | Category: **devops**

Automate testing and deployment.

```yaml
name: CI/CD Pipeline
on:
  push: { branches: [main] }
  pull_request: { branches: [main] }

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with: { java-version: '17', distribution: 'temurin' }
      - run: mvn test
      
  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: mvn package -DskipTests
      - uses: actions/upload-artifact@v4
        with: { name: app, path: target/*.jar }
  
  deploy:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with: { name: app }
      - run: echo "Deploy to production"
```

**Key Takeaway**: Run tests on every PR. Deploy only from main. Use `needs` for job dependencies and `if` for conditional steps.
