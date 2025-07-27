# Python in DevOps for beginers

Highlight why Python has become a go-to scripting language for DevOps
engineers. Its simplicity, flexibility, and vast ecosystem of libraries make it ideal for
DevOps automation and integrations

## Four Pillers of Any Programming Language:
- Keywords
- Data Types
- Operators
- Logic Reasoning Skills
  
## Key Advantages of Python in DevOps

- Ease of Use:
    Python’s readable syntax and ease of learning make it accessible for both
    beginner and experienced DevOps engineers
- Cross-Platform Compatibility:
    Python scripts run on multiple operating systems, including Linux,
    Windows, and macOS, ensuring consistency across environments.
- Rich Library Ecosystem:
    Python has extensive libraries for interacting with APIs, automating
    infrastructure, and working with data, making it suitable for various DevOps use cases.
- Community and Support:
    Python’s strong community support ensures fast problem-solving and
    access to many resources and tools.

## Core Use Cases of Python in DevOps
1. Automation of CI/CD Pipelines -
    Automating deployment, testing, and version control using tools like
    Jenkins, GitLab CI, or CircleCI with Python scripts.
2. Infrastructure as Code (IaC) -
    Provisioning and managing cloud resources and infrastructure using
    Python with tools like Terraform and AWS Boto3 SDK.
3. Configuration Management -
    Managing configurations across different environments using Python to
    ensure uniformity in deployment pipelines.
4. System Monitoring & Alerts -
    Creating monitoring scripts for logging, alerting, and integrating with
    platforms like Nagios, Prometheus, or Grafana.
5. Log Management and Analysis - 
    Parsing and analyzing logs with Python for real-time monitoring and error
    tracking.
6. API Integration - 
    Utilizing Python for interacting with external services via REST APIs, like
    integrating with cloud providers (AWS, Azure) or monitoring services (DataDog,
    Splunk).
7. Cloud Automation - 
    Using Python scripts to automate tasks in AWS, Google Cloud, and Azure
    like resource provisioning, scaling, and managing deployments.
8. Container Management and Orchestration: - 
    Automating the management of Docker containers and Kubernetes
    clusters through Python scripts and API integrations.
---

## 🔧 **Tools and Libraries for Python in DevOps**

Python offers powerful libraries that make DevOps automation efficient, scalable, and cloud-ready. Below are some essential tools—with real-world usage examples:

---

### 🟡 **Boto3** – AWS Automation with Python  
**Use Case:** Provisioning an EC2 instance on AWS  
```python
import boto3

ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-0abcdef1234567890',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro'
)
print("EC2 Instance Created:", instance[0].id)
```

---

### 🔵 **Ansible (Python-Based)** – Configuration Management & Automation  
**Use Case:** Triggering a playbook using Python’s subprocess module  
```python
import subprocess

subprocess.run(["ansible-playbook", "deploy_app.yml"])
```

> Note: Ansible is written in Python and can be extended using Python modules or executed via scripts.

---

### 🟢 **Requests** – API Automation  
**Use Case:** Check application health from a monitoring endpoint  
```python
import requests

response = requests.get("http://myapp.com/health")
if response.status_code == 200:
    print("App is Healthy")
else:
    print("App check failed:", response.status_code)
```

---

### 🔴 **Kubernetes Python Client** – Manage Kubernetes Resources  
**Use Case:** List all pods in a Kubernetes namespace  
```python
from kubernetes import client, config

config.load_kube_config()
v1 = client.CoreV1Api()
pods = v1.list_namespaced_pod(namespace="default")

for pod in pods.items:
    print(pod.metadata.name)
```

Here's a clean and simple sample Python script to demonstrate basic functionality:

---

### 📝 **Sample Python Script**

#### ✅ **Filename:** `test.py`

```python
# test.py
print("Hello, World!")
```

#### ▶️ **To run the script:**

```bash
python test.py
```

#### 🖨️ **Output:**

```
Hello, World!
```

# **Python Data Types**  

Python is a **dynamically typed** language, meaning you don’t need to declare data types explicitly.  

### **Basic Data Types in Python:**  

1. **Numeric Types**  
   - `int` – Whole numbers (e.g., `10`, `-5`)  
   - `float` – Decimal numbers (e.g., `10.5`, `-3.14`)  
   - `complex` – Complex numbers (e.g., `2 + 3j`)  

2. **Sequence Types**  
   - `str` – Text (e.g., `"Hello"`, `'Python'`)  
   - `list` – Ordered, mutable collection (e.g., `[1, "apple", True]`)  
   - `tuple` – Ordered, immutable collection (e.g., `(10, "banana")`)  

3. **Mapping Type**  
   - `dict` – Key-value pairs (e.g., `{"name": "John", "age": 30}`)  

4. **Set Types**  
   - `set` – Unordered, unique elements (e.g., `{1, 2, 3}`)  
   - `frozenset` – Immutable set (e.g., `frozenset({1, 2, 3})`)  

5. **Boolean Type**  
   - `bool` – `True` or `False`  

6. **Binary Types**  
   - `bytes` – Immutable binary data (e.g., `b"hello"`)  
   - `bytearray` – Mutable binary data (e.g., `bytearray(5)`)  

7. **None Type**  
   - `None` – Represents no value (e.g., `x = None`)  

---

### **1. Numeric Types**  
```python
# Integer (int)  
age = 25  
print(age, type(age))  # Output: 25 <class 'int'>  

# Float  
price = 19.99  
print(price, type(price))  # Output: 19.99 <class 'float'>  

# Complex  
z = 3 + 4j  
print(z, type(z))  # Output: (3+4j) <class 'complex'>  
```

---

### **2. Sequence Types**  
```python
# String (str)  
name = "Alice"  
print(name, type(name))  # Output: Alice <class 'str'>  

# List (mutable, ordered)  
fruits = ["apple", "banana", "cherry"]  
print(fruits, type(fruits))  # Output: ['apple', 'banana', 'cherry'] <class 'list'>  

# Tuple (immutable, ordered)  
coordinates = (10, 20)  
print(coordinates, type(coordinates))  # Output: (10, 20) <class 'tuple'>  
```

---

### **3. Dictionary (Mapping Type)**  
```python
# Dictionary (dict) – Key-value pairs  
person = {"name": "Bob", "age": 30}  
print(person, type(person))  # Output: {'name': 'Bob', 'age': 30} <class 'dict'>  
```

---

### **4. Set Types**  
```python
# Set (unordered, unique)  
unique_numbers = {1, 2, 2, 3}  
print(unique_numbers, type(unique_numbers))  # Output: {1, 2, 3} <class 'set'>  

# FrozenSet (immutable set)  
frozen_set = frozenset({1, 2, 3})  
print(frozen_set, type(frozen_set))  # Output: frozenset({1, 2, 3}) <class 'frozenset'>  
```

---

### **5. Boolean Type**  
```python
# Boolean (bool) – True or False  
is_active = True  
print(is_active, type(is_active))  # Output: True <class 'bool'>  
```

---

### **6. Binary Types**  
```python
# Bytes (immutable binary)  
byte_data = b"hello"  
print(byte_data, type(byte_data))  # Output: b'hello' <class 'bytes'>  

# ByteArray (mutable binary)  
byte_array = bytearray(5)  
print(byte_array, type(byte_array))  # Output: bytearray(b'\x00\x00\x00\x00\x00') <class 'bytearray'>  
```

---

### **7. None Type**  
```python
# None (no value)  
result = None  
print(result, type(result))  # Output: None <class 'NoneType'>  
```

---

### **Summary Table**  
| **Data Type**  | **Example** | **Mutable?** |
|--------------|------------|------------|
| `int` | `x = 10` | ❌ |
| `float` | `y = 3.14` | ❌ |
| `str` | `name = "Python"` | ❌ |
| `list` | `nums = [1, 2, 3]` | ✔️ |
| `tuple` | `point = (4, 5)` | ❌ |
| `dict` | `user = {"name": "Alice"}` | ✔️ |
| `set` | `unique = {1, 2, 3}` | ✔️ |
| `bool` | `flag = True` | ❌ |
| `bytes` | `data = b"abc"` | ❌ |
| `None` | `val = None` | ❌ |

These examples cover the most common Python data types with simple usage. 🚀

# **Understanding Python Keywords**

Let me explain Python keywords in a simpler way with clear examples.

## **What are Keywords?**
Keywords are special reserved words in Python that have specific meanings. You **cannot** use them as variable names or function names because Python uses them for its own operations.

### **Example of Invalid Usage**
```python
# This will give an error because 'if' is a keyword
if = 10  # ❌ Wrong!
```

---

## **Categories of Keywords with Simple Examples**

### 1️⃣ **True/False/None Keywords**
```python
# Boolean values
is_active = True  # ✅ Correct
is_blocked = False  # ✅ Correct

# None represents "no value"
result = None  # ✅ Correct
```

### 2️⃣ **Loop Keywords (`for`, `while`, `break`, `continue`)**
```python
# for loop
for i in [1, 2, 3]:
    print(i)  # Prints 1, 2, 3

# while loop
count = 0
while count < 3:
    print(count)
    count += 1  # Prints 0, 1, 2

# break exits the loop
for num in range(5):
    if num == 3:
        break  # Stops at 3
    print(num)  # Prints 0, 1, 2

# continue skips current iteration
for num in range(5):
    if num == 2:
        continue  # Skips 2
    print(num)  # Prints 0, 1, 3, 4
```

### 3️⃣ **Conditional Keywords (`if`, `elif`, `else`)**
```python
age = 18

if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
else:
    print("Adult")  # Prints "Adult"
```

### 4️⃣ **Function Keywords (`def`, `return`, `lambda`)**
```python
# def creates a function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Prints "Hello, Alice!"

# lambda makes small anonymous functions
square = lambda x: x * x
print(square(5))  # Prints 25
```

### 5️⃣ **Class Keywords (`class`)**
```python
class Dog:
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.bark()  # Prints "Woof!"
```

### 6️⃣ **Exception Handling (`try`, `except`, `finally`, `raise`)**
```python
# try-except handles errors
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Can't divide by zero!")  # Prints this

# finally always runs
try:
    file = open("test.txt")
except:
    print("Error occurred")
finally:
    print("This always runs")

# raise creates custom errors
if age < 0:
    raise ValueError("Age can't be negative!")
```

### 7️⃣ **Variable Scope (`global`, `nonlocal`)**
```python
x = 10  # Global variable

def change_x():
    global x  # Allows modifying global x
    x = 20

change_x()
print(x)  # Now prints 20
```

### 8️⃣ **Import Keywords (`import`, `from`, `as`)**
```python
import math  # Imports entire math module
print(math.sqrt(16))  # Prints 4.0

from datetime import datetime as dt  # Imports with alias
print(dt.now())  # Prints current time
```

### 9️⃣ **Other Important Keywords**
```python
# in checks membership
if "a" in "apple":
    print("Found 'a'")  # Prints this

# is checks identity (same object)
x = [1, 2]
y = [1, 2]
print(x == y)  # True (same values)
print(x is y)  # False (different objects)

# del deletes variables
nums = [1, 2, 3]
del nums[1]  # Removes 2
print(nums)  # [1, 3]
```

---

## **How to See All Keywords?**
```python
import keyword
print(keyword.kwlist)
```
This prints all Python keywords like `['False', 'None', 'True', 'and', 'as', ...]`

---

## **Key Points to Remember**
1. Keywords are **reserved** - you can't use them as variable names
2. Each keyword has a **specific purpose** in Python
3. They help control program flow (`if`, `for`), define functions (`def`), handle errors (`try`), etc.


# **Understanding Variables in Python**

Variables are like labeled containers that store data in your program. They give names to values so you can easily refer to them later.

## **Variable Rules in Python**

1. **Naming Rules**:
   - Must start with a **letter** (a-z, A-Z) or **underscore** (`_`)
     ```python
     name = "Alice"    # ✅ Valid
     _age = 25         # ✅ Valid
     1st_try = "test"  # ❌ Invalid (starts with number)
     ```
   
   - Can contain **letters, numbers, and underscores** (`_`)
     ```python
     user1 = "Bob"     # ✅ Valid
     total_score = 100  # ✅ Valid
     user-name = "Sam" # ❌ Invalid (hyphen not allowed)
     ```
   
   - **Case-sensitive** (different from other languages like SQL)
     ```python
     first_name = "Alice"
     First_Name = "Bob"  # Different variable!
     ```

   - **Cannot use Python keywords** (`if`, `for`, `while`, etc.)
     ```python
     class = "Math"  # ❌ Invalid ('class' is a keyword)
     ```

2. **Best Practices**:
   - Use **snake_case** (common in Python)
     ```python
     user_name = "Alice"  # ✅ Preferred
     userName = "Bob"     # ❌ Not Pythonic
     ```
   - Make names **descriptive** (not too short or vague)
     ```python
     n = 10        # ❌ Bad (what does 'n' mean?)
     item_count = 10  # ✅ Better
     ```

---

## **Variable Assignment & Reassignment**
Python variables are **dynamically typed**, meaning you can change their type.

```python
# Assigning a value
x = 10           # Integer
x = "Hello"      # Now a string (allowed in Python!)
x = [1, 2, 3]    # Now a list
```

### **Multiple Assignment**
```python
# Assign multiple variables at once
a, b, c = 1, 2, 3  

# Swap variables easily
x, y = 10, 20
x, y = y, x  # Now x=20, y=10
```

---

## **Variable Scope**
Where a variable is defined determines where it can be used.

### **1. Global Variables**
- Defined outside functions
- Can be accessed anywhere

```python
count = 0  # Global variable

def increment():
    global count  # Needed to modify global variable
    count += 1

increment()
print(count)  # Output: 1
```

### **2. Local Variables**
- Defined inside functions
- Only accessible within that function

```python
def greet():
    message = "Hello"  # Local variable
    print(message)

greet()
print(message)  # ❌ Error: 'message' not defined
```

---

## **Checking Variable Types**
Since Python is dynamically typed, you can check types with `type()`:

```python
x = 10
print(type(x))  # <class 'int'>

x = "Python"
print(type(x))  # <class 'str'>
```

---

## **Deleting Variables**
Use `del` to remove a variable:

```python
x = 100
print(x)  # 100
del x
print(x)  # ❌ Error: 'x' is not defined
```

---

## **Summary Table**
| **Concept**          | **Example**                          | **Notes**                          |
|----------------------|--------------------------------------|------------------------------------|
| Valid variable name  | `user_name`, `_count`, `item1`       | Letters, numbers, `_` allowed     |
| Invalid variable name | `1st_place`, `for`, `user-name`      | No numbers first, no keywords     |
| Case sensitivity     | `name ≠ Name ≠ NAME`                 | Treats as different variables     |
| Dynamic typing       | `x = 10` then `x = "Hello"`          | Type can change                   |
| Global vs local      | `global_var` vs `def func(): local_var` | Scope matters!                   |


# **Functions, Modules, and Packages in Python**

## **1. Functions**
Functions are reusable blocks of code that perform a specific task.

### **Defining a Function**
```python
def greet(name):
    """This function greets the user"""  # Docstring
    return f"Hello, {name}!"
```

### **Calling a Function**
```python
message = greet("Alice")
print(message)  # Output: Hello, Alice!
```

### **Function Parameters**
- **Positional arguments** (required)
- **Default arguments** (optional)
- **Keyword arguments** (explicit naming)
- **Variable-length arguments** (`*args`, `**kwargs`)

```python
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("Fido")  # Uses default animal_type
describe_pet(animal_type="hamster", pet_name="Harry")  # Keyword args
```

### **Lambda (Anonymous) Functions**
```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

---

## **2. Modules**
A module is a file containing Python definitions and statements (e.g., functions, classes,
or variables) that can be imported and used in other Python scripts

### **Creating a Module**
Save as `mymodule.py`:
```python
def add(a, b):
    return a + b

PI = 3.14159
```

### **Using a Module**
```python
import mymodule

print(mymodule.add(2, 3))  # Output: 5
print(mymodule.PI)         # Output: 3.14159
```

### **Import Options**
```python
from mymodule import add  # Import specific function
from mymodule import *    # Import everything (not recommended)
import mymodule as mm     # Alias
```

### **Built-in Modules**
```python
import math
print(math.sqrt(16))  # Output: 4.0

import random
print(random.randint(1, 10))  # Random number between 1-10
```

---

## **3. Packages**
A package is a collection of Python modules organized in directories. Each
package contains an __init__.py file, which signifies that the directory is a Python
package. Packages help you organize related modules into a hierarchy.

### **Creating a Package**
```
my_package/
│── __init__.py  (Required to make it a package)
│── module1.py
│── module2.py
```

### **Using a Package**
```python
from my_package import module1
from my_package.module2 import some_function
```

### **Popular Python Packages**
- **NumPy**: Scientific computing
- **Pandas**: Data analysis
- **Matplotlib**: Data visualization
- **Requests**: HTTP requests
- **Django**: Web development

Install packages using pip:
```bash
pip install numpy pandas
```

---

## **Key Differences**
| Concept       | Description                          | Example                     |
|--------------|--------------------------------------|----------------------------|
| **Function** | Reusable code block                  | `def add(a, b): return a+b` |
| **Module**   | Single Python file with code         | `math.py`                  |
| **Package**  | Directory of modules                 | `numpy/`                   |

---

## **Best Practices**
1. **Functions**:
   - Keep them small and focused
   - Use descriptive names
   - Document with docstrings

2. **Modules**:
   - Group related functionality
   - Avoid circular imports

3. **Packages**:
   - Use `__init__.py` for initialization
   - Follow Python naming conventions


# **Command-Line Arguments & Environment Variables in Python**

## **1. Command-Line Arguments (CLI)**

Command Line Arguments in Python allow a user to provide input to a Python script
when it is executed from the command line. This is useful for passing options, filenames,
or parameters to scripts at runtime.
In Python, command line arguments are stored in the sys.argv list, provided by the sys
module.
Using sys.argv
The sys.argv list contains the arguments passed to the script:
➢ sys.argv[0] is the name of the script itself.
➢ sys.argv[1], sys.argv[2], etc., represent the arguments passed to the script.

### **Using `sys.argv` (Basic)**
```python
import sys

# Example: python script.py arg1 arg2
print("Script name:", sys.argv[0])  # script.py
print("Arguments:", sys.argv[1:])   # ['arg1', 'arg2']
```

### **Using `argparse` (Recommended)**
More powerful argument parsing:
```python
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
```
Run with:
```bash
python script.py 1 2 3 4 --sum  # Output: 10
python script.py 1 2 3 4        # Output: 4 (default max)
```

### **Using `click` (For Complex CLI Apps)**
```python
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    hello()
```

---

## **2. Environment Variables**

Environment variables are dynamic variables maintained by the operating system that
can affect the way running processes behave. They are often used for configuration
settings, like database credentials, API keys, or system paths, and provide a way to pass
information into a program without hardcoding it

- In Python, environment variables can be accessed using the os module.
- You can use the os.environ dictionary to access environment variables.

### **Accessing Environment Variables**
```python
import os

# Get an environment variable
db_host = os.getenv('DB_HOST', 'localhost')  # 2nd arg is default

# Get all environment variables
print(os.environ)  # Dictionary of all env vars
```

### **Setting Environment Variables**

#### **Temporarily in Python**
```python
import os
os.environ['API_KEY'] = '12345'  # Only affects current process
```

#### **Permanently (System-Wide)**
- **Linux/macOS**: Add to `~/.bashrc` or `~/.zshrc`
  ```bash
  export DB_HOST="localhost"
  export DB_PORT="5432"
  ```
- **Windows**: Use System Properties or PowerShell
  ```powershell
  [Environment]::SetEnvironmentVariable("DB_HOST", "localhost", "User")
  ```

### **Using `.env` Files (Recommended for Development)**
1. Install python-dotenv:
   ```bash
   pip install python-dotenv
   ```
2. Create `.env` file:
   ```ini
   DB_HOST=localhost
   DB_PORT=5432
   SECRET_KEY=supersecret
   ```
3. Load in Python:
   ```python
   from dotenv import load_dotenv
   load_dotenv()  # Loads variables from .env

   db_host = os.getenv('DB_HOST')
   ```

---

## **Best Practices**
1. **For CLI Arguments**:
   - Use `argparse` for simple scripts
   - Use `click` for complex CLI applications
   - Always provide help messages

2. **For Environment Variables**:
   - Never commit `.env` files to version control
   - Use `python-dotenv` for development
   - For production, set vars in deployment environment

3. **Security**:
   - Keep sensitive data (API keys, passwords) in env vars
   - Never hardcode secrets in your code

## **Example: Combining Both**
```python
import os
import argparse
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument('--env', choices=['dev', 'prod'], default='dev')
args = parser.parse_args()

if args.env == 'prod':
    db_host = os.getenv('PROD_DB_HOST')
else:
    db_host = os.getenv('DEV_DB_HOST')

print(f"Connecting to {db_host}")
```

# **Python Operators**

Operators are special symbols in Python that perform operations on variables and values. Here's a comprehensive overview of all operator types with examples:

## **1. Arithmetic Operators**
Used for mathematical calculations:

| Operator | Name           | Example   | Result |
|----------|----------------|-----------|--------|
| `+`      | Addition       | `5 + 2`   | 7      |
| `-`      | Subtraction    | `5 - 2`   | 3      |
| `*`      | Multiplication | `5 * 2`   | 10     |
| `/`      | Division       | `5 / 2`   | 2.5    |
| `%`      | Modulus        | `5 % 2`   | 1      |
| `**`     | Exponentiation | `5 ** 2`  | 25     |
| `//`     | Floor Division | `5 // 2`  | 2      |

```python
print(10 / 3)   # 3.333... (float division)
print(10 // 3)  # 3 (integer division)
```

## **2. Comparison Operators**
Return `True` or `False` by comparing values:

| Operator | Name                  | Example   | Result |
|----------|-----------------------|-----------|--------|
| `==`     | Equal                 | `5 == 2`  | False  |
| `!=`     | Not equal             | `5 != 2`  | True   |
| `>`      | Greater than          | `5 > 2`   | True   |
| `<`      | Less than             | `5 < 2`   | False  |
| `>=`     | Greater than or equal | `5 >= 5`  | True   |
| `<=`     | Less than or equal    | `5 <= 2`  | False  |

```python
age = 18
print(age >= 18)  # True (eligible to vote)
```

## **3. Logical Operators**
Combine conditional statements:

| Operator | Description                          | Example                     |
|----------|--------------------------------------|----------------------------|
| `and`    | True if both are true                | `x > 5 and x < 10`          |
| `or`     | True if at least one is true         | `x > 5 or x < 4`            |
| `not`    | Reverse the result                   | `not(x > 5)`                |

```python
balance = 1500
withdraw = 1200
print(balance >= withdraw and withdraw <= 1000)  # False
```

## **4. Assignment Operators**
Assign values to variables:

| Operator | Example    | Equivalent to |
|----------|------------|---------------|
| `=`      | `x = 5`    | `x = 5`       |
| `+=`     | `x += 3`   | `x = x + 3`   |
| `-=`     | `x -= 3`   | `x = x - 3`   |
| `*=`     | `x *= 3`   | `x = x * 3`   |
| `/=`     | `x /= 3`   | `x = x / 3`   |
| `%=`     | `x %= 3`   | `x = x % 3`   |
| `**=`    | `x **= 3`  | `x = x ** 3`  |
| `//=`    | `x //= 3`  | `x = x // 3`  |

```python
counter = 10
counter += 1  # Increment by 1
print(counter)  # 11
```

## **5. Identity Operators**
Compare object memory locations:

| Operator | Description              | Example       |
|----------|--------------------------|---------------|
| `is`     | True if same object      | `x is y`      |
| `is not` | True if not same object  | `x is not y`  |

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)     # True (same object)
print(a is c)     # False (different objects)
print(a == c)     # True (same values)
```

## **6. Membership Operators**
Test if value exists in sequence:

| Operator | Description                    | Example       |
|----------|--------------------------------|---------------|
| `in`     | True if value exists           | `x in y`      |
| `not in` | True if value doesn't exist    | `x not in y`  |

```python
fruits = ["apple", "banana"]
print("banana" in fruits)    # True
print("orange" not in fruits) # True
```

## **7. Bitwise Operators**
Work on binary representations:

| Operator | Name            | Example   | Result (Binary) |
|----------|-----------------|-----------|-----------------|
| `&`      | AND             | `5 & 3`   | `0101 & 0011 = 0001` (1) |
| `\|`     | OR              | `5 \| 3`  | `0101 \| 0011 = 0111` (7) |
| `^`      | XOR             | `5 ^ 3`   | `0101 ^ 0011 = 0110` (6) |
| `~`      | NOT             | `~5`      | Inverts bits     |
| `<<`     | Left shift      | `5 << 1`  | `0101 << 1 = 1010` (10) |
| `>>`     | Right shift     | `5 >> 1`  | `0101 >> 1 = 0010` (2) |

```python
print(5 & 3)   # 1
print(5 | 3)   # 7
print(5 << 1)  # 10 (multiply by 2)
print(5 >> 1)  # 2 (divide by 2)
```

## **Operator Precedence**
Order of operations (highest to lowest):
1. `()` (Parentheses)
2. `**` (Exponentiation)
3. `~ + -` (Bitwise NOT, Unary plus/minus)
4. `* / % //` (Multiplication, Division, etc.)
5. `+ -` (Addition, Subtraction)
6. `<< >>` (Bit shifts)
7. `&` (Bitwise AND)
8. `^` (Bitwise XOR)
9. `|` (Bitwise OR)
10. `== != > < >= <=` (Comparisons)
11. `is`, `is not`, `in`, `not in` (Identity/Membership)
12. `not` (Logical NOT)
13. `and` (Logical AND)
14. `or` (Logical OR)

```python
result = 5 + 3 * 2  # 11 (not 16)
print(result)
```


Run with:
```bash
python script.py --env prod
``` 
# **Condition Handling in Python**

Condition handling allows your programs to make decisions and handle different scenarios. Python provides several ways to manage conditions:

## **1. Basic Conditional Statements (`if`, `elif`, `else`)**

```python
age = 18

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")  # This will execute
```

### **Key Features:**
- `if`: First condition to check
- `elif`: Additional conditions (optional, multiple allowed)
- `else`: Final fallback (optional)

## **2. Ternary Operator (Conditional Expression)**

A compact way to write simple `if-else` statements:

```python
# Syntax: value_if_true if condition else value_if_false
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: "Adult"
```

## **3. Handling Multiple Conditions**

Combine conditions using logical operators (`and`, `or`, `not`):

```python
temperature = 25
is_summer = True

if temperature > 30 or (is_summer and temperature > 25):
    print("It's hot!")
elif not is_summer and temperature < 10:
    print("It's cold!")
else:
    print("Pleasant weather")
```

## **4. Truthy and Falsy Values**

Python evaluates non-boolean values in conditions:
- **Falsy**: `False`, `0`, `""`, `None`, `[]`, `{}`, `()`
- **Truthy**: Everything else

```python
name = ""

if name:  # Falsy check
    print(f"Hello, {name}")
else:
    print("Name is empty")  # This executes
```

## **5. Exception Handling (`try`, `except`, `finally`)**

Handle runtime errors gracefully:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
else:
    print("No errors occurred")  # Runs if no exception
finally:
    print("This always executes")  # Cleanup code
```

### **Common Exception Types:**
- `ZeroDivisionError`: Division by zero
- `TypeError`: Incorrect type operation
- `ValueError`: Invalid value
- `FileNotFoundError`: Missing file
- `KeyError`: Missing dictionary key
- `IndexError`: List index out of range

## **6. Raising Exceptions (`raise`)**

Forcefully trigger exceptions when needed:

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age < 18:
        print("Not eligible")
    else:
        print("Eligible")

try:
    validate_age(-5)  # Raises ValueError
except ValueError as e:
    print(e)  # Output: "Age cannot be negative"
```

## **7. Using `assert` for Debugging**

Check conditions during development (disabled with `-O` flag):

```python
def calculate_discount(price, discount):
    assert 0 <= discount <= 1, "Discount must be between 0 and 1"
    return price * (1 - discount)

# Fails if discount is invalid
print(calculate_discount(100, 0.2))  # 80.0
```

## **8. Pattern Matching (Python 3.10+)**

Advanced conditional logic with structural pattern matching:

```python
def handle_response(response):
    match response:
        case 200:
            print("Success")
        case 404:
            print("Not found")
        case 500 | 503:  # Multiple values
            print("Server error")
        case _:  # Default case
            print("Unknown status code")

handle_response(404)  # Output: "Not found"
```

## **Best Practices**
1. **Keep conditions simple** - Break complex logic into smaller checks
2. **Use specific exceptions** - Catch only what you can handle
3. **Avoid empty except blocks** - Always handle or log errors
4. **Prefer `try/except` over `if/else`** for expected error cases
5. **Document your conditions** - Especially complex business rules

```python
# Good practice example
def process_data(data):
    """Process input data with validation."""
    if not data:  # Explicit check
        raise ValueError("No data provided")
    
    try:
        return complex_operation(data)
    except DatabaseError as e:
        log_error(e)
        return None
```
# **Lists and Tuples in Python**

## **1. Lists (Mutable Sequences)**
Lists are ordered, changeable collections that allow duplicate elements.

### **Creating Lists**
```python
fruits = ["apple", "banana", "cherry"]  # Using square brackets
numbers = list((1, 2, 3))              # Using list() constructor
mixed = [1, "hello", True, 3.14]       # Can hold different types
```

### **List Operations**
| Operation | Example | Result |
|-----------|---------|--------|
| Access | `fruits[1]` | `"banana"` |
| Slice | `fruits[1:3]` | `["banana", "cherry"]` |
| Length | `len(fruits)` | `3` |
| Add item | `fruits.append("orange")` | `["apple", "banana", "cherry", "orange"]` |
| Insert | `fruits.insert(1, "mango")` | `["apple", "mango", "banana", "cherry"]` |
| Remove | `fruits.remove("banana")` | `["apple", "cherry"]` |
| Pop | `fruits.pop(1)` | Removes and returns `"banana"` |
| Concatenate | `[1, 2] + [3, 4]` | `[1, 2, 3, 4]` |
| Repeat | `[0] * 3` | `[0, 0, 0]` |
| Check existence | `"apple" in fruits` | `True` |

### **List Methods**
```python
nums = [5, 2, 8, 1]
nums.sort()                # [1, 2, 5, 8]
nums.reverse()             # [8, 5, 2, 1]
nums_copy = nums.copy()    # Creates shallow copy
nums.clear()               # Empties the list
```

### **List Comprehensions**
```python
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

---

## **2. Tuples (Immutable Sequences)**
Tuples are ordered, unchangeable collections that allow duplicate elements.

### **Creating Tuples**
```python
colors = ("red", "green", "blue")  # Using parentheses
point = tuple((3, 4))             # Using tuple() constructor
single = ("hello",)               # Single-element tuple (note comma)
```

### **Tuple Operations**
| Operation | Example | Result |
|-----------|---------|--------|
| Access | `colors[1]` | `"green"` |
| Slice | `colors[1:3]` | `("green", "blue")` |
| Length | `len(colors)` | `3` |
| Concatenate | `(1, 2) + (3, 4)` | `(1, 2, 3, 4)` |
| Repeat | `(0,) * 3` | `(0, 0, 0)` |
| Check existence | `"red" in colors` | `True` |

### **Tuple Methods**
```python
index = colors.index("green")  # Returns 1
count = colors.count("red")    # Returns 1
```

### **When to Use Tuples**
- When you need an immutable sequence
- For fixed collections (days of week, RGB colors)
- As dictionary keys (lists can't be keys)
- For function return values (multiple returns)

---

## **Key Differences**
| Feature | List | Tuple |
|---------|------|-------|
| Mutability | Mutable (can change) | Immutable (can't change) |
| Syntax | `[ ]` | `( )` |
| Performance | Slightly slower | Faster |
| Methods | Many (append, remove, etc.) | Few (count, index) |
| Use Case | Dynamic data | Fixed data |

---

## **Common Patterns**
### **Unpacking**
```python
# Lists
x, y, z = [1, 2, 3]

# Tuples
name, age = ("Alice", 25)
```

### **Converting Between Types**
```python
tuple_from_list = tuple([1, 2, 3])  # (1, 2, 3)
list_from_tuple = list(("a", "b"))  # ["a", "b"]
```

### **Nested Structures**
```python
# List of tuples
coordinates = [(1, 2), (3, 4), (5, 6)]

# Tuple of lists
mixed = ([1, 2], ["a", "b"])
```

---

## **Best Practices**
1. **Use lists** when you need to modify the collection
2. **Use tuples** for fixed data that shouldn't change
3. **Prefer tuples** for heterogeneous data (different types)
4. **Use lists** for homogeneous data (same types)
5. **Consider tuples** when you need dictionary keys

---

# **Loops in Python: `for` and `while`**

## **1. `for` Loops**
Used for iterating over sequences (lists, tuples, strings, etc.) or a range of numbers.

### **Basic Syntax**
```python
for item in sequence:
    # Code to execute
```

### **Common Use Cases**

#### **Loop through a list**
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
Output:
```
apple
banana
cherry
```

#### **Loop with range()**
```python
for i in range(5):      # 0 to 4
    print(i)

for i in range(1, 6):   # 1 to 5
    print(i)

for i in range(0, 10, 2):  # 0 to 8, step 2
    print(i)
```

#### **Loop through a string**
```python
for char in "Python":
    print(char)
```

#### **Loop with index using enumerate()**
```python
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
```

### **Nested `for` Loops**
```python
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")
```

### **`for-else` Clause**
The `else` block executes after the loop completes normally (without `break`):
```python
for num in [1, 3, 5]:
    if num % 2 == 0:
        print("Even found")
        break
else:
    print("No evens found")  # This executes
```

---

## **2. `while` Loops**
Execute a block of code as long as a condition is true.

### **Basic Syntax**
```python
while condition:
    # Code to execute
```

### **Common Use Cases**

#### **Basic counter**
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

#### **User input validation**
```python
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")
```

#### **Infinite loop with break**
```python
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == "quit":
        break
    print(f"You entered: {user_input}")
```

### **`while-else` Clause**
The `else` block executes if the loop completes normally (without `break`):
```python
n = 5
while n > 0:
    print(n)
    n -= 1
else:
    print("Countdown complete!")
```

---

## **Key Differences**

| Feature | `for` Loop | `while` Loop |
|---------|-----------|-------------|
| **When to use** | When you know iteration count | When you don't know iteration count |
| **Initialization** | Automatic | Manual |
| **Termination** | When sequence ends | When condition becomes false |
| **Common uses** | Lists, ranges, strings | User input, game loops |

---

## **Loop Control Statements**

### **`break`**
Exit the loop immediately:
```python
for num in range(10):
    if num == 5:
        break
    print(num)  # Prints 0-4
```

### **`continue`**
Skip to next iteration:
```python
for num in range(5):
    if num == 2:
        continue
    print(num)  # Prints 0,1,3,4
```

### **`pass`**
Placeholder for empty loops:
```python
for item in sequence:
    pass  # TODO: Implement later
```

---

## **Best Practices**
1. Use `for` when iterating over known sequences
2. Use `while` for conditions that may change unpredictably
3. Avoid infinite loops (ensure exit condition will be met)
4. Use meaningful loop variable names (`for user in users` vs `for x in y`)
5. Consider list comprehensions for simple transformations

```python
# Instead of:
squares = []
for num in range(5):
    squares.append(num**2)

# Use:
squares = [num**2 for num in range(5)]
```

Both loops are essential tools in Python programming - choose the right one based on your specific needs!

Great! You're starting to combine **lists** and **user input**, which is a solid step toward building interactive Python programs. Let's **deep dive** into list exercises with examples to help you really get comfortable with them.

---

## 🧠 Understanding Lists in Python

A **list** is a collection of items that is ordered and changeable. Lists are written with square brackets `[]`.

### ✅ Example:
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
```

---

## 🧪 Interactive List Exercises

### 🔹 **1. Create a list from user input**
Let’s ask the user to enter 5 favorite fruits and store them in a list:

```python
fruits = []
for i in range(5):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)

print("Your favorite fruits are:", fruits)
```

### 🔹 **2. Access and print specific elements**
```python
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
```

---

### 🔹 **3. Check if an item is in the list**
```python
search = input("Enter a fruit to check if it's in your list: ")
if search in fruits:
    print(f"Yes, {search} is in your list.")
else:
    print(f"No, {search} is not in your list.")
```

---

### 🔹 **4. Remove an item from the list**
```python
remove_item = input("Enter a fruit to remove from your list: ")
if remove_item in fruits:
    fruits.remove(remove_item)
    print(f"{remove_item} has been removed.")
else:
    print(f"{remove_item} is not in the list.")

print("Updated list:", fruits)
```

---

### 🔹 **5. Sort and reverse the list**
```python
fruits.sort()
print("Sorted list:", fruits)

fruits.reverse()
print("Reversed list:", fruits)
```

---

### 🧑‍💻 Pro Tip: f-Strings
In your example:
```python
name = input("Enter your name: ")
print("Hello, {name}!")  # ❌ This will print the text as-is
```

You should use an `f-string` to insert variables:
```python
print(f"Hello, {name}!")  # ✅ This prints the actual value
```

---
# **Dictionaries and Sets in Python**

## **1. Dictionaries (dict)**
Dictionaries are **unordered, mutable** collections of **key-value pairs**.

### **Creating Dictionaries**
```python
# Method 1: Curly braces
person = {"name": "Alice", "age": 25, "city": "New York"}

# Method 2: dict() constructor
person = dict(name="Alice", age=25, city="New York")

# Method 3: From list of tuples
person = dict([("name", "Alice"), ("age", 25)])
```

### **Dictionary Operations**
| Operation | Example | Description |
|-----------|---------|-------------|
| Access | `person["name"]` | Gets value for key ("Alice") |
| Add/Update | `person["job"] = "Engineer"` | Adds new key-value pair |
| Remove | `del person["age"]` | Deletes key-value pair |
| Check Key | `"name" in person` | Returns `True`/`False` |
| Length | `len(person)` | Number of key-value pairs |
| Get Keys | `person.keys()` | Returns view of keys |
| Get Values | `person.values()` | Returns view of values |
| Get Items | `person.items()` | Returns view of (key, value) pairs |

### **Dictionary Methods**
```python
person = {"name": "Alice", "age": 25}

# Get value (with default)
age = person.get("age", 0)  # Returns 25 if key exists, else 0

# Remove and return value
job = person.pop("job", None)  # Returns None if key doesn't exist

# Update dictionary
person.update({"age": 26, "city": "Boston"})

# Clear dictionary
person.clear()
```

### **Dictionary Use Cases**
- Storing related attributes (user profiles, configurations)
- Fast lookups by key (O(1) time complexity)
- Counting occurrences (word frequency)
- JSON-like data structures

```python
# Counting word frequency
text = "apple banana apple orange banana"
words = text.split()
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
# Result: {'apple': 2, 'banana': 2, 'orange': 1}
```

---

## **2. Sets (set and frozenset)**
Sets are **unordered, mutable** collections of **unique elements**.

### **Creating Sets**
```python
# Method 1: Curly braces
fruits = {"apple", "banana", "cherry"}

# Method 2: set() constructor
fruits = set(["apple", "banana", "cherry"])

# Immutable set
constants = frozenset([3.14, 2.71, 1.61])
```

### **Set Operations**
| Operation | Example | Description |
|-----------|---------|-------------|
| Add | `fruits.add("orange")` | Adds element |
| Remove | `fruits.remove("banana")` | Removes element (raises error if missing) |
| Discard | `fruits.discard("banana")` | Removes if exists (no error) |
| Pop | `fruits.pop()` | Removes and returns arbitrary element |
| Length | `len(fruits)` | Number of elements |
| Check Membership | `"apple" in fruits` | Returns `True`/`False` |

### **Set Methods**
```python
a = {1, 2, 3}
b = {3, 4, 5}

# Union
print(a | b)  # {1, 2, 3, 4, 5}

# Intersection
print(a & b)  # {3}

# Difference
print(a - b)  # {1, 2}

# Symmetric Difference (elements in either but not both)
print(a ^ b)  # {1, 2, 4, 5}
```

### **Set Use Cases**
- Removing duplicates from a list
- Membership testing (faster than lists)
- Mathematical set operations (unions, intersections)
- Finding unique elements

```python
# Remove duplicates
numbers = [1, 2, 2, 3, 3, 3]
unique = set(numbers)  # {1, 2, 3}

# Fast membership testing
if "apple" in fruits:  # Faster than list for large collections
    print("Found!")
```

---

## **Key Differences**

| Feature | Dictionary | Set |
|---------|-----------|-----|
| **Elements** | Key-value pairs | Unique values |
| **Order** | Unordered (Python 3.7+ preserves insertion order) | Unordered |
| **Mutability** | Mutable | Mutable (except frozenset) |
| **Syntax** | `{key: value}` | `{value}` or `set()` |
| **Use Case** | Associative data storage | Unique collection, membership tests |

---

## **Best Practices**
1. **Dictionaries**:
   - Use descriptive keys
   - Handle missing keys with `.get()` or `try/except`
   - Use dictionary comprehensions for transformations

```python
# Dictionary comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, ...}
```

2. **Sets**:
   - Convert lists to sets to remove duplicates
   - Use for fast membership testing
   - Leverage set operations for comparisons

```python
# Finding common elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)  # {3, 4}
```

