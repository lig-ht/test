# ******************************************
#      Welcome to Las Vegas Texas Holdem
#      Programmed by Nicholas Szijarto
# ******************************************

import random

debug = "false"

# ***************************************
# Function to determine debug output
# ***************************************
def isdebug():
  return debug=="true"

# ***************************************
# Function to select a card from the deck
# Note that this function deletes after
# ***************************************
def getcard(deck):
  suit = random.randint(0,len(deck)-1)
  if(isdebug()):
    print (suit)
  card = random.randint(0,len(deck[suit])-1)
  if(isdebug()):
     print (card)
  cardvalue = deck[suit][card]
  deck[suit].pop(card)
  return (suit,cardvalue,deck)

# ****************************************
# Function to print cash balances
# ****************************************
def printbalances(msg,cash):
  print("***")
  print(msg)
  for x in range(0,len(cash)):
    print(" Player ",x+1,": ",cash[x])
  print("***")

# ****************************************
# Function to print hole cards
# ****************************************
def printholes(holes):
  for x in range(0,len(holes)):
    print(" Player",x+1,":",holes[x][1],"of",holes[x][0],"&",holes[x][3],"of",holes[x][2])
  print("********** REMEMBER YOUR CARDS! ************")

# ****************************************
# Betting Function
# ****************************************
def bet(currbet,pot,players,bigblind,cash,folds):
  obp = bigblind-1
  if (obp==0):
    obp=players-1
  for x in range(players):
    folded = 0
    for f in folds:
       if (f==obp):
         print("--------------")
         print("Player",obp,"previously folded")
         folded = 1
    if (folded==1):
      obp = obp-1
      if (obp==0):
        obp=players
      continue
    print("-------------")
    print("Player",obp,"bets")
    print("Current bet is",currbet)
    b=input("(c)all,(r)aise,(f)old:")
    if (b=="c"):
      cash[obp-1]=cash[obp-1]-currbet
      pot = pot + currbet
    if (b=="r"):
      print("Raise",currbet,"by how much? (must be less than",limit,")")
      r = input("Raise Amount:")
      cash[obp-1]=cash[obp-1]-currbet-int(r)
      pot = pot+currbet+int(r)
      currbet = currbet+int(r)
    if (b=="f"):
      print("Player",obp,"folds")
      folds.append(obp)
    obp = obp-1
    if (obp==0):
      obp=players
  print("-----------------------")
  printbalances("Current Chip Balances",cash)
  print("Pot: ",pot)
  return (currbet,pot,folds)

# Placeholder if we want to return here logically
if (1==1):

# ****************************************
# Define our suits and cards
# Note that each array of cards is a copy
# ****************************************
  suits = ["Clubs","Diamonds","Hearts","Spades"]
  cards = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]

# *******************************************
# Print Welcome Banner
# Custom rule 10 chips per player
# Minimum bet of 2, could be changed to input
# *******************************************
  print("---------------------------------")
  print("Welcome to Las Vegas Texas Holdem")
  print("---------------------------------")
  print("Minimum bet: 2 chips")
  print("Limit: 4 chips")
  print("All players begin with 100 chips")
  minbet = 2
  limit = 4

# ****************************************
# Choose Number of Players
# ****************************************
  players = 0
  while (players<2 or players>10):
    players = int(input("Select number of players (2-10): "))

# ************************************************
# Initialize & Calculate chips
# ************************************************
  cash = []
  for x in range(players):
       cash.append(100)
  printbalances("Initial Chip Balances",cash)

# ***********************************************
# Return here if we're continuing from the end
# ***********************************************
cont = 1
while (cont == 1):
  deck = [cards.copy() for j in range(len(suits))]
  if(isdebug()):
    print(deck)

# ***********************************************
# Identify the dealer, small blind, and big blind
# Note that this is a custom randomized rule
# Not based on cards dealt since it has the
# same purpose
# ***********************************************
  dealer = random.randint(1,players)
  smallblind = dealer-1
  if (smallblind == 0):
    smallblind = players 
  bigblind = smallblind-1
  if (bigblind == 0):
    bigblind = players
  print(" Player ",dealer," has been assigned the dealer button")
  print(" Player ",smallblind," has been assigned the small blind button")
  print(" Player ",bigblind," has been assigned the big blind button")
  print(" Small blind contributes ",int(minbet/2))
  print(" Big blind contributes ",minbet)
  cash[smallblind-1] = int(cash[smallblind-1]-minbet/2)
  cash[bigblind-1] = cash[bigblind-1]-minbet
  pot = int(minbet*1.5)
  printbalances("Current Chip Balances",cash)
  print("Pot: ",pot)

# ******************************************
# Deal the hole cards
# if this were truly multi-player
# no one would be aware of the others' cards
# ******************************************
  print ("**********************")
  print ("Dealing the hole cards")
  print ("**********************")
  hcards = []
  for x in range(players):
    card1 = getcard(deck)
    deck = card1[2] 
    card2 = getcard(deck)
    deck = card2[2]
    hcard = [suits[card1[0]],card1[1],suits[card2[0]],card2[1]]
    hcards.append(hcard)
  if (isdebug()):
    print (hcards)
  printholes(hcards)

# *****************************************
# Opening Bet
# *****************************************
  currbet = minbet
  folds = []
  openbet = bet(currbet,pot,players,bigblind,cash,folds)
  currbet = openbet[0]
  pot = openbet[1]
  folds = openbet[2]

# ************************************
# The flop, 3 shared cards are dealt
# ************************************
  flop1 = getcard(deck)
  deck = flop1[2] 
  flop2 = getcard(deck)
  deck = flop2[2]
  flop3 = getcard(deck)
  deck = flop3[2]
  flop4 = getcard(deck)
  deck = flop4[2]
  flop5 = getcard(deck)
  deck = flop5[2]
  print("***************")
  print("The Flop")
  print("***************")
  print(flop1[1],"of",suits[flop1[0]]);
  print(flop2[1],"of",suits[flop2[0]]);
  print(flop3[1],"of",suits[flop3[0]]);

# **************************************
# Flop betting
# **************************************
  flopbet = bet(currbet,pot,players,bigblind,cash,folds)
  currbet = flopbet[0]
  pot = flopbet[1]
  folds = flopbet[2]

# **************************************
# Fourth Street
# **************************************

  print("***************")
  print("The Turn (Fourth Street)")
  print("***************")
  print(flop1[1],"of",suits[flop1[0]]);
  print(flop2[1],"of",suits[flop2[0]]);
  print(flop3[1],"of",suits[flop3[0]]);
  print(flop4[1],"of",suits[flop4[0]]);

# **************************************
# Fourth Street betting
# **************************************
  fourthbet = bet(currbet,pot,players,bigblind,cash,folds)
  currbet = fourthbet[0]
  pot = fourthbet[1]
  folds = fourthbet[2]

# **************************************
# Fifth Street
# **************************************

  print("***************")
  print("The River (Fifth Street)")
  print("***************")
  print(flop1[1],"of",suits[flop1[0]]);
  print(flop2[1],"of",suits[flop2[0]]);
  print(flop3[1],"of",suits[flop3[0]]);
  print(flop4[1],"of",suits[flop4[0]]);
  print(flop5[1],"of",suits[flop5[0]]);

# **************************************
# Fifth Street betting
# **************************************
  fifthbet = bet(currbet,pot,players,bigblind,cash,folds)
  currbet = fifthbet[0]
  pot = fifthbet[1]
  folds = fifthbet[2]

# **************************************
# Score the Hands and Hand out Winnings
# **************************************

  print("")
  print("**************** Winners ****************")
  winners = (suits,flop1,flop2,flop3,flop4,flop5,hcards,folds)  #Remove texxasscore from here.
  z = (len(winners))        #z must be length of winners for this execute. (len(winners))
  top = (z)                 #removed top = 0
  winner = []               #top is now defined as z. Important.
  hand = ""
  for z in winners:         #Fixed Terminal error line 275 '>' not supported between 'list' and 'int'
    if (0>top):             #Change (z>top) to (0>top) since z = top.
      top=z
  if (top>0):
    hand = "High Card"
  if (top>=20):
    hand = "One Pair"
  if (top>=40):
    hand = "Two Pairs"
  if (top>=60):
    hand = "Three of a Kind"
  if (top>=80):
    hand = "Straight"
  if (top>=100):
    hand = "Flush"
  if (top>=120):
    hand = "Full House"
  if (top>=140):
    hand = "Four of a Kind"
  if (top>=160):
    hand = "Straight Flush"
  if (top>=180):
    hand = "Royal Flush"

  for x in range(len(winners)):
    if (winners[x]==top):
      winner.append(x)
  prize = pot / len(winners)    #len(winner)changed to len(winners)
  print("*********************")
  for y in winner:
    print("Player",y+1,"Wins with a",hand,"!")
    print("*********************")
    cash[y] = int(cash[y]+prize)
  printbalances("Final Balances",cash)
  c = input("Do you wish to continue? [y][n]")
  if (c=="y"):
     cont = 1
  else:
     cont = 0
