def compressWord(word, k):
    # Write your code here



    new_word = word


    while len(new_word) != len(compress(new_word, k)):
        new_word_list = compress(new_word, k)
        new_word = ""
        new_word = new_word.join(new_word_list)

    return new_word


def compress(word, k):
    word = list(word)
    for x in range(0, len(word) - 2):
        k_sub = word[x:x + k]

        if len(set(k_sub)) == 1:
            for y in range(0, k):
                word.pop(x)

            break

    return word

word = ["b", "a", "a", "c"]
k = 2

word_str = ""
word_str = word_str.join(word)
print(compressWord(word_str, k))