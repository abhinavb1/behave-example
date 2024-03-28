### README.md

# Behave Project Example

This is a test project demonstrating api testing use Behave for behavior-driven development (BDD) in Python.

## Overview

This project contains a simple Behave feature file and corresponding step definitions. The feature file (`api.feature`) defines a basic scenario with steps, and the step definitions (`steps/steps.py`) implement the logic for these steps.

### Features

- `api.feature`: Contains the feature file with a scenario for demonstration.
- `steps/steps.py`: Contains step definitions for the scenario outlined in `api.feature`.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/behave-example.git
   cd behave-example
   ```

2. Create and activate a virtual environment (recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running Tests

To run the Behave tests:

```sh
behave -D currency=INR -D Invalidcurrency=VHA

Note: Not passing "currency" or "Invalidcurrency" would throw error.
```

### Options

- `--no-capture`: Display real-time output from print statements in step definitions.
  ```sh
  behave --no-capture -D currency=INR -D Invalidcurrency=VHA
  ```

## Structure

```
behave-project/
│
├── features/                      # Directory for Behave feature files
│   ├── api.feature         # Example Behave feature file
│   └── steps/                     # Directory for step definitions
│       └── steps.py            # Example step definitions
│
├── .gitignore                     # Specifies files/folders to ignore by Git
├── README.md                      # Project README file
└── requirements.txt               # Project dependencies
```

