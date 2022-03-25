# Byte Manipulation using Python

Below is the Hashes associated with the files in this directory.

| Name | Hash |
|------|------|
|What     | 093df51e3493ff08b8c231e30709f918fe2ea507cdf5f13ebe1a8646e1486e2b |
|What.dd  | 3e54122da27eadb1230729ed740b2d80f0a823f9c277066592cdab6ad2e1f4fc |

The file extension `.dd` contains the "Data Dump" of the associated file with similar name.

The point of the additional data dump file is to simplify the investigation of the file data, without the need for a hexeditor.

## Solution

From the datadump file, we can conclude that there are 3 bytes added to the start of the signature. Simply removing the 3 bytes will allow us to access or view the file. This can be done by open(), mmap(), resize(), remove() and turnacate() the file.
