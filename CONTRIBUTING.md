# Contributing to HTCP

Thank you for your interest in contributing to HTCP! This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment. Please:

- Be respectful and considerate in all communications
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/yourusername/htcp.git
   cd htcp
   ```
3. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Contribute

### Types of Contributions

- **Bug Fixes** — Fix issues and improve stability
- **New Features** — Add new functionality
- **Documentation** — Improve docs, add examples
- **Tests** — Add or improve test coverage
- **Performance** — Optimize existing code

### Areas We Need Help

- Adding encryption support (TLS/SSL)
- Async/await support
- Connection pooling
- Compression support
- Additional serialization formats
- Documentation and examples
- Unit and integration tests

## Development Setup

### Project Structure

```
htcp/
├── htcp/
│   ├── client/          # Client implementation
│   ├── server/          # Server implementation
│   └── common/          # Shared modules
│       ├── proto.py     # Protocol definitions
│       ├── serialization.py  # Serialization logic
│       └── utils.py     # Helper functions
├── tests/               # Test files (to be added)
├── examples/            # Usage examples
└── docs/                # Documentation
```

### Running Examples

```bash
# Terminal 1: Start server
python server_example.py

# Terminal 2: Run client
python client_example.py
```

### Running Tests

```bash
# When tests are implemented
python -m pytest tests/
```

## Coding Standards

### Python Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use type hints for all function parameters and return values
- Maximum line length: 120 characters
- Use descriptive variable and function names

### Code Example

```python
def process_data(data: bytes, expected_type: Type = None) -> tuple[Any, int]:
    """
    Process incoming data and return deserialized result.

    Args:
        data: Raw bytes to process
        expected_type: Optional type hint for deserialization

    Returns:
        Tuple of (deserialized_value, bytes_consumed)
    """
    if not data:
        raise ValueError("Empty data")

    # Implementation...
    return result, offset
```

### Commit Messages

Use clear and descriptive commit messages:

```
feat: add support for custom serializers
fix: resolve connection timeout issue
docs: update README with new examples
test: add unit tests for serialization module
refactor: simplify client connection logic
```

Format: `<type>: <description>`

Types:
- `feat` — New feature
- `fix` — Bug fix
- `docs` — Documentation
- `test` — Tests
- `refactor` — Code refactoring
- `perf` — Performance improvement
- `chore` — Maintenance tasks

## Pull Request Process

1. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and commit them with clear messages

3. **Test your changes** thoroughly

4. **Update documentation** if needed

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request** with:
   - Clear title describing the change
   - Description of what was changed and why
   - Reference to related issues (if any)
   - Screenshots or examples (if applicable)

### PR Checklist

- [ ] Code follows project style guidelines
- [ ] All existing tests pass
- [ ] New tests added for new functionality
- [ ] Documentation updated
- [ ] Commit messages are clear and descriptive
- [ ] No merge conflicts with main branch

## Reporting Bugs

When reporting bugs, please include:

1. **Title**: Clear, concise description
2. **Environment**:
   - Python version
   - Operating system
   - HTCP version
3. **Steps to Reproduce**: Minimal code example
4. **Expected Behavior**: What should happen
5. **Actual Behavior**: What actually happens
6. **Error Messages**: Full traceback if applicable

### Bug Report Template

```markdown
**Description**
A clear description of the bug.

**Environment**
- Python: 3.x.x
- OS: Ubuntu 22.04 / Windows 11 / macOS 14
- HTCP: version or commit hash

**Steps to Reproduce**
1. Create server with...
2. Connect client...
3. Call transaction...

**Expected Behavior**
The transaction should return...

**Actual Behavior**
Instead, the following error occurs...

**Error Traceback**
```
paste full traceback here
```
```

## Suggesting Features

Feature suggestions are welcome! Please:

1. Check existing issues to avoid duplicates
2. Describe the feature clearly
3. Explain the use case and benefits
4. Provide examples of how it would work

### Feature Request Template

```markdown
**Feature Description**
A clear description of the proposed feature.

**Use Case**
Why is this feature needed? What problem does it solve?

**Proposed API**
```python
# Example of how the feature would be used
client.new_feature(param1, param2)
```

**Alternatives Considered**
Other approaches you've considered.

**Additional Context**
Any other relevant information.
```

## Questions?

If you have questions about contributing, feel free to:

- Open a GitHub issue with the `question` label
- Contact the maintainers directly

Thank you for contributing to HTCP!
