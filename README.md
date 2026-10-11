# Note App

A simple note-taking application for creating, editing, and organizing notes.

## Requirements

- Python 3.10+
- [Poetry](https://python-poetry.org/)

## Installation

```bash
git clone <repository-url>
cd note-app
poetry install
```

## Usage

Activate the Poetry environment:

```bash
poetry shell
```

Run the application:

```bash
poetry run python <entrypoint>.py
```

Replace `<entrypoint>.py` with the application's entry-point file.

## Development

Install dependencies and run commands through Poetry:

```bash
poetry add <package>
poetry add --group dev <package>
poetry run pytest
```

## License

This project is provided as-is.
