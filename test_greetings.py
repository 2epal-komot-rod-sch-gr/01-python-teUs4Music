# -*- coding: utf-8 -*-
import sys
import greetings  # Εισαγωγή του κώδικα από το αρχείο greetings.py

def test_greeting_variable():
    # Έλεγχος αν η μεταβλητή greeting υπάρχει και περιέχει την τιμή 'Hello, World!'
    assert hasattr(greetings, 'greeting'), "There isnt 'greeting' in greetings.py"
    assert greetings.greeting == 'Hello Python', " 'greeting' not having  'Hello Python'"

def test_print_output(capsys):
    # Εκτελεί το πρόγραμμα και ελέγχει την έξοδο του print
    #import greetings  # Εισαγωγή του αρχείου για να τρέξει το πρόγραμμα
    #out, err = capsys.readouterr()  # Capture output
    #assert out == "Hello Python\n", "It didnt print 'Hello Python'"
    # Χρήση του importlib για να διασφαλίσεις ότι το greetings επανεκτελείται
    
    importlib.reload(greetings)

    # Καταγραφή της εξόδου μετά την επανεκτέλεση του greetings
    out, err = capsys.readouterr()

    # Εκτύπωση της καταγεγραμμένης εξόδου για debugging
    print(f"Captured Output: '{out}'")

    # Έλεγχος της εξόδου
    assert out == "Hello Python\n", f"It didn't print 'Hello Python', instead got: '{out}'"
