class library(list):
    def __init__(self):
        library()
    pass
        
class books(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author        
        
class shelf(library):
    def __init__(self, position):
        self.position = position
    def __repr__(self):
        
books 
    {'Red': 'Tom Green', 'White': 'Jim Blue', 'Moose': 'Eric White'}
answer = raw_input("To shelf or unshelf book input 'shelve 'title' to 'shelf' ").lower()
if answer == "shelve %s to shelf %s" % (books[key], shelf[key]):
    print "%s is now on %s" % (books[key], shelf[key])
elif answer == "unshelve %s" % (books[key]):
    print "%s has been removed from the library" %s
else:
    print "Incorrect format. Try again."        
                   
shelf1 = ()
shelf2 = ()
shelf3 = ()
library = [shelf1, shelf2, shelf3]

#So I know that the code doesnt work, but I feel like I'm at a point where I just need a little bit of guidance
#to understand what I'm not getting. 
