# MLOps CI/CD Project

This repository demonstrates the basics of MLOps by implementing a simple CI/CD pipeline using GitHub Actions, version control with Git, and a sample machine learning project.

## Project Structure

.
├── .github
│ └── workflows
│ └── main.yml # GitHub Actions workflow configuration
├── model.py # Sample ML model script
├── test_model.py # Unit tests for the ML model
├── README.md # Project documentation
└── requirements.txt # Project dependencies


## CI/CD Pipeline

The CI/CD pipeline is set up using GitHub Actions and includes the following stages:

1. **Linting**: Ensures code quality using `pylint`.
2. **Testing**: Verifies functionality using `pytest`.
3. **Deployment**: Placeholder step for deploying the model (can be replaced with actual deployment steps).

The workflow file is located at `.github/workflows/main.yml`.

### Workflow Configuration

```yaml
name: CI/CD Pipeline

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pylint
    - name: Lint with pylint
      run: |
        pylint **/*.py

  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest
    - name: Run tests
      run: |
        pytest

  deploy:
    runs-on: ubuntu-latest
    needs: [lint, test]
    steps:
    - uses: actions/checkout@v2
    - name: Deploy
      run: echo "Deploying your app..." # Replace with actual deployment steps
```

## Version Control

### Version control is implemented using Git. The repository demonstrates the following:

1. **Branching**: Creating new branches for features or fixes.
2. **Merging**: Merging branches through pull requests.
3. **Pull Requests**: Creating and reviewing pull requests to integrate changes.