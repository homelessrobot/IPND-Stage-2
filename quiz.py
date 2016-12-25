#code for the project final quiz.code

#I'll break it down into single pieces and work from there

#0. Write three quizzes: easy, medium, hard and write blanks for each.

# Easy quiz level and answers
easy_level = '''The internet is basically a huge ___1___ of computers that
can all communicate with each other. When a user visits a webpage via their
___2___, their computer sends a request via the web to a ___3___ to request
files and documents. These documents are then translated by the browser
and displayed to the user. The protocol used to translate what the user 
requests into a language that the computer understands and vice versa is 
called ___4___.'''
easy_answers = ["network", "browser", "server", "http"]
easy_placeholders = ["___1___", "___2___", "___3___", "___4___"]  

# Medium quiz level and corresponding answer
medium_level = '''HTML, CSS, and Javascript all have different purposes 
which can be explained by an analogy to a house: ___1___ is like the structure 
of the house - where are walls placed, which room will serve as kitchen, 
bedroom, etc.
___2___ is like the style of your house - what style is the carpeting? What 
color are the walls? Etc.
___3___ is like gadgets in the house - TV remote, garage doors opener, etc.
The tree-like structure of the code is called document ___4___ model.'''
medium_answers = ["html", "css", "javascript", "object"]
medium_placeholders = ["___1___", "___2___", "___3___", "___4___"]


# hard level quiz and corresponding answers.
hard_level = '''HTML stands for ___1___ Markup Language. HTML documents 
form the majority of the content on the web. HTML documents contain text 
content which describes "what you see" and ___2___ which describes "how it 
looks". 
HTML documents are made of HTML ___3___. When writing HTML, we tell browsers 
the type of each element by using HTML ___4___.'''
hard_answers = ["hypertext", "markup", "elements", "tags" ]
hard_placeholders = ["___1___", "___2___", "___3___", "___4___"]

explanation = '\n' + '''Please fill in the blanks.''' + '\n'
 

#1. Beginning - Selecting a difficulty level and displaying quiz
#1.1. Prompt user to select a difficulty level upon opening the program - use raw_input.
#will use .lower() to make sure the user doesn't need to worry about upper or lower case.
#if she inputs a wrong difficulty level (not easy, medium or hard), the while loop will ensure she is prompted again.
#Depending on the chosen level, the respective quiz will be chosen.
#actually, the quiz will not be printed here, but the selection will take place in this step. print is in the next step.

def choose_level():
  
  level = raw_input('Please select a level: easy, medium, or hard').lower()
  while level not in ('easy', 'medium', 'hard'):
    level = raw_input('Please select a level: easy, medium, or hard').lower()
  if level == 'easy':
    prompt_quiz(easy_level, easy_placeholders, easy_answers)
  elif level == 'medium':
    prompt_quiz(medium_level, medium_placeholders, medium_answers)
  elif level == 'hard':
    prompt_quiz(hard_level, hard_placeholders, hard_answers)
    

#2. Check answers and progress through the blanks
#first, the short explanation sentence will be displayed to explain to the user what she needs to do.
#then the level selected in choose_level will be displayed and the user is prompted to fill in blank one.
#again, .lower() makes sure the answer is not case sensitive
#since there are only 4 blanks, I will insert a while loop to stop prompting the user to fill in more after blank 4 has been
#correctly answered.
#Again, raw.input will be used to gather user input. A simple if/else statement will validate the input as true or false
#if true, user will be presented next question. If false, user will be prompted to answer that blank again.
#the number starts at 0 and it adds 1 each time the user inputs a correct question, all the way up to 4, where the 
#while loop makes sure to stop the prompting. At the same time, when 4 is reach, the if statement makes sure the user
#is notified that she has finished the quiz. Thats's it! 

def prompt_quiz(level, placeholders, answers):
  print explanation
  print level
  number = 0
  while number <4:
    answer_input = raw_input('\n' + 'What is the correct answer for blank' + placeholders[number] + '?' + '\n').lower()
    if answer_input == answers[number]:
      print '\n' + 'Great job!!!' + '\n' '\n' + 'Now move on to the next blank!' + '\n'
      print level
      number += +1
    else:
      print 'oops, please try again'
  if number == 4:
    print '\n' +' CONGRATS, you have finished the quiz!!!' + '\n'

#kicks it off
choose_level()
