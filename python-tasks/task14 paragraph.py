#task-14 take a paragragh data and replace is with are and there with that


paragraph = "There is a bird on the tree. Is there anyone who can help me?"
updated_paragraph = paragraph.replace("is", "are").replace("there", "that")
print(updated_paragraph)             # Output: That are a bird on that tree. Is that anyone who can help me?


data = '''She is a doctor or The car is red.
          There is an adverb that is used to 
          indicate the existence or 
          presence of something in a 
          particular place or to introduce a
          location or a subject.
          there is a cat on the roof'''

updated_data = data.replace("is", "are").replace("there", "that")
print(updated_data)







