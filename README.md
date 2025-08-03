# banned_username

A Python module to check whether a given username is allowed based on a predefined list of banned words.

This project helps to prevent the use of inappropriate, reserved, or system-related usernames in web applications or other services.

## Features

- Fast validation of usernames against a list of banned or reserved words
- Easily integrable with Django or other Python-based backends
- Customizable word list

## Installation

You can install the package using `pip`:

```bash
pip install git+https://github.com/makszubkov/banned_username.git

Or clone the repository:

git clone https://github.com/makszubkov/banned_username.git
cd banned_username
pip install .

Usage

from banned_username import is_banned

# Returns True if the username is banned
print(is_banned("admin"))  # True
print(is_banned("john_doe"))  # False

Custom Word List

You can pass a custom list of banned words:

from banned_username import is_banned, set_banned_list

set_banned_list(["badword", "root", "support"])

print(is_banned("root"))  # True
print(is_banned("user123"))  # False

Integration with Django

This module can be used in Django validators or forms to enforce clean username policies.

Example:

from django.core.exceptions import ValidationError
from banned_username import is_banned

def validate_username(value):
    if is_banned(value):
        raise ValidationError("This username is not allowed.")
