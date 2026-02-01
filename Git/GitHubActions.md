# Introduction
- GitHub Actions is a continuous integration and continuous delivery/deployment (CI/CD) platform that automates your software development workflows. 
- It allows you to build, test, and deploy software source code directly from your GitHub repository by creating custom workflows or pipelines. 

# Key Concepts
- **Workflows**: Automated processes that run when specific events occur in your repository (e.g., push, pull request, issue creation).
- **Events**: Triggers that start a workflow (e.g., `push`, `pull_request`, `schedule`, `workflow_dispatch`).
- **Jobs**: A set of steps that execute on the same runner and can run in parallel with other jobs.
- **Steps**: Individual tasks within a job, which can be shell commands or Docker actions.
- **Runners**: Servers that execute your workflows. GitHub provides hosted runners (Linux, Windows, macOS) or you can use self-hosted runners.
- **Actions**: Reusable units of code that perform specific tasks. They can be created by you, GitHub, or the community.

# How does GitHub Actions work?
<p align="center">
    <img src="./images/g1.png" width="400">
    <br/>
- GitHub Actions workflows are configured using YAML files that define the sequence of tasks or actions to be executed when triggered by events like code pushes, pull requests, and releases.

- Actions are reusable units of code that perform specific tasks, such as setting up dependencies, running tests, and deploying to a cloud provider or on-premise servers. You can create and publish custom Actions for your specific requirements.

- GitHub provides virtual machines, a.k.a. runners, to run your workflows on Linux, Windows, and macOS environments. You can also host your own self-hosted runners. Runners support any programming language, platform, and cloud provider, making GitHub flexible for various projects.

- GitHub Actions seamlessly integrates with other GitHub features, such as Issues, PRs, and Marketplace, allowing you to create automated workflows based on events in your repository.

Example:
```yaml
.github/workflows/deploy.yml

name: CI/CD Pipeline to S3

on:
  push:
    branches: [ main ]  # Triggers on every push to the main branch

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest  # Runs on the latest Ubuntu runner

    steps:
    # 1. Setup phase
    - name: Checkout Code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    # 2. Static Code Analysis (Linting)
    - name: Static Code Analysis (Flake8)
      run: |
        pip install flake8
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

    # 3. Automated Testing (Unit Testing)
    - name: Run Tests (Pytest)
      run: |
        pip install pytest
        pytest tests/

    # 4. Vulnerability Scanning (Security)
    - name: Security Scan (Bandit)
      run: |
        pip install bandit
        bandit -r . -f txt

    # 5. Deployment to AWS S3
    - name: Configure AWS Credentials
      uses: aws-actions/configure-aws-credentials@v4
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-east-1

    - name: Deploy to S3
      run: |
        aws s3 sync ./dist s3://my-deployment-bucket --delete
```