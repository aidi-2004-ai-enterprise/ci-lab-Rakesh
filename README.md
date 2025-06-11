# CI Pipeline Lab – Rakesh

This repository demonstrates the setup of a **Continuous Integration (CI) pipeline** using **GitHub Actions** . It was completed as part of a lab2.

---

## Objective

To configure a CI pipeline that automatically:

- Runs a Python script
- Executes unit tests using `pytest`
- Ensures only tested code is merged into the `main` branch via pull requests

---

##  Tools & Technologies Used

- **Python 3.10**
- **pandas** – for data loading
- **pytest** – for writing unit tests
- **GitHub Actions** – for automated CI pipeline
- **uv** – for modern Python dependency management
- **Git Bash** – for local development and version control

---

## Project Description

This project:

- Loads the **Penguin Dataset** from Seaborn's public repository.
- Prints the shape of the dataset using a function in `main.py`.
- Validates the dataset structure using a unit test.
- Automatically runs build and test jobs for **every pull request** targeting the `main` branch using GitHub Actions.

---

## 📁 Project Structure

```bash
ci-lab-Rakesh/
├── main.py                 # Python script that loads and prints the shape of the dataset
├── test_main.py            # Unit test that verifies the dataset shape
├── pyproject.toml          # UV project file for dependency management
├── uv.lock                 # Lock file recording exact versions
├── .python-version         # Python version file (optional, for version pinning)
├── README.md               # Project documentation file
├── __pycache__/            # Python cache folder (auto-generated)
└── .github/
    └── workflows/
        └── ci.yml          # GitHub Actions workflow for CI pipeline


---

## 🔁 CI/CD Workflow Summary

1. created a **feature branch** `add-tests`
2. Writes code and commits changes
3. Pushes the branch and opens a **pull request**
4. GitHub Actions automatically:
   - Runs the script to check it works
   - Runs all unit tests using `pytest`
5. Pull request is only merged if **all CI checks pass**

---

## Author

**Rakesh Kasaragadda**  

