# Basic SHA256 Hashing using Python

Hashing is an important aspect of cryptography, it ensures the integrity of data. The standard python modules includes an easy solution for hashing called `hashlib`

## There are two types of hashing
1. Plaintext/string hashing
2. File hashing

## Plaintext/string hashing

A simple conversion of a normal string of text into a hashed value via a hashing function.

Since the `hashlib` module already provides us a simple solution to hashing, all we need to do is implement it as a function.

```python
import hashlib

def plaintext_to_hash (plaintext : str) -> str:
    hashed  =   hashlib.sha256 (plaintext.encode ()).hexdigest ()
    return hashed
```

1. Create a function called `plaintext_to_hash` which accepts a `string` called `plaintext`
2. Create a new temp variable called `hashed`
3. Using the `hashed` variable, use the `sha256` class constructor to create a hexdigest with the plaintext as input.
4. Before `sha256` constructor can use the plaintext, it needs to the string to be converted into bytes format.
5. Use the `hashed` variable as a return value

Another alternative to implement this is as below:

```python
import hashlib

def plaintext_to_hash (plaintext : str) -> str:
    converted_plaintext     =   plaintext.encode()

    hashed  =   hashlib.sha256 (converted_plaintext).hexdigest ()
    return hashed
```

or

```python
import hashlib

def plaintext_to_hash (plaintext : str) -> str:
    return hashlib.sha256 (plaintext.encode ()).hexdigest ()
```

To run the program insert the `__main__` condition with the function as the entrypoint

```python
import hashlib

def plaintext_to_hash (plaintext : str) -> str:
    converted_plaintext     =   plaintext.encode()

    hashed  =   hashlib.sha256 (converted_plaintext).hexdigest ()
    return hashed

if __name__ == '__main__':
    plaintext_to_hash ("Hello")
```

## File hashing

Converts the binary byte value of a file into a hashed value.

A single file called `python_logo.png` has been included as a control to compare hashes.

|File | SHA256 hash |
|-----|-------------|
| python_logo.png |0c7ed65195c7eec856ab87c70673a4e4828effccb15ddd5144d1a89a4373ab49|

File hashing takes a different approach compared to plaintext hashing. If the same approach were used, the output would not be accurate because a file path is the same as a string, and the file path itself would be converted into a digest.

To hash a file, the bytes contained within the file must be converted byte by byte into a hex digest.

### Opening the file

```python
import hashlib

def file_to_hash (file_path : str) -> str:

    with open (file_path, 'rb+') as file:

```

1. Create a function called `file_to_hash` which accepts a file path called `file_path`.
2. using the `open ()` function open the file by providing the `file_path` as the first argument and the mode as binary read +write.

### Convert the file bytes into hash.

When you open a file, the bytes are available to be read using the `read ()` member function of class type. When calling the `read ()` function it returns a string of bytes.


```python
import hashlib

def file_to_hash (file_path : str) -> str:

    bin_digest : str

    with open (file_path, 'rb+') as file:
        file_bytes  =   file.read ()

        bin_digest  =   hashlib.sha256 (file_bytes).hexdigest ()

    return bin_digest
```

1. Create a function wide variable called `bin_digest`
2. Get the file bytes using `read ()` function and store them into a temp variable called `file_bytes`
3. Using the `bin_digest` variable, store the sha256 hex digest.
4. To get the hex digest, put the `file_bytes` variable as the sha256 parameter.
5. Return the `bin_digest` variable as the return value

Alternatively, a shorter version can be implemented

```python
import hashlib

def file_to_hash (file_path : str) -> str:

    with open (file_path, 'rb+') as file:
        return hashlib.sha256 (file.read()).hexdigest ()
```

To test the function, replace the entrypoint function in `__name__`

```python
import hashlib

def plaintext_to_hash (plaintext : str) -> str:
    converted_plaintext     =   plaintext.encode()

    hashed  =   hashlib.sha256 (converted_plaintext).hexdigest ()
    return hashed

def file_to_hash (file_path : str) -> str:

    with open (file_path, 'rb+') as file:
        return hashlib.sha256 (file.read()).hexdigest ()

if __name__ == '__main__':
    file_to_hash ("python_logo.png")
```

## Combining the two function into a single program

We are able to combine both the function and create a single python program by using the basic python program structure and the `argparse` module

```
sha256
|---  __main__.py
|---  sha256.py
```

Create a file called `__main__.py` to tell the program about the entrypoint of the program

```python
from .sha256 import main

if __name__ == "__main__":
    main()
```

Then in the `sha256.py` file, create a main function and include the `argparse` module


```python
import hashlib
import argparse

def plaintext_to_hash (plaintext : str) -> str:
    converted_plaintext     =   plaintext.encode()

    hashed  =   hashlib.sha256 (converted_plaintext).hexdigest ()
    return hashed

def file_to_hash (file_path : str) -> str:

    with open (file_path, 'rb+') as file:
        return hashlib.sha256 (file.read()).hexdigest ()

def main ():

if __name__ == '__main__':
    main ()
```

### Creating the argparse context for CLI interaction

Calling the `argparse.ArgumentParse ()` function we are able to create a simple CLI interface with `-h` commands

```python
import hashlib
import argparse

def plaintext_to_hash (plaintext : str) -> str:
    converted_plaintext     =   plaintext.encode()

    hashed  =   hashlib.sha256 (converted_plaintext).hexdigest ()
    return hashed

def file_to_hash (file_path : str) -> str:

    with open (file_path, 'rb+') as file:
        return hashlib.sha256 (file.read()).hexdigest ()

def main ():
    input_parse     =   argparse.ArgumentParser (description="A simple SHA256 hashing program")

    parse   =   input_parse.parse_args ()

if __name__ == '__main__':
    main ()
```
1. Create the argument parser context
2. Assign the argument parse input to the `parse` variable

Once the simple format is implemented we are able to add additional parameter and help information

```python
import hashlib
import argparse

def plaintext_to_hash (plaintext : str) -> str:
    converted_plaintext     =   plaintext.encode()

    hashed  =   hashlib.sha256 (converted_plaintext).hexdigest ()
    return hashed

def file_to_hash (file_path : str) -> str:

    with open (file_path, 'rb+') as file:
        return hashlib.sha256 (file.read()).hexdigest ()

def main ():
    input_parse     =   argparse.ArgumentParser (description="A simple SHA256 hashing program")
    input_parse.add_argument ("plaintext", metavar="plaintext", help="A string of characters or a file path")
    input_parse.add_argument('--file', dest="hasher", action="store_const",
                            const=file_to_hash, default=plaintext_to_hash)

    parse   =   input_parse.parse_args ()
    print (parse.hasher (parse.plaintext))

if __name__ == '__main__':
    main ()
```
1. Add an arguement called `plaintext` with the information for the argument field
2. Add another argument `--file` and set the `parser` destination to `hasher` in order to called it.
3. The action for the second argument is a `store_const` action which allows the program to decide the default and const path.
4. Using the `print ()` function called the `parse.hasher` destination and input `parase.plaintext` as in parameter.

The `dest` param in the `--file` add arguement allows the arguement to act like a function and accept input parameter like a typical function

Now that the entire program is finish, we are able to call the program using `python -m sha256`, Since there exist a `__main__` file it treats the `sha256` file as a complete program
