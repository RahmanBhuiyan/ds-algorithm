def search(pat, txt):
    t=txt.replace(" ", "")
    print(t)
    M = len(pat)
    N = len(t)
 
    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0
         
        # For current index i, check
        # for pattern match */
        tx=0
        pa=0
        while(j < M):
            tx+=ord(txt[i+j])
            
            pa+=ord(pat[j])
            # print()
            # print(txt[j])
            j += 1
        print(tx,'  ',pa)
        if pa == tx:
            print("string match :",txt[i],i)
        
# Driver Code
if __name__ == '__main__':
    txt = "Python consistently ranks as one of the most popular programming languages"
    pat = "of"
    search(pat, txt)
        
