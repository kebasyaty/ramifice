Examples of frequently used methods:

```py title="main.py" linenums="1"
# Check data validity.
# The main use is to check data from web forms.
# It is also used to verify Models that do not migrate to the database.
user = User()
if not await user.is_valid():
    user.print_err()  # Convenient to use during development.

# Create or update document in database.
# This method pre-uses the `check` method.
user = User()
if not await user.save():
    user.print_err()  # Convenient to use during development.

# Delete document from database.
user = User()
await user.delete()
# or
await user.delete(remove_files=False)

# Verification, replacement and recoverang of password.
user = User()
await user.verify_password(password="12345678")
await user.update_password(  # + verify_password
  old_password="12345678",
  new_password="O2eA4GIr38KGGlS",
)
```
