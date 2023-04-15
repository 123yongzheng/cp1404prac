def count_words(text):
    words = text.replace(",", "").replace(".", "").split()
    word_count = {}
    for word in words:
        if word.lower() in word_count:
            word_count[word.lower()] += 1
        else:
            word_count[word.lower()] = 1

    sorted_word_count = sorted(word_count.items())
    max_word_length = max(len(word) for word in word_count.keys())
    for word, count in sorted_word_count:
        print("{word:{width}} : {count}".format(word=word, width=max_word_length, count=count))


text = input("Text: ")
count_words(text)
