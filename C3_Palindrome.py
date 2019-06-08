from collections import deque


def palindrome(a_string):
    """Returns True or False depending on whether or not a word is a palindrome."""
    a_deque = deque()
    # Pushes characters from string to deque.
    for character in a_string:
        if character in ' ,./(){};"[]':
            # Ignores special characters. This can be customized.
            continue
        a_deque.append(character.lower())

    balanced = True
    # Pops first and last characters in deque and compares them.
    while len(a_deque) > 1 and balanced:
        first_character = a_deque.popleft()
        last_character = a_deque.pop()
        if first_character != last_character:
            balanced = False
    # If all left and right characters were the same, returns True. Otherwise, return False.
    return balanced


words = ['radar', 'toot', 'corridor', 'I prefer Pi']
for word in words:
    print("Is '%s' a palindrome? Answer: %s" % (word, palindrome(word)))
