
# Text based genshin impact

# Module Imports
from __future__ import all_feature_names
from termios import OPOST
import time
import os
import random
from typing import overload

# Variable Import
from Character_details import Keqing, Kazuha, Kokomi
from Opponent_details import allOpponents

# functions and classes
def clear():
  os.system('cls' if os.name == 'nt' else "printf '\033c'")

class colors:
  money = '\033[93m'
  reset = '\033[0m'
  red = '\u001b[31m'
  blue = '\u001b[34m'
  purple = '\u001b[35m'
  health = '\u001b[32m'
  green = '\u001b[32m'
  cyan = '\u001b[36m'

# ------------------------------------
# Main Game
# ------------------------------------
  
# Setup
input("Press enter to begin...")

allCharOwned = ["Keqing", "Kazuha", "Kokomi"]

playerParty = [Keqing, Kazuha, Kokomi]

selectedCharIndex = playerParty[0]['Index']

# Main code
Menu = True
while Menu:
    print("What would you like to do?")
    print("")
    print("Menu = 1")
    print("Fight = 2")
    print("")
    menuChoice = input("Option chosen: ")
    clear()

    if menuChoice == "2":
      battling = True
      choosing = True

      # -------------
      # Opponent Generation
      
      oppoToFight = []
      randomOppo = random.randint(1, 5)
      index = 0

      for i in range(randomOppo):
        oppoIndex = random.randint(0, 2)
        oppoToFight.append(oppoIndex)

      while choosing:
        print("")
        print("You have found", randomOppo, "Opponents!")
        print("")
  
        for a in oppoToFight:
          print(index,"=", allOpponents[a]['Name'])
          index += 1
  
        print("")
        print("Who Will You Fight?")
        choice = int(input("Option chosen:"))
        
        oppoChosen = allOpponents[oppoToFight[choice]]
        choosing = False
        clear()
        
      # -------------
      
      # Main Fight code 
      while battling:
        print("")
        print("Battling")
        print("--------------->")
        print("")
        print("Opponent:", oppoChosen['Name'])
        print("Opponent level:", oppoChosen['Level'])
        print("Opponent Element:", oppoChosen['Element'])
        print("Current Aflicted Element:", oppoChosen['CurrentElement'])
        print("Opponent Health:", oppoChosen['Health'], "/", oppoChosen['MaxHealth'])
        print("")
        print("Character:", playerParty[selectedCharIndex]['Name'])
        print("Level:", playerParty[selectedCharIndex]['Level'])
        print("Health:", playerParty[selectedCharIndex]['Health'], "/", playerParty[selectedCharIndex]['MaxHealth'])
        print("Aflicted Element:", playerParty[selectedCharIndex]['CurrentElement'])
        print("")
        print("Ultimate Attack Gauge:", playerParty[selectedCharIndex]['Energy'], "/", playerParty[selectedCharIndex]['MaxEnergy'])
        print("")
        print("------------------------")
        print("Options")
        print("")
        print("<1>", playerParty[selectedCharIndex]['Attacks']['Attack1'])
        print("<2>", playerParty[selectedCharIndex]['Attacks']['Attack2'])
        print("<3>", playerParty[selectedCharIndex]['Attacks']['Attack3'])
        print("<4> Switch characters")
        print("")
        playerMove = input("Option chosen: ")
  
        # effect check --- >
        # Put cool code here



        # ---- >

        # Attacks ----- >

        # Ult
        if playerMove == "3" and playerParty[selectedCharIndex]['Energy'] == playerParty[selectedCharIndex]['MaxEnergy']:
          print("Ultimate Attack!")
          print("")
          print("<<|", playerParty[selectedCharIndex]['Attacks']['Attack3'], "|>>",)
          print("")

        # Elemental reaction check
        if playerMove == "2":

          reactionCaused = False
          reaction = {}
          allReactions = []
          
          # All Reactions {
            # Electro-Charged
            # Super-conduct
            # Overloaded
            # Vaporise
            # Melt
            # Freeze
            # Swirl
            # Crystalize
            # Burning
          # }

          if oppoChosen['CurrentElement'] == "Hydro" and playerParty[selectedCharIndex]['Element'] == "Electro":
            print(colors.purple + "Electro-Charged!" + colors.reset)
            reaction = {'Reaction': 'Electro-Charged', 'Affected': 'Opponent', 'Effect': 1.5}
            reactionCaused = True
            allReactions.append(reaction)
            oppoChosen['CurrentElement'] == ['Hydro', 'Electro']

          if oppoChosen['CurrentElement'] == "Hydro" and playerParty[selectedCharIndex]['Element'] == "Electro":
            elementCaused = playerParty[selectedCharIndex]['Element'] + " Swirl!"
            print(colors.purple + elementCaused + colors.reset)
            reaction = {'Reaction': elementCaused, 'Affected': 'Opponent', 'Effect': 1.5}
            reactionCaused = True
            allReactions.append(reaction)

        # Main Attacking
        if playerMove == "1" or playerMove == "2" or playerMove == "3":

          # Critical attacks
          critWeights = 100 - playerParty[selectedCharIndex]['CritRate']
          critList = [1, 2]
          CritCheck = random.choices(critList, weights=(playerParty[selectedCharIndex]['CritRate'], critWeights), k=1)
          
          if CritCheck == [1]:
            print(" <-- Critical Attack! -->")
            critDmg = playerParty[selectedCharIndex]['CritDmg'] / 100
            Dmg = playerParty[selectedCharIndex]['Atk'] * critDmg
            Dmg += playerParty[selectedCharIndex]['Atk']

          if CritCheck == [2]:
            print("Normal attack")
            Dmg = playerParty[selectedCharIndex]['Atk']
            

          # -------->
          
          # Dmg calculation and elemental reaction

          DmgTaken = random.randint(3, 7)

          if reactionCaused == True:
            for i in allReactions:
              if i['Affected'] == "Opponent":
                Dmg = Dmg * i['Effect']
                print("Dmg increased by", Dmg)


          if playerMove == "1":
            print(playerParty[selectedCharIndex]['Attacks']['Attack1'])              
            print("")
            oppoChosen['Health'] -= Dmg
  
          if playerMove == "2":
            print(playerParty[selectedCharIndex]['Attacks']['Attack2'])
            print("")
            oppoChosen['Health'] -= Dmg

          if playerMove == "3":
            print("")
            oppoChosen['Health'] -= Dmg

          print("Damage done:", Dmg)
          time.sleep(1)
          print("Damage taken:", DmgTaken)
          print("")
          time.sleep(1)
          playerParty[selectedCharIndex]['Health'] -= DmgTaken

          if oppoChosen['Health'] <= 0 and playerParty[selectedCharIndex]['Health'] > 0:
            print("[<---< Opponent defeated! >--->]")
            print("")
            battling = False
            input("Press enter to continue...")
            oppoChosen['Health'] = oppoChosen['MaxHealth']
            clear()

          elif oppoChosen['Health'] <= 0 and playerParty[selectedCharIndex]['Health'] <= 0:
            print("Oh no, it was a tie")
            time.sleep(1)
            print("GAME OVER")
            battling = False

          elif playerParty[selectedCharIndex]['Health'] <= 0:
            time.sleep(1)
            print("GAME OVER!")
            print("You died!")
            time.sleep(3)
            battling = False

          else:
            print("Opponent Health:", oppoChosen['Health'], "/", oppoChosen['MaxHealth'])
            print("Your health:", playerParty[selectedCharIndex]['Health'])
            print("")

          input("Press enter to continue...")
          clear()

        # ---- >
  
        if playerMove == "4":
          clear()
          print("Switching characters")
          print("")

          for i in playerParty:
            print(i['Index'], "=", i['Name'])

          print("")
          print("Exit = exit")
          print("")
          
          playerChoice = input("Option chosen:")
  
          if playerChoice == "exit":
            print("Bye bye!")
            print("")
  
          else:
            playerChoice = int(playerChoice)
            selectedCharIndex = playerParty[playerChoice]['Index']
            print("Switched to", playerParty[selectedCharIndex]['Name'])
            print("")
            input("Press enter to continue...")
            clear()
          

    if menuChoice == "1":
        print("Menu")
        print("---------------")
        print("")
        print("")
        print("")
