def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    if len(s)%2==1:
        d=s[len(s)//2]
    elif len(s)%2==0:
        d=s[((len(s)//2)-1):((len(s)//2)+1)]
    return d 
print(main('codemm'))