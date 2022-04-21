######################
# Import libraries
######################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image


###########################
# Links to customize this app
# Youtube video tutorial = https://www.youtube.com/watch?v=JwSS70SZdyM&t=5786s
# github library with all of the original code = https://github.com/dataprofessor/streamlit_freecodecamp/find/main
# markdown cheat sheat = https://github.com/adam-p/# markdown-here/wiki/Markdown-Cheatsheet
##########################


######################
# Page Title
######################

image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
""")


######################
# Input Text Box
######################

#st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#! sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
#! Assign new variable to text box with parameters as follows
sequence = st.text_area("Sequence input", sequence_input, height=250)
#! split the lines in the sequence
sequence = sequence.splitlines()
#! skip the sequence name (>DNA Query 2) so that it isn't used when counting DNA sequence.
sequence = sequence[1:]
# ? sequence
sequence = ''.join(sequence)  # concatenates list to string.
# ? sequence

#! Prints the input DNA sequence
st.header('INPUT (DNA Query)')
#? sequence

#! 1. Print dictionary
st.subheader('1. Print dictionary')
#! custom function that creates a dictionary for each DNA letter and counts(seq.count) that letter in the sequence.
def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

#! 2.Print text 
st.subheader('2. Print text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' adenine (T)')
st.write('There are ' + str(X['G']) + ' adenine (G)')
st.write('There are ' + str(X['C']) + ' adenine (C)')
