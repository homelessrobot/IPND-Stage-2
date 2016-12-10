
# I will use random notes from Lesson 1 as quiz content.

# first just create the story, answers and placeholders and mark them 
# accordingly

# Easy quiz level and answers
easy_level = '''The internet is basically a huge ___1___ of computers that
can all communicate with each other. When a user visits a webpage via their
___2___, their computer sends a request via the web to a ___3___ to request
files and documents. These documents are then translated by the ___2___
and displayed to the user. The protocol used to translate what the user 
requests into a language that the computer understands and vice versa is 
called ___4___.'''
easy_answers = ["network", "browser", "server", "HTTP"]
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
medium_answers = ["HTML", "CSS", "JavaScript", "object"]
medium_placeholders = ["___1___", "___2___", "___3___", "___4___"]


# hard level quiz and corresponding answers.
hard_level = '''HTML stands for ___1___ Markup Language. HTML documents 
form the majority of the content on the web. HTML documents contain text 
content which describes "what you see" and ___2___ which describes "how it 
looks". 
HTML documents are made of HTML ___3___. When writing HTML, we tell browsers 
the type of each element by using HTML ___4___.'''
hard_answers = ["Hypertext", "markup", "elements", "tags" ]
hard_placeholders = ["___1___", "___2___", "___3___", "___4___"]


# Now the code to let the user choose the difficulty level
# it should also ensure that the user only proceeds if she puts in either easy, medium, or hard
# if not, the prompt shuld reload and ask the user again.

def difficulty_level():
	print "Welcome to my quiz!" 
	level = raw_input("Please select a level: easy, medium, or hard").lower()
	
	if level == "easy":
		play_game(easy_level, easy_answers, easy_placeholders)
		print "You have chosen the easy level"
	elif level == "medium":
		play_game(medium_level, medium_answers, medium_placeholders)
		print "You have chosen the medium level"
	elif level == "hard":
		play_game(hard_level, hard_answers, hard_placeholders)
		print "You have chosen the hard level"
	else:
		print "Your input must be easy, medium or hard, please try again"
		return difficulty_level
 

# 1. print the quiz corresponding to the user's choice(easy, medium, hard)
# 2. prompt the user for input on placeholder 1. If correct -> move to next placeholder. If 
# false, prompt for input again.
#  

def play_game(level, answers, placeholders):
	print level  # prints the quiz
# now ask user for input for placeholders
user_answer = raw_input("What is the correct answer for blank 1?").lower()
if user_answer == 



	

# Game Execution
difficulty_level()
