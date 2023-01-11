"""
A file containing functions encrypt and decrypt fot the Caesar cipher
"""


def encrypt(s_normal, offset):
    """
    Function that encrypts a string using the Caesar cipher

    @param s_normal: the string to be ecrypted
    @param offset: the encryption offset
    @:return the encrypted string
    """

    res = ''
    for value in map(ord, s_normal):
        if value in range(65, 91):
            value = (value - 65 + offset) % 26 + 65
        if value in range(97, 123):
            value = (value - 97 + offset) % 26 + 97
        res += str(chr(value))
    return res


def decrypt(s_encrypted, offset):
    """
    Function that decrypts a string using the Caesar cipher

    @param s_encrypted: the ecrypted string
    @param offset: the encryption offset
    @:return the original string
    """

    res = ''
    for value in map(ord, s_encrypted):
        if value in range(65, 91):
            value = (value - 65 - offset) % 26 + 65
        if value in range(97, 123):
            value = (value - 97 - offset) % 26 + 97
        res += str(chr(value))
    return res


def simple_visual_test():
    """
    A function to provide a quick feedback, only for testing purposes

    @:return void
    """

    print(encrypt("ahoj", 1))
    print(decrypt("bipk", 1))
    print(encrypt("ahoj?", 1))
    print(decrypt("bipk?", 1))
    print(encrypt("ahoj", 13))
    print(decrypt("nubw", 13))


if __name__ == "__main__":
    simple_visual_test()
