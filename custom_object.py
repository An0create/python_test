class MyFirstClass():
    print("Who wrote this?!")
    index = "Author-Book"

    def hand_list(self, philosopher, book, year):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book + " in " + year)

whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War", "1939")
