# initializes a writer class to specify the words they're writing
class Writer():
    def __init__(self, words):
        self.words = words

# function to write words onto the paper
    def write(self):
        paper_text = my_paper.text
        writer_words = my_writer.words
        setattr(my_paper, 'text', paper_text + writer_words)
        return my_paper.text
        
# create a paper class that starts out blank, then text is added on
class Paper():
    def __init__(self, text = ''):
        self.text = text

# not sure how to continuously add on words to the paper, and also trouble generalizing the code to any Paper or Writer instance created
my_paper = Paper("She sells sea shells")
my_writer = Writer(' down by the sea shore')
print(my_writer.write())

# Creates a Pencil class that takes in durability
class Pencil():
    def __init__(self, durability):
        self.durability = durability

# checks if a letter in the text is upper or lowercase, then breaks when the threshold meets durability
    def input_text(self, text):
        i = 0
        letters = [x for x in text]
        for letter in letters:
            i += 1
            if self.durability == 0:
                undulled = text[:i-1]
                break
            elif letter.isspace() == False:
                if letter.isupper():
                    self.durability -= 2
                elif letter.islower():
                    self.durability -= 1
        
        return undulled
            


x = Pencil(3)
print(x.input_text('Cats  \n'))

# Uncovered degradation use cases: spaces and newlines after the dulled pencil writes