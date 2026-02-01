# Secure best Practices

1. Always use the latest version of Python and its libraries. 
    - Vulnerabilities are often discovered in older versions, and using the latest ensures you benefit from the most recent security patches.
    - Example:
    ```
    python -m pip check 
    ```
    - Inclusion of OpenSSL 1.0.2k in the core runtime libraries

2. Use a Virtual Environment
    - Use a Virtual Environment
    - Example:
    ```
    python -m venv .venv
    ```

3. Sanitize All Input
    - Sanitize All Input
    - Example:
    ```
    import re
    
    def sanitize_input(input):
        # Remove any characters that are not letters, numbers, or whitespace
        return re.sub(r'[^a-zA-Z0-9\s]', '', input)
    ```

4. Use Parameterized Queries
    - Avoid SQL injection attacks by using parameterized queries when interfacing with databases.
    - Example:
    ```
    import sqlite3

    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    user_id = 1
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    ```

5. Avoid Executing Dynamically Generated Code
    - Avoid Executing Dynamically Generated Code
    - Example:
    ```
    user_input = "print('Hello, World!')"
    eval(user_input)
    ```
    - Secure Alternative‍
        - Use safer methods or avoid dynamic execution altogether. If parsing is needed, consider using libraries like `ast.literal_eval()` which only evaluates simple data types. 

6. Follow the Principle of Least Privilege
    - Ensure that your scripts only have the necessary permissions to perform their tasks. Avoid running scripts with elevated privileges unless absolutely necessary.


7. Data Encryption and Transmission sensitive data
    - Implement encryption mechanisms for sensitive data both at rest and in transit. Use libraries like `cryptography` to handle encryption and decryption securely. 
    - When transmitting data, use protocols like HTTPS to ensure data integrity and confidentiality.
    - Example:
```
from cryptography.fernet import Fernet

# Generate and save a key (this is done only once)
# In production, this key should be stored in an AWS Secrets Manager
clave = Fernet.generate_key()
cipher_suite = Fernet(clave)

data_sensitive = "confidential data here".encode()

# Encrypt
data_encrypted = cipher_suite.encrypt(data_sensitive)
print(f"Cifrado: {data_encrypted}")

# Decrypt
data_decrypted = cipher_suite.decrypt(data_encrypted)
print(f"Original: {data_decrypted.decode()}")
```

    - Salting and Hashing (For Passwords)
        - If you need to store user passwords, don't use encryption; use salted hashing (like bcrypt or Argon2). Encryption is reversible; hashing should not be.
        - Example:

```
import bcrypt

# Generate a salt
salt = bcrypt.gensalt()

# Hash the password
hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

# Verify the password
test_password = "password123"
if bcrypt.checkpw(test_password.encode('utf-8'), hashed_password):
    print("Password is correct!")
else:
    print("Password is incorrect!")
```

8. Use Proper Exception Handling
- Properly handling exceptions not only helps in debugging but also prevents your script from exposing sensitive information during failures.
- Error messages often leak valuable information about your application’s internals, which attackers can exploit. Keep error messages concise and generic to avoid exposing sensitive data.

9. Secure Password Handling
Never store passwords in plain text. Use cryptographic hashing algorithms like bcrypt or Argon2 to hash passwords securely. Implement strong password policies and consider multi-factor authentication for added security layers.

10. Protect Against Cross-Site Scripting (XSS)
XSS attacks occur when an attacker injects malicious scripts into web applications viewed by other users. Sanitize and escape user-generated content properly to prevent these attacks. Frameworks like Flask and Django provide built-in protection against XSS.

11. Regular Security Audits
- Periodically conduct security audits and vulnerability assessments of your codebase. 
- Utilize static code analysis tools like `bandit` to identify potential security flaws early in the development process.
    - Bandit identifies common security issues in Python code through static analysis. The tool scans for patterns known to introduce vulnerabilities including hardcoded passwords, SQL injection risks, and insecure cryptographic practices. 

12.  Stay Informed
Stay up-to-date with the latest security threats and trends in the Python community. Follow security advisories and patches released by the Python Software Foundation and other relevant organizations.
