import mmap

def main():
    # The number of additional bytes found in the "what" binary file
    ADDITIONAL_BYTE =   3

    # Signature list representing guard to counter byte removal execution
    # Current the known signature of the file is a "JPG" file
    SIGN_LIST       =   [b'\xff\xd8\xff']

    # Open the file using binary read/write mode
    with open ("what", "rb+") as bin:

        # Map the binary file information into memory map
        file_vcopy  =   mmap.mmap(bin.fileno(), 0)

        # Loop over the first few bytes to identify whether the file is tampered
        # or not
        for SIGN in SIGN_LIST:

            # If the signature matches the first 3 bytes, then the files has been fixed
            if SIGN == file_vcopy.read(ADDITIONAL_BYTE):
                print ("File is not manipulated")

                # early exit to avoid byte removal execution
                return

        # Get the original file size in bytes
        origin_size =   file_vcopy.size()

        # Subtract the size with the additional bytes found in binary file
        new_size    =   origin_size - ADDITIONAL_BYTE

        # Move the starting position of the starting bytes to 3.
        # This is to resize the current file and then append a new size
        file_vcopy.move(0, ADDITIONAL_BYTE, new_size)

        # Flush the memory copy from memory and append to binary using turncate function
        file_vcopy.flush()

        file_vcopy.close()
        bin.truncate(new_size)

        # Remap the file onto memory to force changes. Hacky solution
        mmap.mmap(bin.fileno(), 0)

if __name__ == "__main__":
    main()
