#------------------------IMPORTS-------------------------------#
from random import choice
from copy import copy
import os


#------------------------DICTIONARIES-------------------------------#
day_count=1
time_periods = ['Morning', 'Afternoon', 'Evening', 'Night']

## Morning Happiness Actions ##
m_hap_actions = [
  'Relax in the Root Cove', 
  'Go to CCP for a meal with your classmates',
  'Play board games in hostel lounge with floormates',
  'Eat gomgom for breakfast',
  "Go to McDonald's for breakfast with your roommate"
]

## Afternoon Happiness Actions ##
a_hap_actions = [
  'Sing karaoke with your mates in recreational room', 
  'Class outing to East Coast Park',
  'Play Nintendo Switch games with classmates',
  'Watch a movie',
  'Netflix and chill'
]

## Evening Happiness Actions ##
e_hap_actions = [
  'Cook dinner with friends',
  'Play pool in Root Cove',
  'Watch the sunset on the hostel rooftop',
  'Go for hotpot dinner',
  'Watch a football match in the hostel lounge with friends'
]

## Night Happiness Actions ## 
n_hap_actions = [
  'Play board games in hostel lounge with friends', 
  'Play PC games with friends',
  'Sing karaoke with your mates in recreational room',
  'Stay Up Till Dawn hanging out with your friends',
  'Go for drinks with your buddies'
]

## Morning Health Actions ##
m_hea_actions = [
  'Go to the gym',
  'Go for a run at the school track',
  'Cook a healthy breakfast',
  'Go for a walk in Changi Business Park',
  'Go for a morning swim'
]

## Afternoon Health Actions ## 
a_hea_actions = [
  'Go for a run at the school track',
  'Go to the gym',
  'Go for an afternoon swim',
  'Take a nap',
  'Go for a mindfulness class'
]

## Evening Health Actions ##
e_hea_actions = [
  'Go for yoga class', 
  'Take a stroll outside campus',
  'Go to the gym',
  'Go for badminton 5th row training',
  'Cycle to Changi Jurassic Mile'
]

## Night Health Actions ##
n_hea_actions = [
  'Night cycling from SUTD to East Coast Park',
  'Cycle around Upper Changi Road',
  'Have a late night run around Changi Business Park',
  'Take a late night walk around the school',
]

## Actions For Random Dilemma Choice ##
mas_dilemma = [
  'Help a friend with their homework',
  'Go for remedial class',
  "Do the following week's homework",
  'Hold a lesson for your classmates',
  'Attend a seminar'
]


#------------------------FUNCTIONS-------------------------------#


def generate_message(period, day_count):
  # Function to generate message after every period
  # Input arguments: period is the part of the day from the for loop, day_count is the day         number from the while loop
  
  print(f'{period}, Day {day_count}')
  if period == 'Morning':
    print('Rise and shine! Time to take on the day.')
  elif period == 'Afternoon':
    print("Beat the afternoon slump... or not.")
  elif period == 'Evening':
    print("The sky's getting dark after a productive(?) day.")
  elif period == 'Night':
    print('Is it time for bed or is the night still young?')
  print('\n')
  print("  Activities: ")
  

def generate_choices(period):
  # This function returns a dictionary comprising of keys of integer 1-4 and activities as values.
  # Takes in period from the for loop as argument 
  if period == 'Morning':
    random_choices = {
      1: 'Go to class',
      2: 'Study',
      3: choice(m_hap_actions),
      4: choice(m_hea_actions)
    }

  elif period == 'Afternoon':
    random_choices = {
      1: 'Go to class',
      2: 'Study',
      3: choice(a_hap_actions),
      4: choice(a_hea_actions)
    }

  elif period == 'Evening':
    random_choices = {
      1: choice(['Take a long nap', 'Attend a party']),
      2: 'Study',
      3: choice(e_hap_actions),
      4: choice(e_hea_actions)
    }

  elif period == 'Night':
    random_choices = {
      1: 'Sleep',
      2: 'Study',
      3: choice(n_hap_actions),
      4: choice(n_hea_actions)
    }
    
  for i in random_choices:
    print(f'  {i}: {random_choices[i]}')
    
  return random_choices
  

def music_or_no():
  #Function to ask user if they want music or not
  print('\n')
  answer = input('Would you like music today? Y / N ')
  print('\n')
  if answer.lower() == 'y':
    return generate_music_choices()
  else:
    print('Okay :(')
  print('\n')


def generate_music_choices():
  # This function returns a string (dictionaries and for loops makes python confused in this case) of choices for the user to choose the music they would like to listen to.
    print('1: House Music', '\n2: Pop Music', '\n3: J-pop', '\n4: Classical')
    print('\n')
    music_choice = input('What would you like to listen to today? ')
    print('\n')
    
    if music_choice == '1':
      print ('  1: Tiesto - The Motto', '\n  2: Tiesto - The Business', "\n  3: David Guetta & Bebe Rexha - I'm Good (Blue)")
      print('\n')
      song_choice = int(input('  Please pick a song: '))
      if song_choice == 1:
        os.system('start chrome.exe https://www.youtube.com/watch?v=1_4ELAxKrDc')
      elif song_choice == 2:
        os.system('start chrome.exe https://www.youtube.com/watch?v=nCg3ufihKyU')
      elif song_choice == 3:
        os.system('start chrome.exe https://www.youtube.com/watch?v=90RLzVUuXe4')
      else:
        os.system('start chrome.exe https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    
    elif music_choice == '2':
      print ('  1: Cyberpunk: Edgerunners - I Really Want to Stay At Your House', '\n  2: BLACKPINK - Shut Down', '\n  3: LE SSERAFIM (르세라핌) - ANTIFRAGILE', '\n  4: Mr. Kitty - After Dark', '\n  5: Fools Garden - Lemon Tree', '\n  6: Sadie Jeans - Locksmith', '\n  7: Lana Del Rey - Serial Killer', '\n  8: Jnr Choi - TO THE MOON (Drill Remix)')
      print('\n')
      p_song_choice = int (input ('  Please pick a song: '))
      if p_song_choice == 1:
        os.system('start chrome.exe https://www.youtube.com/watch?v=h4VJGNNSQnw')
      elif p_song_choice == 2:
        os.system('start chrome.exe https://www.youtube.com/watch?v=POe9SOEKotk')
      elif p_song_choice == 3:
        os.system('start chrome.exe https://www.youtube.com/watch?v=pyf8cbqyfPs')
      elif p_song_choice == 4:
        os.system('start chrome.exe https://www.youtube.com/watch?v=Cl5Vkd4N03Q')
      elif p_song_choice == 5:
        os.system('start chrome.exe https://www.youtube.com/watch?v=wCQfkEkePx8')
      elif p_song_choice == 6:
        os.system('start chrome.exe https://www.youtube.com/watch?v=ltcCxKw_Qiw')
      elif p_song_choice == 7:
        os.system('start chrome.exe https://www.youtube.com/watch?v=xlf9e9PnJZM')
      elif p_song_choice == 8:
        os.system('start chrome.exe https://www.youtube.com/watch?v=VXXlPiDnkNg')
      else:
        os.system('start chrome.exe https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    
    elif music_choice == '3':
      print ('  1: Eve - 廻廻奇譚', '\n  2: YOASOBI -「祝福」', '\n  3: Kenshi Yonezu - KICKBACK', '\n  4: なとり - Overdose', '\n  5: ONE OK ROCK - We Are')
      print('\n')
      jp_song_choice = int (input ('  Please pick a song: '))
      if jp_song_choice == 1:
        os.system('start chrome.exe https://www.youtube.com/watch?v=1tk1pqwrOys')
      elif jp_song_choice == 2:
        os.system('start chrome.exe https://www.youtube.com/watch?v=3eytpBOkOFA')
      elif jp_song_choice == 3:
        os.system('start chrome.exe https://www.youtube.com/watch?v=M2cckDmNLMI')
      elif jp_song_choice == 4:
        os.system('start chrome.exe https://www.youtube.com/watch?v=H08YWE4CIFQ')
      elif jp_song_choice == 5:
        os.system('start chrome.exe https://www.youtube.com/watch?v=uyaKoj7wABY')
      else:
        os.system('start chrome.exe https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    
    elif music_choice == '4':
      print('  1: Chopin - Nocturne op.9 No.2', '\n  2: Chopin - Ballade No.1 in G minor, Op.23', '\n  3: Joe hisaishi - Asian Dream Song')
      print('\n')
      c_song_choice = int (input ('  Please pick a song: '))
      if c_song_choice == 1:
        os.system('start chrome.exe https://www.youtube.com/watch?v=9E6b3swbnWg')
      elif c_song_choice == 2:
        os.system('start chrome.exe https://www.youtube.com/watch?v=BSFNl4roGlI')
      elif c_song_choice == 3:
        os.system('start chrome.exe https://www.youtube.com/watch?v=skmMiNKBrJE')
      else:
        os.system('start chrome.exe https://www.youtube.com/watch?v=dQw4w9WgXcQ')
  
    else:
      music_choice == False
      os.system('start chrome.exe https://www.youtube.com/watch?v=dQw4w9WgXcQ')
  
print('\n')

#function to return scores for going to class action
def go_to_class():
  # Function activated when the user chooses to go to class. This function works by chance,        where the user will end up having either a good, mid, or bad professor.
  good_prof = {'name': 'good professor', 'value': (2, 0, -1)}
  mid_prof = {'name': 'mid professor', 'value': (1, 0, -1)}
  bad_prof = {'name': 'bad professor', 'value': (0, -1, -1)}
  random_perc = float(choice(range(0, 101)))
  if random_perc < 25:
    return bad_prof
    
  elif random_perc >= 25 and random_perc < 85:
    return mid_prof
    
  elif random_perc >= 85:
    return good_prof

def study():
  # Function activated when user chooses to study, giving the user 4 options to choose from.
  study_types = {
    1: 'Self study',
    2: 'Study with friends',
    3: 'Go for a consultation session with a professor',
    4: 'Go for PLS'
  }
  for i in study_types:
    print(f'    {i}: {study_types[i]}')
  valid_input = False
  
  while valid_input == False:
    print('\n')
    study_choice = int(input('    How would you like to study? '))
    print('\n')
    if study_choice in [1, 2, 3, 4]:
      valid_input == True
      print(f'    You choose to {(study_types[study_choice][0]).lower()}{study_types[study_choice][1:]}.')
      print('\n')
      if study_choice == 1:
        return (1, 0, -1)
      elif study_choice == 2:
        return (1, 0.5, -0.5)
      elif study_choice == 3:
        return (1.5, -0.5, -1)
      elif study_choice == 4:
        return (2, -1, -1)
        
    else:
      valid_input == False
      print('    Please input a number from 1 to 4.')

#function to choose the action and print accordingly based on user input
def choose_action(random_choices):
  # This function takes an user input of a number 1 - 4 and returns the corresponding action and its value tuple in the random choices dictionary.
  # The random_choices argument provides the function with the choices given to the user.
  
  valid_input = False
  user_choice = None
  
  while valid_input == False:
    print('\n')
    user_input = input('  What would you like to do? ')
    print('\n')
    if user_input in ['1', '2', '3', '4']:
      valid_input = True
      user_choice = random_choices[int(user_input)]
      print(f'  You have decided to {user_choice[0].lower()}{ user_choice[1:]}.')
      print('\n')
      
      if user_choice == 'Sleep':
        choice_score = (0, 0, 2)  
        
      elif user_choice == 'Take a long nap':
        choice_score = (-1, -1, 2) 

      elif user_choice == 'Attend a party':
        choice_score = (-1, 2, -1)
        
      elif user_choice == 'Go to class':
        prof_dict = go_to_class()
        prof_name = prof_dict['name']
        choice_score = prof_dict['value']
        if prof_name == 'bad professor':
          print(f'    Aww man! The {prof_name} is teaching the class today.')
          print('\n')
          input("    Press enter to continue.")
          print('\n')
          
        elif prof_name == 'good professor':
          print(f'    Yes! The {prof_name} is teaching the class today.')
          print('\n')
          input("    Press enter to continue.")
          print('\n')
  
        return choice_score
  
      elif user_choice == 'Study':
        choice_score = study()
    
      elif user_choice in m_hap_actions or a_hap_actions or e_hap_actions or n_hap_actions:
        choice_score = (-1, 1, 0)
    
      elif user_choice in m_hea_actions or a_hea_actions or e_hea_actions or n_hea_actions:
        choice_score = (-1, 0, 1)
      
      return choice_score
        
    else:
      valid_input = False
      print('  Please input a number from 1 to 4.')

#function where there is a random chance for a second choice (dilemma action) after user selects an action
      
def generate_dilemma(period, choices):
  # This function has a chance of happening after every turn, giving the user 2 choices that will either help their current stats or make them worse. Inspiration was drawn from Monopoly's community chest and chance cards.
  # The period argument affects what choices are given due to the time of day
  # The choices argument is used to reference the choices that were already given prior to the dilemma, so as to not duplicate the same choice twice.
  
  if period == 'Morning':
    print('  Oof! You are hit with a dilemma!')
    m_hap_dilemma = m_hap_actions.copy()
    m_hap_dilemma.remove(choices[3])
    m_hea_dilemma = m_hea_actions.copy()
    m_hea_dilemma.remove(choices[4])
    random_perc = choice(range(0, 101))
    if random_perc <= 33:
      dilemma_choices = {
        1: choice(mas_dilemma),
        2: choice(m_hap_dilemma)
      }
    elif random_perc >= 67:
      dilemma_choices = {
        1: choice(mas_dilemma),
        2: choice(m_hea_dilemma)
      }
    else:
      dilemma_choices = {
        1: choice(m_hap_dilemma),
        2: choice(m_hea_dilemma)
      }
      
  elif period == 'Afternoon':
    print('  Oof! You are hit with a dilemma!')
    a_hap_dilemma = a_hap_actions.copy()
    a_hap_dilemma.remove(choices[3])
    a_hea_dilemma = a_hea_actions.copy()
    a_hea_dilemma.remove(choices[4])
    random_perc = choice(range(0, 101))
    if random_perc <= 33:
      dilemma_choices = {
        1: choice(mas_dilemma),
        2: choice(a_hap_dilemma)
      }
    elif random_perc >= 67:
      dilemma_choices = {
        1: choice(mas_dilemma),
        2: choice(a_hea_dilemma)
      }
    else:
      dilemma_choices = {
        1: choice(a_hap_dilemma),
        2: choice(a_hea_dilemma)
      }
    
  elif period == 'Evening':
    print('  Oof! You are hit with a dilemma!')
    e_hap_dilemma = e_hap_actions.copy()
    e_hap_dilemma.remove(choices[3])
    e_hea_dilemma = e_hea_actions.copy()
    e_hea_dilemma.remove(choices[4])
    random_perc = choice(range(0, 101))
    if random_perc <= 33:
      dilemma_choices = {
        1: choice(mas_dilemma),
        2: choice(e_hap_dilemma)
      }
    elif random_perc >= 67:
      dilemma_choices = {
        1: choice(mas_dilemma),
        2: choice(e_hea_dilemma)
      }
    else:
      dilemma_choices = {
        1: choice(e_hap_dilemma),
        2: choice(e_hea_dilemma)
      }

  else:
    dilemma_choices = None
    
  return dilemma_choices

#function to choose the dilemma action and return its score
def choose_dilemma(dilemma_choices):
  # This function takes in the user's dilemma choice, adding its value to the user's total score whilst subtracting the value of the choice that was not chosen.
  # The argument dilemma_choices is used to reference the options given to the user.
  if dilemma_choices == None:
    dilemma_score = (0, 0, 0)

  else:
    for i in dilemma_choices:
          print(f'  {i}: {dilemma_choices[i]}')
    print('\n')
    valid_input = False
    user_choice = None
  
    while valid_input == False:
      user_input = input('  What would you like to do? ')
      print('\n')
      if user_input in ['1', '2']:
        valid_input = True
        user_choice = dilemma_choices[int(user_input)]
        other_choice = dilemma_choices[3 - int(user_input)]
        print(f'  You have decided to {user_choice[0].lower()}{user_choice[1:]}.')
        print('\n')
        if user_choice in mas_dilemma:
          choice_score = (1, 0, 0)
        elif user_choice in m_hap_actions or a_hap_actions or e_hap_actions:
          choice_score = (0, 1, 0)
        elif user_choice in m_hea_actions or a_hap_actions or e_hea_actions:
          choice_score = (0, 0, 1)
        
        if other_choice in mas_dilemma:
          other_score = (1, 0, 0)
        elif other_choice in m_hap_actions or a_hap_actions or e_hap_actions:
          other_score = (0, 1, 0)
        elif other_choice in m_hea_actions or a_hap_actions or e_hea_actions:
          other_score = (0, 0, 1)
          
        dilemma_score = (choice_score[0] - other_score[0], choice_score[1] - other_score[1], choice_score[2] - other_score[2])
      
      else:
        valid_input = False
        print('  Please input a number from 1 to 2.')
        print('\n')
      
  return dilemma_score

  
#function to update the scores for the current period and the total score
def update_scores(choice_score, dilemma_score, day_scores, total_scores):
  # This function updates the score after each period
  # Choice_score and dilemma_score values are added to the day_score and total_scores argument 
 
  
  if not (total_scores['Mastery'] <= 0 and choice_score[0] < 0): 
    day_scores['Mastery'] += choice_score[0] + dilemma_score[0]

  if not (total_scores['Happiness'] <= 0 and choice_score[1] < 0):
    day_scores['Happiness'] += choice_score[1] + dilemma_score[1]
  
  if not (total_scores['Health'] <= 0 and choice_score[2] < 0):
    day_scores['Health'] += choice_score[2] + dilemma_score[2]
  
  total_scores['Mastery'] += choice_score[0] + dilemma_score[0]
  total_scores['Happiness'] += choice_score[1] + dilemma_score[1]
  total_scores['Health'] += choice_score[2] + dilemma_score[2]


def display_scores(day_count, day_scores, total_scores):
  # This function takes in the day_count, day_scores and total_scores to display the points earned for the day
  print("Score obtained Day {}:".format(day_count))
  for i in day_scores:
    print(f'{i}: {day_scores[i]}')
  print('\n')
  print("-------------------")
  print("| Total scores:   |")

  for i in total_scores:
    if i=='Mastery':
      for j in range(1,5):
        if len(str(total_scores[i]))==j:
          print(f"| {i}: {total_scores[i]}"+" "*(7-j)+"|")
    elif i=='Happiness':
      for j in range(1,5):
        if len(str(total_scores[i]))==j:
          print(f"| {i}: {total_scores[i]}"+" "*(5-j)+"|")
    elif i=='Health':
      for j in range(1,5):
        if len(str(total_scores[i]))==j:
          print(f"| {i}: {total_scores[i]}"+" "*(8-j)+"|")
  print("-------------------")
  print('\n')


#return warnings if the score is dangerously low as it could result in losing the game.
def score_warnings(total_scores, day_count):
  # Function to warn user when their score values are too low 
  # Takes in the day_count to warn the user of low mastery levels from day 3 onwards
  
  for i in total_scores:
    if i == "Mastery" and day_count >= 3:
      if total_scores["Mastery"] < float(2) and total_scores["Happiness"] > float(0) and total_scores["Health"] > float(0):
        print("WARNING: Your Mastery is dangerously low! You should start studying if you want to pass your final exam and beat the game!\n")

    elif i == "Happiness":
      if float(0) < total_scores["Happiness"] < float(2) and total_scores["Health"] > float(0):
          print("WARNING: Your Happiness is dangerously low! Work-life balance is very important, take some time to destress if you want to make it to the end of the game!\n")
  
    elif i == "Health":
      if float(0) < total_scores["Health"] < float(2) and total_scores["Happiness"] > float(0):
          print("\nWARNING: Your Health is dangerously low! Take care of your health if you want to survive and make it to the end of the game!\n")

        
#function to cap the scores to max 10 and min 0.
def score_cap(total_scores):
  # Function that caps the maximum attainable score to 10
  # If health or happiness levels reach 0, user ends up losing the game
  
  res = True
  for i in total_scores:
    if i == "Mastery":
      if total_scores[i] > 10:
        total_scores[i] = 10
      elif total_scores[i] < 0:
        total_scores[i] = 0
        
    elif i == "Happiness":
      if total_scores[i] > 10:
        total_scores[i] = 10
      elif total_scores[i] <= 0:
        print('Oh no, your Happiness score has hit 0! You have crippling depression, and decided to drop out of SUTD :(.')
        print('\n')
        print('\n')
        print(''' ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝''')
        res=False
        
    elif i == "Health":
      if total_scores[i] > 10:
        total_scores[i] = 10
      elif total_scores[i] <= 0:
        print("Oh no, your Health score has hit 0! You died. RIP bozo. :'(")
        print('\n')
        print('\n')
        print(''' ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝''')
        res=False
  
  return res

  
#main game function with all other funcrtions inside

##################################################################
#------------------------MAIN GAME-------------------------------#
##################################################################  
  
#assess the mastery score after the 5 days and return a string
def grade_mastery(meter_value): 
  # Function to grade the user based on their total mastery score
  if meter_value <= 0:
    grade = 'abysmal and you are a mistake.'
  elif 0 < meter_value <= 3:
    grade = 'poor. Did you even study? Wake up your idea!'
  elif 3 < meter_value <= 6:
    grade = "meh. I mean it's alright, overrated as heck in my opinion."
  elif 6 < meter_value <= 9:
    grade = 'very commendable, WOOOOOOO!'
  else:
    grade = "Perfect! That's what I'm talking about! That's why you're the goat. THE GOAT!"
  return grade

#assess the happiness score after the 5 days and return a string
def grade_happiness(meter_value): 
  # Function to grade the user's total happiness score
  
  if meter_value <= 0:
    grade = 'extremely depressed. You need therapy to continue functioning.'
  elif 0 < meter_value <= 3:
    grade = "very unhappy. Overworking much? Stop it. Get some help."
  elif 3 < meter_value <= 6:
    grade = 'meh. Neither happy nor unhappy. Focus on yourself more!.'
  elif 6 < meter_value <= 9:
    grade = 'happy and we are happy for you too. :)'
  else:
    grade = "...wow! You having such a good time, you're having a ball!"
  return grade

#assess the health score after the 5 days and return a string
def grade_health(meter_value): 
  # Function to grade the user's total health score
  
  if meter_value <= 0:
    grade = "died. RIP bozo :'("
  elif 0 < meter_value <= 3:
    grade = "plagued with disease. You are going to end up in the hospital if you don't watch it!"
  elif 3 < meter_value <= 6:
    grade = "aight. Touch more grass and drink more water."
  elif 6 < meter_value <= 9:
    grade = 'pretty healthy! Could it be a sore throat keeping you from tip top condition?'
  else:
    grade = "looking PENG! You must be a fitness freak or something, well done!"
  return grade


def game_main():
  print('''███████╗██╗   ██╗████████╗██████╗     ███████╗██╗███╗   ███╗       ██████╗ 
██╔════╝██║   ██║╚══██╔══╝██╔══██╗    ██╔════╝██║████╗ ████║    ██╗██╔══██╗
███████╗██║   ██║   ██║   ██║  ██║    ███████╗██║██╔████╔██║    ╚═╝██║  ██║
╚════██║██║   ██║   ██║   ██║  ██║    ╚════██║██║██║╚██╔╝██║    ██╗██║  ██║
███████║╚██████╔╝   ██║   ██████╔╝    ███████║██║██║ ╚═╝ ██║    ╚═╝██████╔╝
╚══════╝ ╚═════╝    ╚═╝   ╚═════╝     ╚══════╝╚═╝╚═╝     ╚═╝       ╚═════╝ ''')
  print('\n')
  char_name = input('What is your name? ')
  print('\n')
  
  print(f"Welcome to SUTD {char_name}! Finals are in 5 days LOL!")
  print('\n')
  input("Press enter to continue.")
  print('\n')
  
  print("With Finals in 5 days, you have to achieve a level of Mastery of 5 and above in order to pass the game. To earn levels of Mastery, attend classes or go for study sessions.")
  print('\n')
  input("Press enter to continue.")
  print('\n')

  print("To maintain your levels of Health, you have to sleep and exercise.")
  print('\n')
  input("Press enter to continue.")
  print('\n')
  
  print("To maintain your levels of Happiness, you have to socialise and relax with friends.")
  print('\n')
  input("Press enter to continue.")
  print('\n')

  print("Study hard but don't forget to maintain your levels of Health and Happiness!")
  print('\n')
  input("Press enter to continue.")
  
  day_count = 1

  total_scores = {'Mastery': round(float(0), 1), 'Happiness': round(float(5), 1), 'Health': round(float(5), 1)}

  while (day_count <= 5):

    day_scores = {'Mastery': round(float(0), 1), 'Happiness': round(float(0), 1), 'Health': round(float(0), 1)}

    music_or_no()
    
    for period in time_periods:
    
      generate_message(period,day_count)
      
      choices = generate_choices(period)
           
      c_s = choose_action(choices)

      if choice(range(0, 101)) <= 25:
        dilemma = generate_dilemma(period, choices)
        d_s = choose_dilemma(dilemma)
        
      else:
        d_s = (0, 0, 0)
      
      update_scores(c_s, d_s, day_scores, total_scores)

      cap = score_cap(total_scores)
      if cap == False:
        return
      
    display_scores(day_count, day_scores, total_scores)
    
    score_warnings(total_scores, day_count)
      

        
    print('--------------------------------------------------')
    print('\n')
    input("Press to continue")
    print('\n')
    
    day_count += 1


  print("Your 5 days for finals preparation are over! Let's find out how you did for your examinations.")

  print(f"\n")
  
  input("Press to continue")

  print("\n")

  if total_scores['Mastery'] >= 5:
    print(f"Congratulations {char_name}! You have passed the end of year finals examinations. ")
    print("\n")
    
    print(f"You have obtained a score of {total_scores['Mastery']}! With this score, we want you to know that fortunately or unfortunately, this is {grade_mastery(total_scores['Mastery'])} ")
    print("\n")

    print(f"Now you may have passed, but how happy and healthy are you? In terms of happiness, you are {grade_happiness(total_scores['Happiness'])}")
    print('\n')
    
    print(f"As for health, you are {grade_health(total_scores['Health'])} Hope you're happy with your results, {char_name}. If not, try again!")
    print('\n')

  else:
    print(f"{char_name}, we are sorry to tell you that you have failed your final exam! Are you ready for bootcamp?! If not, give this game another try!")
    print("\n")
    print('--------------------------------------------------')
  print('\n')
  print('''
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝''')
    

  
game_main()




