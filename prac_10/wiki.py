import wikipedia

while True:
    search_phrase = input("Enter a page title or search phrase (or leave blank to exit): ")
    if not search_phrase:
        break

    try:
        page = wikipedia.page(search_phrase, auto_suggest=False)
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
        print()
    except wikipedia.exceptions.DisambiguationError as e:
        print("Disambiguation Error:")
        options = e.options[:5]  # Print the first 5 options
        for option in options:
            print(option)
        print()
    except wikipedia.exceptions.PageError:
        print("Page not found.")
        print()
