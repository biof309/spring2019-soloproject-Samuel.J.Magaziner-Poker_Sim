#%% Imports
import random
from PIL import Image

#%% Variables
# 'C' are clubs, 'D' are diamonds, 'H' are hearts, 'S' are spades
Suit_list = ['C', 'D', 'H', 'S']
# Numeric corresponds to rank with 'T' for 10, 'J' for Jack, 'Q' for Queen, 'K' for King, and 'A' for Ace
Value_list = ['2', '3', '4', '5', '6', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

# This dictionary is used to pull from the card call the values of each assigned and suit for use in hand determination
rank_dictionary = {
        '2': 1,
        '3': 2,
        '4': 3,
        '5': 4,
        '6': 5,
        '7': 6,
        '8': 7,
        '9': 8,
        'T': 9,
        'J': 10,
        'Q': 11,
        'K': 12,
        'A': 13
        }
suit_dictionary = {
        'S': 4,
        'H': 3,
        'D': 2,
        'C': 1

        }

#%%  Making a deck using lists instead of new class functions
deck2 = [[v + s] for s in Suit_list for v in Value_list]
print(deck2)

#%% Draw a random hand

#Use this function to draw a random 5 card hand from the deck
def draw_a_hand():
    random_hand = random.sample(deck2, 5)
    return random_hand

draw_a_hand()

#%% Auto hand-drawer and visualizer

# Enter the number of hands you desire to generate
how_many_hands = 1

#Do you want images to appear for each hand (if yes, input 1, if false input 0?
make_images_appear = True


def these_are_your_hands():
    '''This function will randomly assign a given number of 5 card hands and generates images of them if chosen'''
    # This draws one's unique 5-card hand
    random_hand = draw_a_hand()
    # This calls the png file associated with each card the player names
    card1_file = str(random_hand[0]) + '.png'
    card2_file = str(random_hand[1]) + '.png'
    card3_file = str(random_hand[2]) + '.png'
    card4_file = str(random_hand[3]) + '.png'
    card5_file = str(random_hand[4]) + '.png'
    # This employs pillow to read the images to later exract data
    card1 = Image.open('Deck_of_cards_with_parentheses/' + card1_file)
    card2 = Image.open('Deck_of_cards_with_parentheses/' + card2_file)
    card3 = Image.open('Deck_of_cards_with_parentheses/' + card3_file)
    card4 = Image.open('Deck_of_cards_with_parentheses/' + card4_file)
    card5 = Image.open('Deck_of_cards_with_parentheses/' + card5_file)

    # the X.size module extracts the pixel height and width of each image; the later functon defines the new image size
    (width1, height1) = card1.size
    (width2, height2) = card2.size
    (width3, height3) = card3.size
    (width4, height4) = card4.size
    (width5, height5) = card5.size

    result_width = width1 + width2 + width3 + width4 + width5
    result_height = max(height1, height2, height3, height4, height5)

    # The final hand image is a new photo generated by stitching the card files at the appropriate locations within a-
    # 2D box (the new box is a result of the combination of widths)
    hand = Image.new('RGB', (result_width, result_height))
    hand.paste(im=card1, box=(0, 0))
    hand.paste(im=card2, box=(width1, 0))
    hand.paste(im=card3, box=(width1 + width2, 0))
    hand.paste(im=card4, box=(width1 + width2 + width3, 0))
    hand.paste(im=card5, box=(width1 + width2 + width3 + width4, 0))

    # Pulls individual card files from the hands by indexing one card at a time
    card1_call = (random_hand[0])

    # Parses out each key character (rank and suit) per card for use in hand ranking determinations
    card1_value = (card1_call[0][0:1])
    card1_suit = (card1_call[0][1:2])

    if make_images_appear == 1:
        return Image._show(hand), list(random_hand), print(random_hand), print(dict.get(rank_dictionary, card1_value)), print(dict.get(suit_dictionary, card1_suit))
    elif make_images_appear == 0:
        return list(random_hand), print(random_hand), print(dict.get(rank_dictionary, card1_value)), print(dict.get(suit_dictionary, card1_suit))
    else:
        return print("Do you want to see hands?  How many hands?  Don't forget to fill in your preferences!")

for i in range(how_many_hands):
    these_are_your_hands()


#%% Choose images function

# Do you want images to appear for each hand (if yes, input 1, if false input 0?
make_images_appear = False

    if make_images_appear == 1:
        return Image._show(hand), list(random_hand), print(dict.get(rank_dictionary, card1_value)), print(dict.get(suit_dictionary, card1_suit))
    else:
        return list(random_hand), print(dict.get(rank_dictionary, card1_value)), print(dict.get(suit_dictionary, card1_suit))



#%% Assigning hand values

test_hand2 = list(random.sample(deck2, 5))
print(test_hand2)

# Operation first indexes the card a positions 1, 2, 3, 4 ,5 in the hand an converts the list to a string
# This string contains six characters ['VS'] (where v=value and s=suit); therefore card value is pulled using
# [2:3] and suit is pulled using [3:4]. (Example below)
card1_value = (str((test_hand2[0]))[2:3])
card1_suit = (str((test_hand2[0]))[3:4])

print(card1_value)

# Operation employs the previous method and looks up pulled suit and value info against a dictionary
# assigning an integer to each for use in hand rankings

card1_dict_value = rank_dictionary[card1_value]
card1_dict_suit = suit_dictionary[card1_value]

print(card1_dict_value)

#%% Hand rankings
th = [['AH'], ['2S'], ['9D'], ['KC'], ['TD']]

card1_value = (str((th[0]))[2:3])
card1_suit = (str((th[0]))[3:4])
card2_value = (str((th[1]))[2:3])
card2_suit = (str((th[1]))[3:4])
card3_value = (str((th[2]))[2:3])
card3_suit = (str((th[2]))[3:4])
card4_value = (str((th[3]))[2:3])
card4_suit = (str((th[3]))[3:4])
card5_value = (str((th[4]))[2:3])
card5_suit = (str((th[4]))[3:4])


#Dictionary calls for ranks and suits
cdv1 = rank_dictionary[card1_value]
cds1 = suit_dictionary[card1_suit]
cdv2 = rank_dictionary[card2_value]
cds2 = suit_dictionary[card2_suit]
cdv3 = rank_dictionary[card3_value]
cds3 = suit_dictionary[card3_suit]
cdv4 = rank_dictionary[card4_value]
cds4 = suit_dictionary[card4_suit]
cdv5 = rank_dictionary[card5_value]
cds5 = suit_dictionary[card5_suit]

hs = [cds1, cds2, cds3, cds4, cds5]
hs.sort(reverse=True)
hv = [cdv1, cdv2, cdv3, cdv4, cdv5]
hv.sort(reverse=True)

def flush_check():
    if len(set(hs)) == 1:
        return True, print('Flush!')
    if len(set(hs)) == 2:
        print('four to a Flush!')
    if len(set(hs)) == 3:
        print('three to a Flush!')
    else:
        return False

def straight_check():
    if hv[0]==hv[4]+4 or hv == [13, 4, 3, 2, 1]:
        return True, print('Straight!'), straight_flush_counter==+1
    if hv[0] == hv[3]+3 or hv[1] == hv[4]+3:
        print('four to a Straight!')
    if hv[0] == hv[2]+2 or hv[2] == hv[4]+2 or hv[1] == hv[3]+2:
        print('three to a Straight!')
    else:
        return False

def straight_flush_check():
    if flush_check()[0] and straight_check()[0] == True:
        return True, print('Straight Flush!')
    else:
        return False

def pair_check():
    if len(set(hv)) == 4:
        return True, print('Pair!')
    else:
        return False

def two_pair_and_three_of_a_kind_check():
    if len(set(hv)) == 3 and (hv[0] == hv[2] or hv[2] == hv[4]):
        return True, print('Three of a Kind!')
    if len(set(hv)) == 3:
        return True, print('Two Pair!')
    else:
        return False

def full_house_check():
    if len(set(hv)) == 2:
        return True, print('Full House!')
    else:
        return False

def high_card_check():
    if full_house_check == False and two_pair_and_three_of_a_kind_check() == False and pair_check == False:
        return True, print('High Card!')
    else:
        return False

flush_check()
straight_check()
full_house_check()
two_pair_and_three_of_a_kind_check()
pair_check()
high_card_check()
#%%Check your hand status



#####TO DO!!!!!!!!!!!!!!

### 1) Enter hand classifications
###    counter system in a while loop?
### 2) Build decision tree for player decisions in Jacks or Better
###
### 3)USe pandas to build/organize info on hands in excel sheet before shuttling t