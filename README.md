# Python Practice Repository

A collection of Python exercises covering the core foundations: variables, conditionals, loops, functions, modules, error handling, file handling and script organisation. Built as part of the AI Engineering curriculum (Module B1: Python programming foundations).

## Requirements

- Python 3.11 or higher
- Git

## Setup

1. Clone the repository and open the folder:
```
      git clone https://github.com/azubukouju8-dev/python-practice.git
   cd python-practice
```
2. Create a virtual environment:
```
   py -m venv .venv
```
3. Activate it (Windows PowerShell):
```
   .venv\Scripts\activate
```
4. Install the dependencies:
```
   pip install -r requirements.txt
```

## Exercises

| Folder | Concept | How to run |
|---|---|---|
| `01_variables_and_data_types` | Data types and type conversion | `py 01_variables_and_data_types\profile.py` |
| `02_conditionals` | if / elif / else (grade checker) | `py 02_conditionals\grade_checker.py` |
| `03_loops` | for and while loops, FizzBuzz | `py 03_loops\loops_practice.py` |
| `04_functions` | Parameters, defaults, return values | `py 04_functions\calculator.py` |
| `05_modules` | Standard library and custom modules | `py 05_modules\main.py` |
| `06_error_handling` | try / except / else / finally | `py 06_error_handling\safe_operations.py` |
| `07_file_handling` | Text files, JSON, missing files | `py 07_file_handling\notes_manager.py` |
| `08_script_organisation` | Splitting code into config, helpers and main | `py 08_script_organisation\main.py` |

## Running the tests

Automated tests cover exercise 2 (grade checker) and exercise 4 (calculator functions). From the project root, with the virtual environment active, run:

```
pytest
```

All 20 tests should pass.

## Debugging note

See [DEBUGGING.md](DEBUGGING.md) for a real error I hit while building this project, what caused it and how I fixed it.

## Project structure

```
python-practice/
├── 01_variables_and_data_types/
├── 02_conditionals/          (includes tests)
├── 03_loops/
├── 04_functions/             (includes tests)
├── 05_modules/
├── 06_error_handling/
├── 07_file_handling/
├── 08_script_organisation/
├── requirements.txt
├── README.md
└── DEBUGGING.md
```