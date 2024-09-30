# -*- coding: utf-8 -*-
import sys
import greetings  # Εισαγωγή του κώδικα από το αρχείο greetings.py

def test_greeting_variable():
    # Έλεγχος αν η μεταβλητή greeting υπάρχει και περιέχει την τιμή 'Hello, World!'
    assert hasattr(greetings, 'greeting'), "There isnt 'greeting' in greetings.py"
    assert greetings.greeting == 'Hello Python', " 'greeting' not having  'Hello Python'"

def test_print_output(capsys):
    # Εκτελεί το πρόγραμμα και ελέγχει την έξοδο του print
    main_output = greetings  # Εισαγωγή του αρχείου για να τρέξει το πρόγραμμα
    out, err = capsys.readouterr()  # Capture output
    sys.stdout.write(out)
    sys.stderr.write(err)
    assert out == 'Hello Python', "It didnt print 'Hello Python'"
