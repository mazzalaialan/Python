s = 0

for n in range(1, 10):

   if n % 11 == 0:

         break

   s += n

else:

    s += 10
print(s)