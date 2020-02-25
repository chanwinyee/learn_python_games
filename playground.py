# print('Set a range for your "For" loop.')
# set_range = int(input())

# for i in range(set_range):
#     print('Hello! i is set to', i)

# print('This is the end of the loop.')


# HANGMAN_PICS = ['''
#     +---+
#         |
#         |
#         |
#        ===''','''
#     +---+
#     O   |
#         |
#         |
#        ===''','''
#     +---+
#     O   |
#     |   |
#         |
#        ===''','''
#     +---+
#     O   |
#    /|   |
#         |
#        ===''','''
#     +---+
#     O   |
#    /|\  |
#         |
#        ===''','''
#     +---+
#     O   |
#    /|\  |
#    /    |
#     ===''','''
#     +---+
#     0   |
#    /|\  |
#    / \  |
#        ===''']

# print(HANGMAN_PICS[0])
# print(HANGMAN_PICS[3])
# print(HANGMAN_PICS[6])

# animals = ['aardvark','anteater','antelope','albert']
# print(animals)
# print(animals[0])

sentence = 'I am a big cat, who eats a lot of cans'
words = sentence.split()
print(words)
sentence=input()
words = words + sentence.split()
print(words)