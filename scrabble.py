import itertools, twl
# Function to create a set of all the possible combinations of letters
def randomize(word):
    t = []
    comb = set()
    for i in range(2, len(word) + 1):
        t = list(itertools.permutations(word, i))
        for j in range(0, len(t)):
            comb.add(''.join(t[j]))
    return comb

# Point Calculator
def calculate_scores(word_dict):
    points_table = {'a' : 1, 'b' : 3, 'c' : 3, 'd' : 2, 'e' : 1, 'f' : 4, 'i' : 1, 'j' : 8, 'k' : 5, 'l' : 1, 'm' : 3, 'n' : 1, 'o' : 1, 'p' : 3, 'q' : 10, 'r' : 1, 's' : 1, 't' : 1, 'u' : 1, 'v' : 4, 'w' : 4, 'x' : 8, 'y' : 4, 'z' : 10}
    try:
        for word in word_dict:
            score = 0
            for letter in word:
                score += points_table[letter]
            word_dict[word] = score
    except KeyError:
        print("Letter Missing")

    return word_dict
              
# Function to see if the words are anagrams
def check_anagram(input_word, word):
    if sorted(input_word) == sorted(word):
            print(word)

# Calculate factorial 
def fact(num):
    sum = 0
    if num <= 1:
        return 1
    else: 
        return (num * fact(num - 1))

# Create a dictionary of all valid combinations
def valid(comb):
    print("All Valid Combinations are:")
    word_dict = {}
    for i in comb:
        if twl.check(i):
            word_dict[i] = 0
    return word_dict

# Displaying from max to min scores
def display(scores):
    print("Word\t\tScores")
    for word in scores:
        print('{}\t\t{}'.format(word.upper(), scores[word]))

        
''' MAIN FUNCTION '''
def main():
    # Input for the letters
    ana = str(input("Enter the String(characters accepted): "))
    combinations = randomize(ana)
    # Creating a dictionary of words
    word_dictionary = valid(combinations)
    scores = calculate_scores(word_dictionary)
    display(scores)
if __name__ == "__main__":
    main()
