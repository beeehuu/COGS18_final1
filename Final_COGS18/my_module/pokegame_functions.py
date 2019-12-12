import random
import webbrowser
#list of all 151 pokemon
grass = ['Bulbasaur', 'Ivysaur', 'Venusar', 'Oddish', 'Gloom', 'Vileplume' ,'Bellsprout' , 'Weepinbell', 'Victeebel', 'Exeggcute', 'Exeggutor', 'Tangela']

fire = ['Charmander', 'Charmeleon', 'Charizard', 'Vulpix', 'Ninetails', 'Growlithe', 'Arcanine', 'Ponyta', 'Rapidash', 'Magmar', 'Flareon', 'Moltres']

water =['Squirtle', 'Wartortle', 'Blastoise', 'Psyduck', 'Golduck', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Tentacool', 'Tentacruel', 'Slowpoke', 'Slowbro', 'Seel', 'Dewgong', 'Shellder', 'Cloyster', 'Krabby', 'Kingler', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Magikarp', 'Gyarados', 'Lapras', 'Vaporeon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops']

flying = ['Pidgey', 'Pidgeotto', 'Pidgeot', 'Spearow', 'Fearow', "Farfetch'd", 'Areodactyl', 'Articuno']

bug = ['Caterpie', 'Metapod', 'Butterfree','Weedle', 'Kakuna', 'Beedrill', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Scyther', 'Pinsir']

normal = ['Rattata', 'Raticate', 'Meowth', 'Persian', 'Duduo', 'Dodrio', 'Lickitung', 'Chansey', 'Kangashan', 'Tauros', 'Ditto', 'Eevee', 'Porygon', 'Snorlax']

electric = ['Pikachu', 'Raichu', 'Voltorb', 'Electrode', 'Electabuzz', 'Jolteon', 'Zapdos']

ground = ['Sandshrew', 'Sandslash', 'Diglett', 'Dugtrio', 'Geodude', 'Graveler', 'Golem', 'Onix', 'Cubone', 'Marowak','Rhyhorn', 'Rhydon']

fairy = ['Clefairy', 'Clefable', 'Jigglypuff', 'Wigglytuff', 'Mr. Mime']

poison = ['Ekans', 'Arbok', 'Nidoran', 'Ninorina', 'Nidoqueen', 'Nidoran', 'Nidorino', 'Nidoking', 'Zubat', 'Golbat', 'Grimer', 'Muk', 'Koffing', 'Weezing']

fighting = ['Mankey', 'Primape', 'Machop', 'Machoke', 'Machamp', 'Himonlee', 'Hitmonchan']

psychic = ['Abra', 'Kadabra', 'Alakazam', 'Drowzee', 'Hypno', 'Jynx', 'Mewtwo', 'Mew']

steel = ['Magnemite','Magneton']

ghost = ['Gastly','Haunter','Gengar']

dragon = ['Dratini', 'Dragonair', 'Dragonite']

legendary =['Mewtwo', 'Mew', 'Articuno', 'Moltres', 'Zaptos', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops']

what_type ="What type is "

#a randomizer for each type
def r_grass():
    output = None
    output = random.choice(grass)
    return output
def r_fire():
    output = None
    output = random.choice(fire)
    return output
def r_water():
    output = None
    output = random.choice(water)
    return output
def r_flying():
    output = None
    output = random.choice(flying)
    return output
def r_bug():
    output = None
    output = random.choice(bug)
    return output
def r_normal():
    output = None
    output = random.choice(normal)
    return output
def r_electric():
    output = None
    output = random.choice(electric)
    return output
def r_ground():
    output = None
    output = random.choice(ground)
    return output
def r_fairy():
    output = None
    output = random.choice(fairy)
    return output
def r_poison():
    output = None
    output = random.choice(poison)
    return output
def r_fighting():
    output = None
    output = random.choice(fighting)
    return output
def r_psychic():
    output = None
    output = random.choice(psychic)
    return output
def r_steel():
    output = None
    output = random.choice(steel)
    return output
def r_ghost():
    output = None
    output = random.choice(ghost)
    return output
def r_dragon():
    output = None
    output = random.choice(dragon)
    return output
def r_legendary():
    output = None
    output = random.choice(legendary)
    return output

#questions for the user
pr_grass = what_type +  r_grass() + "?"
pr_fire = what_type +  r_fire() + "?"
pr_water = what_type +  r_water() + "?"
pr_flying = what_type +  r_flying() + "?"
pr_bug = what_type +  r_bug() + "?"
pr_normal = what_type +  r_normal() + "?"
pr_electric = what_type +  r_electric() + "?"
pr_ground = what_type +  r_ground() + "?"
pr_fairy = what_type +  r_fairy() + "?"
pr_poison = what_type +  r_poison() + "?"
pr_fighting = what_type +  r_fighting() + "?"
pr_psychic =what_type +  r_psychic() + "?"
pr_steel =what_type +  r_steel() + "?"
pr_ghost = what_type +  r_ghost() + "?"
pr_dragon = what_type +  r_dragon() + "?"
pr_legendary = "What is " +  r_legendary() + "?"

#shortcuts for the questions
a = pr_grass
b = pr_fire 
c = pr_water
d = pr_flying
e = pr_bug
f = pr_normal
g = pr_electric
h = pr_ground
i = pr_fairy
j = pr_poison
k = pr_fighting
l = pr_psychic
m = pr_steel
n = pr_ghost
o = pr_dragon
p = pr_legendary

#a list of all the questions
all_q = [a, b, c ,d , e, f ,g, h, i, j, k, l, m, n, o, p]

#to define a question and its answer
class QA:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

#corresponding the question to the right answer
correct_a= [
    QA(all_q[0], "grass"),
    QA(all_q[1], "fire"),
    QA(all_q[2], "water"),
    QA(all_q[3], "flying"),
    QA(all_q[4], "bug"),
    QA(all_q[5], "normal"),
    QA(all_q[6], "electric"),
    QA(all_q[7], "ground"),
    QA(all_q[8], "fairy"),
    QA(all_q[9], "poison"),
    QA(all_q[10], "fighting"),
    QA(all_q[11], "psychic"),
    QA(all_q[12], "steel"),
    QA(all_q[13], "ghost"),
    QA(all_q[14], "dragon"),
    QA(all_q[15], "legendary"),
    
]

#the function for the quiz game to work
def run_quiz(correct_a):
    print("You will be given 16 questions to answer.")
    print("Your choices are: poison, fire, ground, water, fairy, grass, bug, normal, electric, flying, fighting, dragon, ghost, steel, and psychic. There might be a special one.")
    #code from an online source 
    score = 0
    for QA in correct_a:
        answer = input(QA.question)
        if answer == QA.answer:
            score +=1
    #My code
    print("you got "+ str(score) + " out of 15! Now activate talk_time for some support!")
    if answer == "legendary":
        output = webbrowser.open_new_tab("https://www.youtube.com/watch?v=MqX4Se5V5RA") , " GOOD JOB YOU GOT THE LEGENDARY QUESTION RIGHT!"
    else:
        output = None
    return output
    
#responses for the chatbot
happy_q = "Are you happy with your score?"
happy_y = ['yes','yeah','yuh','sure']
happy_n = ['no', 'nah','nope']

it_okay = "I think you did great, but if you didn't you can do the quiz again!"
another_chance = "The questions are the same so I believe you can get it!"
confused = "I'm sorry I don't fully understand."

end_s = "You did well and your score does not define you!"
good_s = "Thats good to hear you are happy with your score!"
type_okay = "please type in 'okay'"

okay_s = "Would looking at a list of the pokemon help?"
link_s = "Type in 'link' and a browser of the pokemon will open!"
help_s = "I hope this helps!"
better_s = "Now try the quiz again! I think you get a better score!"
exit_s= "To exit type in 'quit' and start run_quiz again!"
one_way = "Only one way to find out!"

#Code from A3

#prepares text to be easily interpreted
def prepare_text(input_string):
    for x in input_string:
        temp_string = input_string.lower()
        out_list = temp_string.split()
    return out_list

#puts strings together if needed
def string_concatenator(string1,string2,separator):
    output = string1 + separator + string2
    return output

#changed a list into a string
def list_to_string(input_list, separator):
    output = input_list[0]
    for x in input_list[1:]:
        output = output + separator + x
    return output

#ends the chat 
def end_chat(input_list):
    if 'quit'in input_list:
        output = True
    else:
        output = False
    return output

#check if yes is in the input
def good(input1):
    if "yes" in input1:
        output = True
    else:
        output = False
    return output

#check if no is in the input
def bad(input1):
    if "no" in input1:
        output = True
    else:
        output = False
    return output

#checks if okay is in the input
def okay(input1):
    if "okay" in input1:
        output = True
    else:
        output = False
    return output

#checks if the input is a link
def is_link(input1):
    if "link" in input1:
        output = True
    else:
        output = False
    return output

#responds to the user of intrest
def wow(input1):
    if "yeah" in input1:
        output = True 
    else:
        output = False
    return output
def yikes(input1):
    if 'nah' in input1:
        output=True
    else:
        output = False
    return output

        
#activate the chatbot
def talk_time():
    
    chat = True
    
    print(happy_q+" yes or no?")
    
    while chat:
        #gets input from user
        msg = input('User : ')
        msg = prepare_text(msg)
            
        if end_chat(msg):
            out_msg = end_s
            chat = False
        elif good(msg):
            out_msg = good_s + ' ' +type_okay
            
        elif bad(msg) :
            out_msg = it_okay + " " +another_chance + " " +type_okay
            
        else:
            out_msg = confused
            
        if okay(msg):
            out_msg = okay_s + " " +link_s
        
        #opens a link if this function is true
        if is_link(msg):
            out_msg = webbrowser.open("https://www.pokemon.com/us/pokedex/") , " This should help right? Yeah or nah?"
            
        if wow(msg) :
            out_msg = one_way + " " + help_s +" "+ better_s +" "+ exit_s
            
        if yikes(msg):
            out_msg = one_way + " " + help_s +" "+ better_s +" "+ exit_s
            

        print('Comp :', out_msg)