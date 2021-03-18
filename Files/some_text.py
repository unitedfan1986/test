#avg_length = total/count
file = open("some_text.txt", "r")
count = 0
for line in file:
    words = line.split()
    count += len(words)
print("Number of words:", (count))
