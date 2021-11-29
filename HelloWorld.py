def HelloWorld(input = "World"):
    return "Hello World!" + input + "!"


name: CI for helloworld

on:
  push:
    branches: [main]
    
jobs:
  build:
    runs-on: ubuntu_latest
    steps:
    - uses: actions/setup-python@v2
      with:
        python-version: 3.8
    - name: Install Libraries
      run: 
        pip install flake8 pytest pytest-cov
        
    - name: Checkout Own Repo
      uses: actions/checkout@v2
      with: 
        repository: isaiahlowjung/HelloWorld
    - name: Checkout Test Script
      uses: actions/checkout@v2
      with:
        repository: lowkh2/DevOpsQARepo
        path: tests
        tokens: ${{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}}

    - name: Begin Pytest
      run:
        mv ./tests/. ./
        pytest --cov