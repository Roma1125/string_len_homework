def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    if len(s1)%2==1 and len(s2)%2==0 and  len(s3)%2==0: 
        s=f'[{s1}]'
    if len(s2)%2==1 and len(s1)%2==0 and len(s3)%2==0:
        s=f'[{s2}]'
    if len(s3)%2==1 and len(s2)%2==0 and len(s1)%2==0:
        s=f'[{s3}]'
    if (len(s1)%2==1 and len(s2)%2==1) and  len(s3)%2==0: 
        s=f'[{s1},{s2}]'
    if (len(s2)%2==1 and len(s3)%2==1) and len(s1)%2==0:
        s=f'[{s2},{s3}]'
    if (len(s3)%2==1 and len(s1)%2==1) and len(s2)%2==0 :
        s=f'[{s1},{s3}]'
    if len(s1)%2==1 and len(s2)%2==1 and  len(s3)%2==1: 
        s=f'[{s1},{s2},{s3}]'
    
    return s
print(main('aaada','ssxs','ddd'))