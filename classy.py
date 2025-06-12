"""
Title: Classy (SelfMadeClass)
Author: Christopher Lee Crader

This is a completely useless class designed to prove to me that "self"
is just a convention and not a special parameter in any way, shape,
or form. I'm uploading this to Github because I am weird and may want
to show this to somebody.

Note how there is no "self" paramater. Of course, there is, but there also
isn't! You see, I'm my own boss! I paragon among programmers! A truly unique
master of the banal and bombastic alike! ALL SHALL TREMBLE AT MY PARAMETER
NAMING PROWESS!
"""

class SelfMadeClass:
    def __init__(myOwnBoss):
        myOwnBoss.name = "My Own Boss"
        myOwnBoss.amIMyOwnBoss = True
    
    def __repr__(myOwnBoss):
        repr_output = "Am I " + myOwnBoss.name + "? \n"
        if myOwnBoss.amIMyOwnBoss:
            repr_output = repr_output + "YEEEEEAH!!!!!"
        else:
            repr_output = repr_output + "Okay, maybe not."
        return repr_output