# LOGIC
# Take in a file and replace one word with another
# Create a method to handle the replacement

def word_swap(input_text, look_for, swap):
    return input_text.replace(look_for, swap)


with open("Files/story.txt", encoding="utf-8-sig") as f:
    imported_story = f.read()

print(word_swap(imported_story, "the", "DUCKS"))
