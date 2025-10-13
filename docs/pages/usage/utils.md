General auxiliary methods:

```python
from xloft.converters import to_human_size
from xloft.itis import is_number
from ramifice.utils.tools import (
    get_file_size,
    hash_to_obj_id,
    is_color,
    is_email,
    is_ip,
    is_mongo_id,
    is_password,
    is_phone,
    is_url,
    normal_email,
)


# Convert the number of bytes into a human-readable format.
size: str = to_human_size(2097152)
print(size)  # => 2 MB

# Check if a string is a number.
if is_number("5"):
    ...

# Validate Password.
if is_password("12345678"):
    ...

# Validate Email address.
if await is_email("kebasyaty@gmail.com"):
    ...

# Normalizing email address.
# Use this before requeste to a database.
# For example, on the login page.
email: str | None = normal_email("kebasyaty@gmail.com")  # None, if not valid

# Validate URL address.
if is_url("https://www.google.com"):
    ...

# Validate IP address.
if is_ip("127.0.0.1"):
    ...

# Validate Color code.
if is_color("#000"):
    ...

# Validate Phone number.
if is_phone("+447986123456"):
    ...

# Validation of the Mongodb identifier.
if is_mongo_id("666f6f2d6261722d71757578"):
    ...

# Get ObjectId from hash string.
from bson.objectid import ObjectId
_id: ObjectId | None = hash_to_obj_id("666f6f2d6261722d71757578")

# Get file size in bytes.
path = "public/media/default/no_doc.odt"
size: int = get_file_size(path)
print(size)  # => 9843
```
