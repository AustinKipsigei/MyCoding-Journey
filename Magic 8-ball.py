name = "Frank"
question = "Are you real?"
answer = ""

#importing random module to generate random numbers
import random
random_number = random.randint(1 , 9)
if random_number == 1:
   answer = "Yes - definitely"

   #adding "elif" statements 
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
     answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say so"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    answer = "Error"

#Frank's question
print("Frank asks:" + question)
#The Magic 8-Ball's answer
print("Magic 8-Ball's answer:" + answer)