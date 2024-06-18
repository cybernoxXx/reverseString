def reverseString(word):
    reverted = ''
    # Cycling to all the list
    for element in word:
        # Adding the element first and after adding the string reverted, in this way I can revert the string, the order of adding is important, if the first addend is reverted I obtain the same string
        reverted = element + reverted
    return reverted


assert reverseString('Hello') == 'olleH'
assert reverseString('') == ''
assert reverseString('aaazzz') == 'zzzaaa'
assert reverseString('xxxx') == 'xxxx'
