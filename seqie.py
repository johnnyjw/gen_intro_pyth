seq = 'atggg'
print(seq, "\n\n")

for i in range(len(seq)) :     # line 1
        for j in range(i) :        # line 2
                print(seq[j:i])     # line 3