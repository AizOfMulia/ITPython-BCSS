import hashlib
import argparse

# Takes a string plaintext then simply return a hexdigest
def plaintext_to_hash (plaintext : str):
    return hashlib.sha256(plaintext.encode()).hexdigest()

# Takes a file directory location and passes it into a file open funct
# in order to get the bytes associated with the binary before hashing
def file_to_hash (directory : str):

    # Create a temp variable out of the file open scope
    # to use as a return variable
    bin_digest : str

    # Open a file in read and write binary mode
    with open (directory, "rb+") as bin:
        bin_digest  =   hashlib.sha256(bin.read()).hexdigest()

    return bin_digest

def main():
    input_parse     =   argparse.ArgumentParser(description="A simple SHA256 hashing program")
    input_parse.add_argument("plaintext", metavar="plaintext", help="A string of character or file directory")

    '''
    If the "--file" argument is not provided the default function to be used is the
    Plaintext_to_hash function.

    the parse dest indicated the parse naming convention that will be called during
    final output

    action `store_const` stores the value for the parse to use. based on the `--file`
    argument
    '''
    input_parse.add_argument('--file', dest="hasher", action="store_const",
                            const=file_to_hash, default=plaintext_to_hash)

    parse   =   input_parse.parse_args()
    print (parse.hasher(parse.plaintext))

if __name__ == "__main__":
    main()
