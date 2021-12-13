seq = 'atggg'
print(seq, "\n\n")

i=0 
while i<len(seq) :
      j=0 
      while(j<i) :
                print(seq[j:i])
                j+=1
      i+=1