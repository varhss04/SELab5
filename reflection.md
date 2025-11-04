## Reflection 

1. Which issues were the easiest to fix, and which were the hardest? Why?  
   1. The convention issues and non-logical code errors were easiest to fix since their solution required either just a docstring, or small variable changes. Logical error changes were harder due to the fact that they require complete understanding and running of the code.  
2. Did the static analysis tools report any false positives? If so, describe one example.  
   1. No, not in this case.   
3. How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.  
   1. I'd use pre-commit hooks (e.g., using the `pre-commit` framework) to automatically run basic checks like Flake8 and Bandit on staged files before a commit is finalized. This catches simple errors (like unused imports or bare `except` statements ) immediately, shifting the burden of fixing issues early in the process.  
4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
   1. The most tangible gains were here. Fixing the dangerous default value (`W0102`) on the `logs` argument prevents a critical, hidden bug where a single list would be unintentionally shared across all function calls. Additionally, fixing the bare `except` (`W0702`) makes the code more robust by preventing the silent suppression of unexpected errors , and fixing the `eval`\-used warning eliminates a major security vulnerability