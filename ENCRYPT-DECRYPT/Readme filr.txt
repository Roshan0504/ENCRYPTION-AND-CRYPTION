**Caesar Cipher Encryption and Decryption**
=============================================

This is a Python implementation of the Caesar Cipher algorithm, a simple encryption technique that shifts each letter in a message by a fixed number of positions in the alphabet.

**Functions**
-------------

### `encrypt(message, shift)`

Encrypts a message using the Caesar Cipher algorithm with a given shift value.

* `message`: The message to be encrypted (string)
* `shift`: The number of positions to shift each letter in the alphabet (integer)

Returns the encrypted message as a string.

### `decrypt(encrypted_message, shift)`

Decrypts an encrypted message using the Caesar Cipher algorithm with a given shift value.

* `encrypted_message`: The encrypted message to be decrypted (string)
* `shift`: The number of positions to shift each letter in the alphabet (integer)

Returns the decrypted message as a string.

**Example Usage**
-----------------


message = "Hello, World!" shift = 3

encrypted_message = encrypt(message, shift) print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, shift) print("Decrypted message:", decrypted_message)


**Output**
----------

Encrypted message: Khoor, Zruog! Decrypted message: Hello, World!



**Note**
-----

This implementation only works with alphabetical characters (a-z and A-Z). Non-alphabetical characters (such as punctuation and whitespace) are left unchanged.

This is a very simple encryption algorithm and should not be used for sensitive data. In real-world applications, more secure encryption algorithms should be used.

