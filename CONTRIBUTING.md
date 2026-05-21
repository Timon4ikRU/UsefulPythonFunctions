## 🛠️ How to Contribute?

Any help is welcome. Here’s what you can do:

| CONTRIBUTION TYPE | WHAT TO DO | EXAMPLE |
| :--- | :--- | :--- |
| **Report a bug** | Open an Issue with description | "equal_strict() doesn't work with None" |
| **Suggest an improvement** | Open an Issue with `enhancement` label | "Add compare_arrays() function" |
| **Improve documentation** | PR with fixes to README or docstrings | "Fixed typo in docstring" |
| **Write code** | Fork, make changes, submit PR | "Added is_prime() function" |
| **Write tests** | Add checks to `upfcheck.py` | "Test for random_array_int" |

---

## How to Submit a Pull Request (PR)

1. **Fork the repository** (click Fork on GitHub)
2. **Clone your copy**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/UsefulPythonFunctions.git
   ```
3. **Create a branch for your changes**:
   ```bash
   git checkout -b my-cool-feature
   ```
4. **Make changes and commit**:
   ```bash
   git commit -m "Add is_prime() function"
   ```
5. **Push to your fork**:
   ```bash
   git push origin my-cool-feature
   ```
6. **Open a Pull Request** on GitHub (click "Compare & pull request")

---

## Code Requirements

| REQUIREMENT | WHY |
| :--- | :--- |
| **Docstrings ('''...''')** | So others understand what the function does |
| **English function names** | UPF is an international project |
| **Don't break old functions** | Backward compatibility |
| **Update `upfcheck.py`** | So new functions are tested |
| **Follow PEP 8** | Code readability |

---

## Testing

Before submitting a PR, **always run**:
```bash
python upfcheck.py
```

If something breaks — fix it.

---

## Contact

- **Code questions**: open an Issue with `question` label
- **Suggestions**: `enhancement` label
- **Urgent**: email timofey202419@outlook.com

---

## License

This project is licensed under **GPL-2.0**.  
By contributing, you agree that your work will be under the same license.
