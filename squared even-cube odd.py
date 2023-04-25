# Franchesca Marie U. Donadillo
# BSCPE 1-5
# Program 4 - Squared even, cube odd

# read source text file integers.txt
# create file named double.txt
# create file triple.txt
with open("integers.txt", "r") as file_integers, open("double.txt", "w") as even_square, open("triple.txt", "w"):

    # iterate through integers.txt
    for line in file_integers:
        num = int(line)
        # determine the even numbers and square it
        if num % 2 == 0:
            sqrt = (num)**2
            even_square.write(str(sqrt) + "\n")
        
        # determine the odd numbers and cube it