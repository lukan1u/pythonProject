"""
Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates
 all the odd-indexed characters of S with all the even-indexed characters of S
 ,this process should be repeated N times."""

def decrypt(text, n):
    if text in ("", None):
        return text
    
    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
    return text



def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text


encrypt("012345", 1)