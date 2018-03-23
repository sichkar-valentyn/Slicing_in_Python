# Initial string
dna = 'ATTCGGAGCT'
#   = '0123456789'
#   =   'A   T   T   C   G   G   A   G   C   T'
#   = '(-10)(-9)(-8)(-7)(-6)(-5)(-4)(-3)(-2)(-1)'

print(dna[1])  # Showing the 1 element - T
print(dna[1:4])  # Showing the elements from 1 to 4 - TTC
print(dna[:4])  # Showing the elements from 0 (beginning) to 4 - ATTC
print(dna[4:])  # Showing the elements from 4th to the end - GGAGCT
print(dna[-4:])  # Showing the elements from -4th counting from the end to the end - AGCT
print(dna[1:-1])  # Showing the elements from 1 to -1th - TTCGGAGC
print(dna[1:-1:2])  # Showing the elements from 1 to -1th with step 2 - TCGAG
print(dna[::-1])  # Showing the elements from the beginning to the end in revers direction with step 1 - TCGAGGCTTA
