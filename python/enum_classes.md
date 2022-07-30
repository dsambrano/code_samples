# Enum

Enum is an import that a class will depend on. Its most effective use case is to give a list of options available to a class. For example, if you only want to have 3 possible options for employees and let users create an employee (but its only one of those, this is how you do it:

```python
from enum import Enum, auto

class EmpRole(Enum):
    CEO = auto() # Can either be auto or an actual number (short hand can be range). Auto is preferred to improve readablity in version control
    MANAGER = auto()
    STAFF = auto()

def main():
    my_role = EmpRole.MANAGER
    print(my_role)
    print(my_role.value) # to print the value, in this case 2.

if __name__ == "__main__":
    main()

```

[source][https://youtu.be/kIsTFApllIQ]
