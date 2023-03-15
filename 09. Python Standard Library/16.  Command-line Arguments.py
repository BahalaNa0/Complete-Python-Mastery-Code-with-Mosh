"""
9. Python Standard Library, 16. Command-line Arguments

For scripts that expect command line arguments.
"""
import sys

if len(sys.argv) == 1:
    print("Usage: python3 app.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)
