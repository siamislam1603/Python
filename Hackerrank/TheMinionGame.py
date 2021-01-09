def minion_game(string):
    vowel=0
    consonent=0
    len_s=len(s)

    for i in range(len_s):
        if(s[i].upper() in 'AEIOU'):
            vowel+=len_s-i
        else:
            consonent+=len_s-i
    if(vowel>consonent):
        print(f"Kevin {vowel}")
    elif(consonent>vowel):
        print(f"Stuart {consonent}")
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)