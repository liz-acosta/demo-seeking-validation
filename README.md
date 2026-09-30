# 🐾 Seeking Validation: An introduction to Pydantic

Demo code for a talk on Python data validation techniques —- from manual type checks to Pydantic models —- illustrated through a dog-themed lens.

## Overview

This repository contains example code demonstrating a progressive approach to data validation in Python:

1. **Type hints:** Using Python's `typing` module to annotate function signatures
2. **Manual validation:** Catching type errors at runtime with explicit checks
3. **Pydantic:** Leveraging data models for automatic parsing and validation

## Repository structure

```
demo-seeking-validation/
├── helpers/                  # Helper utilities
├── dog_examples.py           # Additional dog class examples
├── get_dog_facts.py          # Main app — fetches breed info from the Dog API using a Pydantic model
├── len_examples.py           # Examples illustrating len() behavior with mock objects
├── mock_examples.py          # Standalone examples of Mock, MagicMock, and @patch
├── pydantic_examples.py      # Pydantic BaseModel with field constraints and type coercion
├── requirements.txt
├── talk_demos.ipynb          # Jupyter notebook with live demo walkthroughs
├── test_get_dog_facts.py     # Unit tests for get_dog_facts.py using unittest and mocked HTTP calls
├── types_examples.py         # Type hint annotations with dog breed classes
└── validation_examples.py    # Manual runtime validation to catch invalid types early
```


## Prerequisites

- Python 3.10+
- A basic understanding of using Jupyter Notebooks (A great intro can be found [here](https://code.visualstudio.com/docs/datascience/jupyter-notebooks))

## Environment setup and dependency installation

Create and activate a virtual environment:

```bash
virtualenv venv && source venv/bin/activate
```

(This is also the environment to select for the notebook kernel.)

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Explore the examples

```bash
python types_examples.py
python validation_examples.py
python pydantic_examples.py
python mock_examples.py
```

### Run the Jupyter notebook

To run the notebook UI locally:
```bash
jupyter notebook pydantic_demos.ipynb
```

Or you can run the notebook in your IDE with the appropriate extension. The Visual Studio Code extension can be found [here](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).

### Optional: Static type checking with `mypy`

```bash
mypy types_examples.py
```

## Resources and references

- [Wikipedia Entry About Pugs](https://en.wikipedia.org/wiki/Pug): Learn all about Pugs on Wikipedia
- [Seeking Validation: Data Validation in Python with Pydantic and Vonage Verify](https://vonage.dev/4h5kvtt): Learn how Pydantic simplifies Python data validation, with a real-world demo using the Vonage Verify API

![A gif of a cute Pug against a pink backdrop making it rain with dollar bills.](giphy-457171081.gif)