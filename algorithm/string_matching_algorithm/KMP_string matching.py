def kmp_search(pat,txt):
    n=len(txt)
    m=len(pat)
    #store  longest prefix that is also suffix ...lps
    lps=[0]*m#create a list
    j=0# index for pat[]
    LPSArray(pat,m,lps)
    i=0# index for txt[]
    while i<n:
        #check one by one text and pattern are matched then this 		condition work
        if txt[i]==pat[j]:
            j+=1
            i+=1
        #if j value and m vlue are same it means pattern matched in text
        if j==m:
            print("Found pattern at index",str(i-j))
            #store lps_array value in j
            j=lps[j-1]
        #check one by one text and pattern are not matched then this part 		work
        elif i < n and pat[j] != txt[i]:
            #if j value is not 0
            if j != 0:
                #store lps_array value in j
                j=lps[j-1]
            #if j value is 0 
            else:
                #then increase i
                i+=1
#creat lps array in this function 
def LPSArray(pat,m,lps):
    len=0#length of the lps_array
    i=1# index for pat[]
    lps[0]=0
    while i < m:
        #check one by one text and pattern are matched then this 		condition work
        if pat[i]==pat[len]:
            #lps_array use index i for store store value
            lps[i]=len+1
            #then increase i
            i+=1
        #check one by one text and pattern are not matched then this part 		work
        else:
            #if len is not 0 
            if len !=0:
                #store lps_array value in len using index
                len=lps[len-1]
            #if len is 0
            else:
                #in index i lps_array value is 0
                lps[i]=0
                #increase i 
                i+=1
txt = "hghjdshjsdhjvsdhdvjh"
pat = "jvs"
kmp_search(pat, txt)
