class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to be sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


print "_" * 10


class Lyrics(object):

    def __init__(self):
        self.refrain = "Green grow the rushes-O"
        self.next = """                                                         
                    I'll sing you two-O!                                        
                    Green grow the rushes-O                                     
                    What is your two-O?                                         
                    Two, two the lily-white boys                                
                    clothed all in green-O                                      
                    """

    def song_body(self):
        print "I'll sing you one-O"

words = Lyrics()
words.song_body()
print words.refrain
print words.next


##NOTES ON THREE WAYS TO GET THINGS FROM THINGS (STORE OBJECTS AND RETRIEVE THEM):
#  1.)
#  dictionary style  -  one file, but transferable
#  mystuff = {'apple', "I am apples!"}
#  print mystuff['apple']  -  RETURNS value "I am apples!"

#  2.)
#  module style  -  created in one file, but especially useful if used in other files
#  In its own text file (for example, named OtherStuff) goes:
#  def apple():
#      print "I am apples!"
#  tangerine = "Living reflection of a dream"  -  just an added variable
# 
#  Once this little script is written, it can be used this way in another script/job:
#  import OtherStuff
#
#  OtherStuff.apple()  -   RETURNS   I am apples!
#  print OtherStuff.tangerine()   -   RETURNS   Living reflection of a dream


#  3.)
#  Class style  -  one file, but transferable
#  class OtherStuff(object):
#
#      def __init__(self):
#          self.tangerine = "And now a thousand years between"
#
#      def apple(self):
#          print "I am classy apples!"
#
#  thing = OtherStuff()      -     Creating an object in the class "OtherStuff"
#  thing.apple()             -     Calls the function 'apple' on thing &  RETURNS   I am classy apples!
#  print thing.tangerine     -     Applies the class "OtherStuff" to tangerine and RETURNS    And
#                                                   now a thousand years between
