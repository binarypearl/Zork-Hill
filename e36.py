#!/usr/bin/python

# -*- coding: utf-8 -*-

import re			# for regular expression matching
from sys import exit		# To exit the game with a return code
import os			# To use the system call to clear the screen
from pygame import mixer	# To play music
import time			# To create an artificial delay to add erieness
import shutil			# Looks like it has a copy file function or two...


"""
This is the code for Zork Hill.  It's a pardoy of Zork and Silent Hill series of games.
What we have is 5 rooms.  You start in the center room, and have to search for the one
room that is unlocked.  Once you find that room, if you play your cards right,
you will encounter a puzzle.  If you solve the puzzle, you will get an item that will 
help you on your quest.
"""

"""------------------------------------------------------------------------------------------"""
def begin_game():
  """
    This is start of the game.  From here we can initialize anything that is needed.
  """
  
  os.system ("clear")
  
  # Let's set are doors to the correct lock/unlock status
  
  write_lock_status_file_handle = open ('./door_lock_status.txt', 'w+')
  
  write_lock_status_file_handle.write ("north_door:L\n")
  write_lock_status_file_handle.write ("east_door:L\n")
  write_lock_status_file_handle.write ("south_door:U\n")
  write_lock_status_file_handle.write ("west_door:L\n")
  
  write_lock_status_file_handle.close()
  
  # Let's initialize the volume knob settings:
  write_amplifiter_settings = open ('./amplifier_knob_settings.txt', 'w+')
  
  write_amplifiter_settings.write ("volume_knob:1\n")
  write_amplifiter_settings.write ("bass_knob:1\n")
  write_amplifiter_settings.write ("mid_knob:1\n")
  write_amplifiter_settings.write ("treble_knob:1\n")
  
  write_amplifiter_settings.close()
  
  
  # Let's play our intro song!
  mixer.init()
  mixer.music.load ('./zork_hill_intro.ogg')
  mixer.music.play()
  
  print "Welcome to Zork Hill.  This is a console based game like Zork, but with Silent Hill undertones."
  print "Something brought you here...oh right!  There was a forum on-line, a strange one."
  print "There were posts about this place called Zork Hill, where you could find anything that you are missing."
  print "But what was I missing that made me want to come to this place?"
  print 
  print "Press Enter to start... (or 'q' or 'Q' to quit)",
  
  user_response = raw_input ("")
  user_response_lower_case = user_response.lower()  # Make it lowercase regardless for easier comparison
  
  if user_response_lower_case == "q":
    we_died()
    
  else:
    mixer.music.stop()
    center_room()

"""------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------"""
def center_room():
  """
  This is the staring room.  Basically the map here is a cross.  We start in the center, and 
  there are 4 doors, one to the north, east, south, and west. 
  """
  
  user_repsonse_acceptable = False
  current_door = ""
  
  os.system ("clear")
  
  while not user_repsonse_acceptable:
    print "You are in the center of the center room.  There are 4 doors."
    print "There are four doors in this room.  One to the north, east, south and west"
    print "Which direction would you like to go?"
    
    print 
    
    print "1. North door"
    print "2. East door"
    print "3. South door"
    print "4. West door"
    print "Q. Quit"
    print
    
    user_response = raw_input("> ")
    
    if user_response == "1" or user_response == "n" or user_response == "north":
      current_door = "north_door"
      # "direction_door" is the syntax we use in the text file.
      user_repsonse_acceptable = True
      returned_lock_status = check_door_lock_status(current_door)
    
    elif user_response == "2" or user_response == "e" or user_response == "east":
      current_door = "east_door"
      user_repsonse_acceptable = True
      returned_lock_status = check_door_lock_status (current_door)
    
    elif user_response == "3" or user_response == "s" or user_response == "south":
      current_door = "south_door"
      user_repsonse_acceptable = True
      returned_lock_status = check_door_lock_status (current_door)
    
    elif user_response == "4" or user_response == "w" or user_response == "west":
      current_door = "west_door"
      user_repsonse_acceptable = True
      returned_lock_status = check_door_lock_status (current_door)

    elif user_response == "q" or user_response == "Q":
      we_died()

    else:
      user_repsonse_acceptable = False
      print "Response not understood.  Please try again."
      
  # Now we know the status of the door:  
  if returned_lock_status == "L":
    # play the locked door sound:
    mixer.init()
    mixer.music.load ('./door_locked.mp3')
    mixer.music.play()
    
    time.sleep(1)
    
    print "I can't get the %s door open." % user_response
    
    # Crude way to handle this.  Basically once we call center_room(), the message saying can't open the door
    # will go away due to it's clear statement.  I know I have had better solutions for this situation before....
    # in due time we will fix.
    time.sleep(2)
    
    center_room()
      
  elif returned_lock_status == "U":
    if current_door == "north_door":
      north_door_room()
      
    elif current_door == "east_door":
      east_door_room()
    
    elif current_door == "south_door":
      south_door_room()
   
    elif current_door == "west_door":
      west_door_room()
      
  else:
    print "unm..."
"""------------------------------------------------------------------------------------------"""


"""------------------------------------------------------------------------------------------"""
def south_door_room():
  """
  This is the south door room.  We encounter the first puzzle here.
  """
  
  next_room = ""
  user_repsonse_acceptable = False
  
  os.system ("clear")
  
  # Play erie sound...
  mixer.init()
  mixer.music.load ('./door_open.mp3')
  mixer.music.play()
  
  time.sleep(2)
  
  print "You are now in the south door room.  There is a twisted, mannequin looking like monster "
  print "in the room.  It doesn't see you yet.  Behind the monster there are two things."
  print "There is a medkit on a table.  There is also a box with a keypad."
  print "You have 3 options:\n"
  print "1. Run away back to the center room."
  print "2. Try to sneak around the monster."
  print "3. Attack the monster directly."
  print "q. Quit the game."
  
  while not user_repsonse_acceptable:
    user_response = raw_input("\nWhat would like to do: ")
  
    if user_response == "1":
      next_room = "center_room"
      user_repsonse_acceptable = True
    
    elif user_response == "2":
      os.system ("clear")
      
      print "You were able to get around the monster."
      print "You picked up the medkit.  Your attention is now drawn to the box with keypad...."
      print 
      print "There is some writing on the box.  A clue to the combination perhaps?"
      print 
      print "The numer of key presses is that of the same of the amount of strings on a common bass guitar."
      print "The first number is the pike that started it all.  It's alive!"
      print "The second is the number of episodes in flcl"
      print "The rest is up to chance.  Either you win or you don't."
      print 
      
      # Initialize our loop control variable for the puzzle.
      puzzle_solved = False
      
      while not puzzle_solved:
	user_response_puzzle = raw_input("What is the combination?: ")
  
	if user_response_puzzle == "1650":
	  print "\nYou got the 'cowboy' key."
	  
	  # Play unlock sound
	  mixer.init()
	  mixer.music.load ('door_unlock.mp3')
	  mixer.music.play()
	
	  time.sleep (2)
	  
	  puzzle_solved = True
	  
	  next_room = "center_room"
	  
	  # Now lets write our key to indicate the next door is / will be unlocked:
	  # Lets say the key we get here is the key for the west door
	  unlock_door ("west_door")
	  
	
	elif user_response_puzzle == "q" or user_response_puzzle == "Q":
	  we_died()
	
	else:
	  # play annoying alarm sound
	  mixer.init()
	  mixer.music.load ('./annoying_alarm.mp3')
	  mixer.music.play()
	
	  time.sleep (1)
      
	user_repsonse_acceptable = True
    
    elif user_response == "3":
      print "You don't have a weapon!  The monster spits some type of acid.  You can't see."
      print "The monster attacks, and you are dead."

      user_repsonse_acceptable = True
      we_died()
      
      
    elif user_response == "q" or user_response == "Q":
      user_repsonse_acceptable = True
      we_died()
    
    else:
      print "Response not valid.  Try again."
      user_repsonse_acceptable = False

  # This needs to be the last thing in this function so we don't 
  # execute things afterwards

  if next_room == "center_room":
    center_room()
"""------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------"""
def west_door_room():
  """
  This is the routine for the west door.  Here we have the 2nd puzzle of the game.
  """
  
  west_door_puzzle_solved = False
  
  while west_door_puzzle_solved == False:
  
    os.system ("clear")
  
    print "No monsters here in here...the west door room.  There is a guitar amplifier in the corner."
    print "But I don't see a guitar anywhere."
    print "There are 4 knobs on the amplifier, a volume knob and 3 tone knobs (bass, mid, and treble)."
    print "Each knob goes from 0-10."
    print 
  
    # Now define the clues for the puzzle:
    print "There is also a tape deck in the other corner of the room."
    print "You press play...\n"
  
    print "She screamed, but no one could hear her...unless you were in the room with her."
    print "Not even a rumble was felt when she came crashing down on to the floor."
    print "It was a full day later before she was discovered."
    print "Not even 2 people with the power of 10 oxen could have stopped this tragedy."
  
    # Let's open our amp knob setting file for read:
    with open ('./amplifier_knob_settings.txt', 'r') as read_amplifier_knob_settings:
      records = read_amplifier_knob_settings.readlines()
      
      for record in records:
	match_object = re.search ('(.*)(:)(.*)', record)
	
	if match_object:
	  current_knob_name = match_object.group(1)
	  current_knob_setting = match_object.group(3)
	  
	  if current_knob_name == "volume_knob":
	    volume_knob_name = current_knob_name
	    volume_knob_setting = current_knob_setting
	    
	  elif current_knob_name == "bass_knob":
	    bass_knob_name = current_knob_name
	    bass_knob_setting = current_knob_setting
	    
	  elif current_knob_name == "mid_knob":
	    mid_knob_name = current_knob_name
	    mid_knob_setting = current_knob_setting
	    
	  elif current_knob_name == "treble_knob":
	    treble_knob_name = current_knob_name
	    treble_knob_setting = current_knob_setting
	    
	  
      user_volume_knob_setting = raw_input ("\nVolume Knob is currently set to: " + volume_knob_setting  + ". Change it here if you like: ")
      user_bass_knob_setting = raw_input ("Bass Knob is currently set to: " + bass_knob_setting  + ". Change it here if you like: ")
      user_mid_knob_setting = raw_input ("Mid Knob is currently set to: " + mid_knob_setting  + ". Change it here if you like: ")
      user_treble_knob_setting = raw_input ("Trebble Knob is currently set to: " + treble_knob_setting + ". Change it here if you like: ")
      
      # Now that we have the request for each setting, let's write it to the file:
      
      write_amplifiter_knob_settings = open ('./amplifier_knob_settings_new.txt', 'w+')
      read_amplifier_knob_settings.seek(0)
      

      records = read_amplifier_knob_settings.readlines()
      
      for record in records:
	match_object = re.search ('(.*)(:)(.*)', record)
	
	if match_object:
	  knob_type = match_object.group(1)
	  knob_setting = match_object.group(3)
	  
	  # We test for empty strings here, so if the user just presses enter, it doesn't change the values.
	  if knob_type == "volume_knob":
	    if user_volume_knob_setting == '':
	      write_amplifiter_knob_settings.write ("volume_knob:" + knob_setting + "\n")
	      user_volume_knob_setting = knob_setting
	    
	    else:
	      write_amplifiter_knob_settings.write ("volume_knob:" + user_volume_knob_setting + "\n")
	    
	  elif knob_type == "bass_knob":
	    if user_bass_knob_setting == '':
	      write_amplifiter_knob_settings.write ("bass_knob:" + knob_setting + "\n")
	      user_bass_knob_setting = knob_setting
	    
	    else:
	      write_amplifiter_knob_settings.write ("bass_knob:" + user_bass_knob_setting + "\n")
	    
	  elif knob_type == "mid_knob":
	    if user_mid_knob_setting == '':
	      write_amplifiter_knob_settings.write ("mid_knob:" + knob_setting + "\n")
	      user_mid_knob_setting = knob_setting
    
	    else:
	      write_amplifiter_knob_settings.write ("mid_knob:" + user_mid_knob_setting + "\n")
	    
	  elif knob_type == "treble_knob":
	    if user_treble_knob_setting == '':
	      write_amplifiter_knob_settings.write ("treble_knob:" + knob_setting + "\n")
	      user_treble_knob_setting = knob_setting
	    
	    else:
	      write_amplifiter_knob_settings.write ("treble_knob:" + user_treble_knob_setting + "\n")
	    
      write_amplifiter_knob_settings.close()
      read_amplifier_knob_settings.close()
      
      shutil.copy2 ('./amplifier_knob_settings_new.txt', 'amplifier_knob_settings.txt')
	

      # Ok now we got our settings saved.  Now we see if they set it right:
      if user_volume_knob_setting == "1" and user_bass_knob_setting == "0" and user_mid_knob_setting == "2" and user_treble_knob_setting == "4":
	# Play Pyramid head tone (which indicates now that the East door is open)...not that you would figure that out
	os.system ("clear")
	print "There is a siren coming out of the amplifier...\n"
	
	mixer.init()
	mixer.music.load ('./siren.mp3')
	
	# Let's play it 3 times:
	mixer.music.play()
	time.sleep(2)
	
	mixer.music.play()
	time.sleep(2)
	
	mixer.music.play()
	time.sleep(2)
	
	west_door_puzzle_solved = True
	
	# Now that the puzzle has been solved, lets unlock the east door:
	unlock_door ("east_door")
	
	center_room()
	
      else:
	# play bad tone	
	mixer.init()
	mixer.music.load ('monster_noise.mp3')
	mixer.music.play()
	
	time.sleep (2)
	
	os.system ("clear")
	print "\nWHAT THE HECK WAS THAT?  Sigh, it came out of the amplifier..."
	
	time.sleep (3)
    
    
"""------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------"""
def east_door_room():
  """
    The 3rd room in the series, here we have a telephone puzzle.
  """
  
  puzzle_solved = False
  os.system ("clear")
  
  while puzzle_solved == False:
    print "Here we are in the East room.  There is a desk telephone in here."
    print "There is a book with some writing in it..."
  
    print "\n911 can't help you here.  I do know someone who can help you though."
  
    print "\nFor an entire year, I was held captive in the prison below this place."
    print "For the crimes that I have committed...I deserved it."
  
    print "\nI never saw the sun, but was brought up to the offices one dark night."
    print "It was hard to keep my bearings but I think I mapped it out in my head."
  
    print "\nHow I wish I could talk to the Godfather.  I'm sure he could help me"
    print "with all of his powers and resources."
  
    print "\nI never saw freedom, but I knew that to be the case."
    print "Tick, tock...tick, tock...the end is now close...Tick, tock...tick tock...The End.\n"
  
    print "\nBut I'm free now!  I can help you!.  I'm the only one...Just give me a call!\n"
  
  
    # So the answer is: 365-5341
    user_telephone_response = raw_input ("Number to dial: ")
  
    if user_telephone_response == "365-5341" or user_telephone_response == "3655341":
      # north door unlock...
    
      mixer.init()
      mixer.music.load ('./item_select_i_think.mp3')
      mixer.music.play()
    
      time.sleep(1)
    
      os.system ("clear")
      print "A bloody hand reachs out from the back of the phone.  There is a key in the hand.  You take it."
    
      unlock_door ("north_door")
      puzzle_solved = True
    
    
    else:
      # lets print 3 knocks:
      mixer.init()
      mixer.music.load ('./bang_on_door.mp3')
    
      mixer.music.play()
      time.sleep(1)
    
      mixer.music.play()
      time.sleep (1)
    
      mixer.music.play()
      time.sleep(1)
    
      os.system ("clear")
      print "It sounds like someone is in the phone..."
    
      time.sleep(3)
  
   # Go to center room once we fall out of the loop....
   # This is slightly different from before, but I think this is more proper.
  center_room()

"""------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------"""
def north_door_room():
  """
  This is the final room of this level, and the game at this point.
  """
  
  os.system ("clear")
  
  going_down_elevator = False

  while not going_down_elevator:
    print "It's very cold in the North door room.  There is an elevator at the end."
    print "\nWill you push the button to open the door?"
    
    user_elevator_button_press = raw_input ("Press the button?  (Enter yes or no): ")
  
    if user_elevator_button_press == "y" or user_elevator_button_press == "Y" or user_elevator_button_press == "yes":
      # Play elevator stuff
      
      os.system ("clear")
      
      print "The elevator door is opening..."
      
      mixer.init()
      mixer.music.load ('elevator_open.mp3')
      mixer.music.play()
      
      time.sleep(2)
      
      print "\nGoing down..."
      
      mixer.init()
      mixer.music.load ('./elevator_go_down.mp3')
      mixer.music.play()
      
      time.sleep(4)
      
      going_down_elevator = True
    
    else:
      os.system ("clear")
      print "This room is making me sick..."
      
      mixer.init()
      mixer.music.load ('./eddie_hurl.mp3')
      mixer.music.play()

      time.sleep(2)

  # Lets define one last routine
  end_game()

"""------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------"""
def end_game():
  """
  Let's have this routine end the game
  """
  
  print "do something more elaborate here."
  
  exit (0)
  
"""------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------"""
def check_door_lock_status(user_passed_in_door): 
  """
  
  This routine checks the file ./door_lock_status.txt, which looks like this:
  north_door:L
  east_door:L
  south_door:U
  west_door:L
  
  So 'L' means locked and 'U' is unlocked.  We default to only allowing the south_door 
  to be unlocked.  At later points in the game, we will unlock other doors by 
  modifying the records in this file.
  
  """
  
  with open ('./door_lock_status.txt', 'r') as lock_status_file_handle:
    records = lock_status_file_handle.readlines()
    
    for record in records:
      match_object = re.search ('(.*)(:)(.*)', record)
      
      if match_object:
	#print "door: %s is: %s" % (match_object.group(1), match_object.group(3))
	door = match_object.group(1)
	lock_status = match_object.group(3)
	
	if door == user_passed_in_door:
	  return lock_status
	
"""------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------"""
def unlock_door (door_to_unlock):
  """
    This routine will "unlock" a door by setting the passed in door to 'U' in the ./door_lock_status
    file.
  """
  
  write_lock_status_file_handle = open ('./door_lock_status_new.txt', 'w+')
  
  with open ('./door_lock_status.txt', 'r') as read_lock_status_file_handle:
    records = read_lock_status_file_handle.readlines()
    
    for record in records:
      match_object = re.search ('(.*)(:)(.*)', record)
      
      if match_object:
	door_to_check = match_object.group(1)
	lock_status = match_object.group(3)
	
	if door_to_unlock == door_to_check:
	  write_lock_status_file_handle.write (door_to_check + ":U\n")
	 
	else:
	  write_lock_status_file_handle.write (door_to_check + ":" + lock_status + "\n")
	  

  read_lock_status_file_handle.close()
  write_lock_status_file_handle.close()
	  
  shutil.copy2 ('./door_lock_status_new.txt', './door_lock_status.txt')
  

"""------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------"""      
def we_died():
  
  mixer.init()
  mixer.music.load ('./i_die.mp3')
  mixer.music.play()
  
  time.sleep(2)
  
  print "You have died.  Try again."
  exit(0)
"""------------------------------------------------------------------------------------------"""    
    

# Let's begin:
begin_game()
    
    
    
    
  
  
  
  
    
