"""
NewestMultiply.py - This program prints the numbers 0 through 10 along with
                     these values multiplied by 2 and by 10.
Input:  None.
Output: Prints the numbers 0 through 10 along with their values multiplied by
        2 and by 10.
"""
head1 = "Number: "
head2 = "Multiplied by 2: "
head3 = "Multiplied by 10:  "
NUM_LOOPS = 10  # Constant used to control loop.

print("0 through 10 multiplied by 2 and by 10" + "\n")

# Write while loop
x = 0
while True:
  if x > NUM_LOOPS:
    break
  else:
    print(head1 + str(x))
    print(head2 + str(x*2))
    print(head3 + str(x*10))
    x += 1