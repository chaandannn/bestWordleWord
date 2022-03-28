with open('wordle.txt') as file:
    wordle_list = [word.split('\n')[0] for word in file.readlines()]

freq = [[0] * 26 for x in range(5)]
for word in wordle_list:
    for index, character in enumerate(word):
        freq[index][ord(character) - 97] += 1

d = []
for word in wordle_list:
    prob = 1.0
    for index, letter in enumerate(word):
        prob *= freq[index][ord(word[index]) - 97]
    d.append([word, prob])

bestWords = sorted(d, key=lambda x: x[1], reverse=True)
for index in range(5):
    print(f"#{index+1:2}: {bestWords[index][0]}")git
