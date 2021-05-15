import random


# main function
def main():
    # variable for continuing to generate names
    keep_going = 'y'
    # while loop that generates names
    while keep_going == 'y':
        print('Welcome to the Wild West Name Generator!')
        # input
        gender = input('Please enter what gender you would like. (M)ale or (F)emale?: ')
        # input validation loop
        while gender not in ['M', 'm', 'F', 'f']:
            # input
            gender = ('ERROR! You must enter either (M)ale or (F)emale!: ')
        # if-else statement for processing F/M input
        if gender == 'F' or gender == 'f':
            # generates female name
            name = generate_female_name()
            # output
            print('Your Wild West name is:', name)
        else:
            # generate male name
            name = generate_male_name()
            # output
            print('You Wild West name is:', name)
        # asks user if they want to keep going
        keep_going = input('Would you like to generate a new name? Y/N?: ')
        # input validation
        while keep_going not in ['Y', 'y', 'N', 'n']:
            keep_going = input('ERROR! You must enter Y/N: ')


# function to generate female names
def generate_female_name():
    # lists of names
    descriptor = ['Sharp Shooting', 'Gun-slinging', 'Dynamite', 'Crazy', 'Slippery', 'Safe-cracking'
                  'Ma', 'Madam', 'Miss', 'Gun-toting', 'Slick-fingered', 'Swindling', 'Blackjack',
                  'Crooked', 'Ol Gal', 'Hell-raising', 'Stagecoach', 'Wild', 'Cattle-rustling',
                  'Buffalo']
    first_name = ['Annie', 'Mary-lou', 'Sadie', 'Delilah', 'Isabelle', 'Belle', 'Joanne', 'Jo',
                  'Kate', 'Jane', 'Pearl', 'Lottie', 'Rose', 'Laura', 'Mary', 'Anne', 'Yolanda',
                  'Lolita', 'Juana', 'Josie']
    last_name = ['Oakley', 'Starr', 'Jenkins', 'Hart', 'Smith', 'Dumont', 'Dunn', 'Fields', 'James',
                 'McCarty', 'O\'Driscoll', 'Cassidy', 'Hickok', 'Crockett', 'Escuella', 'Rodriguez']
    # generates random name from lists
    name = random.choice(descriptor) + ' ' + random.choice(first_name) + ' ' + random.choice(last_name)
    return name


# function to generate male names
def generate_male_name():
    # lists of names
    descriptor = ['Sharp Shooting', 'Gun-slinging', 'Dynamite', 'Crazy', 'Slippery', 'Safe-cracking',
                  'Gun-toting', 'Slick-fingered', 'Swindling', 'Blackjack', 'Crooked', 'Ol Man',
                  'Hell-raising', 'Stagecoach', 'Smooth-talking', 'Wild', 'Rattlesnake',
                  'Cattle-rustling', 'Buffalo']
    first_name = ['Jesse', 'Bill', 'John', 'Billy', 'Davy', 'Joe', 'Bob', 'Sam', 'George', 'Ed',
                  'Charlie', 'Joaquin', 'Jose', 'Eduardo', 'Dick', 'Frankie', 'Emmett', 'Dan', 'Jim',
                  'Jimmy', 'Jack', 'Ned']
    last_name = ['Oakley', 'Starr', 'Jenkins', 'Hart', 'Smith', 'Dumont', 'Dunn', 'Fields', 'James',
                 'McCarty', 'O\'Driscoll', 'Cassidy', 'Hickok', 'Crockett', 'Escuella', 'Rodriguez']
    # generates random name from lists
    name = random.choice(descriptor) + ' ' + random.choice(first_name) + ' ' + random.choice(last_name)
    return name


main()
