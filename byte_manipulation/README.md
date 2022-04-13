# Byte Manipulation using Python

Below is the Hashes associated with the files in this directory.

| Name | Hash |
|------|------|
|What     | 093df51e3493ff08b8c231e30709f918fe2ea507cdf5f13ebe1a8646e1486e2b |
|What.dd  | 3e54122da27eadb1230729ed740b2d80f0a823f9c277066592cdab6ad2e1f4fc |

The file extension `.dd` contains the "Data Dump" of the associated file with similar name.

The point of the additional data dump file is to simplify the investigation of the file data, without the need for a hexeditor.

## Solution

Based on the datadump file, the `ff d8 ff` hex is a common signature used for `JPG` files.

The first noticably strange feature is that `4c 4f 4c` is not a nature byte formation of the binary. Which might mean that it has been added there, leaving the first **three** bytes unnecessary.

```
00000000: 4c4f 4cff d8ff e000 104a 4649 4600 0101  LOL......JFIF...
00000010: 0000 0100 0100 00ff db00 4300 0503 0404  ..........C.....
00000020: 0403 0504 0404 0505 0506 070c 0807 0707  ................
00000030: 070f 0b0b 090c 110f 1212 110f 1111 1316  ................
00000040: 1c17 1314 1a15 1111 1821 181a 1d1d 1f1f  .........!......
```
Once we've identified the number of bytes needed to be removed we can construct a quick prototype.

## Prototyping

### Opening the file

Using `open()` and the memory map module `mmap` we can open the file in binary mode and map the bytes to memory.

```
import mmap

def remove_bytes ():

    with open ('what', 'rb+') as bin:
        file_vcopy  =   mmap.mmap (bin.fileno (), 0)
```

1. Open the `what` file with read binary plus mode, which allows read +write to be executed.
2. Create an in memory virtual copy using mmap using the `bin` file as a reference.

### Calculating the bytes after removing the additional bytes

Once we've opened the file and map it to memory, we need to calculate the remaining bytes after removal.

```
import mmap

ADDITIONAL_BYTES    =   3

def remove_bytes ():

    with open ('what', 'rb+') as bin:
        file_vcopy  =   mmap.mmap (bin.fileno (), 0)

        origin_size =   file_vcopy.size ()
        new_size    =   origin_size - ADDITIONAL_BYTES
```

1. Declare a variable to indicate the number of bytes we need to remove.
2. Get the original size of the `what` file in bytes
3. Calculate the new size of the file once we remove the additonal bytes.

### Removing and appending the changes

We've calculated the size of the remaining bytes, now we need to remove and append the changes.

```
import map

ADDITIONAL_BYTES    =   3

def remove_bytes ():

    with open ('what', 'rb+') as bin:
        file_vcopy  =   mmap.mmap (bin.fileno (), 0)

        origin_size =   file_vcopy.size ()
        new_size    =   origin_size - ADDITIONAL_BYTES

        file_vcopy.move (0, ADDITIONAL_BYTES, new_size)
        file_vcopy.flush ()

        file_vcopy.close ()
        bin.turncate (new_size)

        file_vcopy  =   mmap.mmap (bin.fileno (), 0)
```

1. Move the starting byte to its new location, in this case we want to remove the first three bytes. 0 -> 3
2. Next we need to flush the changes from memory.
3. Close the virtual copy file
4. Append or turncate the changes to the file size
5. Optionally, reload the file onto memory

Now to run the script, we need to use the python `__name__` conditional check to tell it which function to run

```
import map

ADDITIONAL_BYTES    =   3

def remove_bytes ():

    with open ('what', 'rb+') as bin:
        file_vcopy  =   mmap.mmap (bin.fileno (), 0)

        origin_size =   file_vcopy.size ()
        new_size    =   origin_size - ADDITIONAL_BYTES

        file_vcopy.move (0, ADDITIONAL_BYTES, new_size)
        file_vcopy.flush ()

        file_vcopy.close ()
        bin.turncate (new_size)

        file_vcopy  =   mmap.mmap (bin.fileno (), 0)

if __name__ == '__main__':
    remove_bytes ()
```

### Apply a signature list to avoid deleting correct bytes

However, there is a problem here when rerunning the script after the file has been corrected. It will remove **three** bytes everytime its executed. Therefore, we need to have a signature list to avoid that.


```
import map

ADDITIONAL_BYTES    =   3

SIGN_LIST           =   [b'\xff\xd8\xff']

def remove_bytes ():

    with open ('what', 'rb+') as bin:
        file_vcopy  =   mmap.mmap (bin.fileno (), 0)

        if file_vcopy.read (ADDITIONAL_BYTES) in SIGN_LIST:
            print ("The binary is correct")
            return

        origin_size =   file_vcopy.size ()
        new_size    =   origin_size - ADDITIONAL_BYTES

        file_vcopy.move (0, ADDITIONAL_BYTES, new_size)
        file_vcopy.flush ()

        file_vcopy.close ()
        bin.turncate (new_size)

        file_vcopy  =   mmap.mmap (bin.fileno (), 0)

if __name__ == '__main__':
    remove_bytes ()
```

1. Create a signature list, this signature list can be further expanded on based on the type of files you want to conduct byte removal. Since the current file is a `JPG` file, we only include the `JPG` signature.
2. We check whether the first three bytes is in the signature list
3. Prompt that the file hasn't been modified or is correct.
4. Early exit the function to avoid removal execution
