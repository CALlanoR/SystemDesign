# Unit Tests
- Unit testing helps you find bugs and produces better, more reliable code.
- Unit testing helps to develop a tester's mindset. 
    - A mindset that every piece of code potentially breaks something. 
    - A mindset that takes edge cases into account by default. 

- Unit testing best practices
    1. Tests Should Be Readable (Use Sound Naming Conventions)
    2. Avoid logical conditions such as if, for, while, switch. You should not create any data in test method scope. Only focus result.
    3. Focus Most Effective Methods
    4. Unit Tests Should Be Fast
    5. Avoid Magic Strings
    6. Tests Should Be Independent
    7. Each Test Should Test One Thing
    8. Tests Should Be Deterministic
    9. Tests Should Not Include Implementation Details (behaviour not details)
    10. Tests Should Be Part Of The Commit and Build Process (pre-commit hooks to run tests before each commit)
    11. Use Single Assert Per Test Method
    12. Use Fake Data/Databases in Testing
    13. Avoid Test Interdependence (Write individual, independent test methods and put related tests in a single test class)
    14. Test for Security Issues as Part of Your Unit Tests (SQL Injection for example)
    
- Coverage %
    - Code coverage percentage of between 60% and 90% (do not become obsessed with 100%)
    - Code Coverage Percentage = (Number of lines of code executed by a testing algorithm/Total number of lines of code in a system component) * 100
- Cloud Services Unit test
    - https://medium.com/@seifeddinerajhi/unit-testing-aws-lambda-with-python-and-mock-aws-services-using-moto-80e1855c16e1