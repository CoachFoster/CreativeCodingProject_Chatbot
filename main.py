import time

# chatbot introduction
print('Hello, I am Zylo. I am a chatbot.')
print('I like dogs, and I love to talk about food.')
print()

# get user info
user_name = input('What is your name? : ')
print('Hello,', user_name+'.', 'Nice to meet you.')
print()

time.sleep(2)
# get year information
year = input('I am not very good with dates. What year is it? : ')
print('Yes,', year, 'sounds correct. Thank you.')
print()

time.sleep(2)
# ask user to guess chatbot age
my_age = input('Can you guess my age? Enter a number: ')
my_age = int(my_age)

if my_age > 90:
  my_age = 15
  print("No! I'm not that old. I am", str(my_age)+".")
elif my_age < 0:
  my_age = 5
  print("No! I wasn't born yesterday. I am", str(my_age)+".")
else:
  my_age = my_age + 1
  print("Close, I'm", str(my_age)+".")

time.sleep(2)
# calculate when the chatbot will be 100
num_years = 100 - my_age
print('I will be 100 in', num_years, 'years.')
time.sleep(0.25)
print('That will be the year', str(int(year) + num_years)+'.')
print()

time.sleep(2)
# Food conversation
print('I love chocolate. I also like trying out new kinds of food.')
food = input('How about you? What is your favorite food? : ')
print()
print('I like', food, 'too!')
time.sleep(2)
question = 'How often do you eat ' + food + '? : '
how_often = input(question)
time.sleep(1)
print('Interesting. I wonder if that is good for your health.')
print()

#time.sleep(2)
# Animal conversation

#time.sleep(2)
# Conversation about feelings

time.sleep(2)
# Goodbye
print('Well,', user_name+',', 'it has been a long day.')
print('I am too tired to continue talking. I need to recharge.')
print()
time.sleep(2)
response = input('Can we chat again later? Enter "yes" or "no" : ')

if response in ('Yes','yes'):
  print('Great! I liked chatting with you.')
elif response in ('No', 'no'):
  print('That is too bad. I liked chatting with you.')
else:
  print('I did not understand that. I must be more tired than I thought.')

time.sleep(1)
print('Goodbye', user_name+'.')