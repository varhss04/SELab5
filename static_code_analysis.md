
# Static Code Analysis Reports

Note: All the “Fix Approaches” are the fixes I’ve made in my clean\_inventory\_system.py file. It seemed sensible to mention them within the issues table itself. 

Issues and Fixes \- Pylint Report

Pylint errors come with codes labelled C \- Convention, W \- Warning. I have only fixed W coded warnings from Pylint since C is to do with readability and not necessary for code execution. This covers the assignment requirement of fixing at least 4 issues.

| SI. No. | Issue | Type | Line | Description | Fix Approach |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | Mutable default arg | W | 12 | logs=\[\] shared across calls | Change default to None and initialize in method |
| 2 | missing-module-docstrong (sic) | C | 1 | The Python file is missing a module-level docstring at the top.  | Add a module-level docstring (e.g., """Inventory management system.""") to the first line of the file. |
| 3 | unused-import | W | 2 | The logging module was imported  but never used in the code. | Remove the line import logging since it is not needed. |
| 4 | missing-function-docstring | C | 8 | The function addItem does not have a docstring.  | Add a docstring to the addItem function explaining what it does (e.g., """Adds an item to the stock."""). |
| 5 | invalid-name | C | 8 | The function name addItem does not follow the snake\_case naming convention.  | Rename the function to add\_item and update all the places it is called. |
| 6 | dangerous-default-value | W | 8 | Using a mutable list \[\] as a default argument is dangerous because this single list is shared across all calls to the function.  | Change the default argument to None. Inside the function, add logic to check if the argument is None and initialize a new empty list if it is. |
| 7 | consider-using-f-string | C | 12 | The code is using an older string formatting method when a modern f-string could be used for better readability.  | Convert the string formatting to an f-string (e.g., print(f"Item {item} added with quantity {qty}.")). |
| 8 | missing-function-docstring | C | 14 | The function removeItem is missing a docstring.  | Add a docstring to the removeItem function explaining its purpose. |
| 9 | invalid-name | C | 14 | The function name removeItem uses camelCase instead of the preferred snake\_case style.  | Rename the function to remove\_item and update its calls. |
| 10 | bare-except | W | 19 | The try...except block does not specify an exception type.  This is risky as it catches all exceptions, including SystemExit and KeyboardInterrupt, making the code hard to debug. | Specify the exact exception you expect to catch, for example, except KeyError:. |
| 11 | missing-function-docstring | C | 22 | The function getQty is missing a docstring.  | Add a docstring to the getQty function explaining what it returns. |
| 12 | invalid-name | C | 22 | The function name getQty does not follow the snake\_case convention.  | Rename the function to get\_qty and update its calls. |
| 13 | missing-function-docstring | C | 25 | The function loadData is missing a docstring.  | Add a docstring to the loadData function. |
| 14 | invalid-name | C | 25 | The function name loadData does not follow the snake\_case convention.  | Rename the function to load\_data and update its calls. |
| 15 | unspecified-encoding | W | 26 | The open() function is used without specifying a file encoding.  This can lead to errors on different operating systems with different default encodings. | Add an explicit encoding to the open() call, such as encoding="utf-8". |
| 16 | global-statement | W | 27 | The global keyword is used. Modifying global variables from within functions can make code hard to read, debug, and maintain. | Refactor the code to avoid using a global variable. For example, have load\_data return the loaded data and assign it to stock\_data in the main script. |
| 17 | consider-using-with | R | 26 | A file is opened but not managed with a with statement.  This can cause resource leaks if the file is not properly closed, especially if an error occurs. | Rewrite the file operation using a with open(...) as f: block, which automatically handles closing the file. |
| 18 | missing-function-docstring | C | 31 | The function saveData is missing a docstring.  | Add a docstring to the saveData function. |
| 19 | invalid-name | C | 31 | The function name saveData does not follow the snake\_case convention.  | Rename the function to save\_data and update its calls. |
| 20 | unspecified-encoding | W | 32 | The open() function is called without an encoding argument.  | Add encoding="utf-8" to the open() call. |
| 21 | consider-using-with | R | 32 | A file is opened without using a with statement, risking a resource leak.  | Use a with open(...) as f: block to automatically manage the file resource. |
| 22 | missing-function-docstring | C | 36 | The function printData is missing a docstring.  | Add a docstring to the printData function. |
| 23 | invalid-name | C | 36 | The function name printData does not follow the snake\_case convention.  | Rename the function to print\_data and update its calls. |
| 24 | missing-function-docstring | C | 41 | The function checkLowItems is missing a docstring.  | Add a docstring to the checkLowItems function. |
| 25 | invalid-name | C | 41 | The function name checkLowItems does not follow the snake\_case convention.  | Rename the function to check\_low\_items and update its calls. |
| 26 | missing-function-docstring | C | 48 | The main (unnamed) function block is missing a docstring.  | Add a docstring explaining the main execution flow of the script. |
| 27 | eval-used | W | 59 | The code uses the eval() function, which is a significant security risk as it can execute arbitrary code. | Remove the eval() call. If it's for evaluating simple data structures, use the much safer ast.literal\_eval. In this case, just delete the line. |

Issues and Fixes \- Bandit Report

| SI.No | Issue | Type | Line | Description | Fix Approach |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | try\_except\_pass | W | 19 | A try...except block is used with a pass statement. This silences all errors (including unexpected ones) and can hide bugs, making debugging very difficult. | At a minimum, log the exception or print it. Ideally, catch a specific exception (like KeyError) and provide meaningful user feedback. |
| 2 | blacklist | W | 59 | The code uses the eval() function, which is "blacklisted" for being insecure. It allows for arbitrary code execution, which is a major security vulnerability (CWE-78) | Remove the eval() call. Bandit suggests using the safer ast.literal\_eval if you need to parse simple Python literals32, but in this case, the line should be deleted. |

Issues and Fixes \- Flake8 Report

| Sl.No | Issue | Type | Line | Description | Fix Approach |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 'logging' imported but unused | F | 2 | The logging module is imported but never used (F401).  | Remove the import logging line. |
| 2 | expected 2 blank lines, found 1 | E | 8 | According to the PEP 8 style guide, a top-level function definition should be preceded by two blank lines, but only one was found (E302).  | Add an additional blank line before def addItem.... |
| 3 | expected 2 blank lines, found 1 | E | 14 | Only one blank line was found before a function definition where two are expected (E302).  | Add an additional blank line before def removeItem.... |
| 4 | do not use bare 'except' | E | 19 | The except: block is "bare" and does not specify which exception it is catching (E722).  | Specify the exception type to catch, e.g., except KeyError:. |
| 5 | expected 2 blank lines, found 1 | E | 22 | Only one blank line was found before a function definition where two are expected (E302).  | Add an additional blank line before def getQty.... |
| 6 | expected 2 blank lines, found 1 | E | 25 | Only one blank line was found before a function definition where two are expected (E302).  | Add an additional blank line before def loadData.... |
| 7 | expected 2 blank lines, found 1 | E | 31 | Only one blank line was found before a function definition where two are expected (E302).  | Add an additional blank line before def saveData.... |
| 8 | expected 2 blank lines, found 1 | E | 36 | Only one blank line was found before a function definition where two are expected (E302).  | Add an additional blank line before def printData.... |
| 9 | expected 2 blank lines, found 1 | E | 41 | Only one blank line was found before a function definition where two are expected (E302).  | Add an additional blank line before def checkLowItems.... |
| 10 | expected 2 blank lines, found 1 | E | 48 | Only one blank line was found before a function definition where two are expected (E302).  | Add an additional blank line before the main function. |
| 11 | expected 2 blank lines after class or function definition, found 1 | E | 61 | Two blank lines are expected after the last function definition, but only one was found before the end of the file (E305).  | Add an additional blank line at the end of the script. |
