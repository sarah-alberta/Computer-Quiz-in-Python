print("\nWelcome To My Computer Quiz!")

playing = input("\nDo you want to play? ")

if playing.lower() != 'yes':
    quit()

print("Okay! let's play :) ")
score = 0

# Question 1
answer = input("\nWhat does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The answer is 'Central Processing Unit'")

# Question 2
answer = input("\nWhat is the main function of RAM? ")
if answer.lower() in ["temporary storage", "short-term memory", "working memory"]:
    print('Correct!')
    score += 1
else:
    print("Incorrect! RAM is used for temporary storage.")

# Question 3
answer = input("\nWhat does ROM stand for? ")
if answer.lower() == "read only memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The answer is 'Read Only Memory'")


# Print results
print("\nYou got " + str(score) + " questions correct out of 4.")
print("You scored " + str((score/4) * 100) + "%.")

# Add a final message
if (score/4) * 100 >= 75:
    print("Great job! You have a good understanding of basic computer concepts.")
else:
    print("Keep learning! There's always more to discover about computers.")
