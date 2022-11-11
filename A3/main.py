# Behnam Baharmand
# Assignment 3: Text Processing and Visualization with Python
# Version 0.1.0

# Import resources/libraries
import string
from collections import Counter
import csv
import goodies
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import time

start_time = time.time()  # Let's see how long it takes to run the code

### 0. Setup / Load the content ==========================================

with open("./A3/Sapir1921_chapter1.txt", "r") as ch1_handle, open(
    "./A3/Muller1861_chapter2.txt", "r"
) as ch2_handle, open("./A3/stopwordlist.txt", "r") as swords:
    chapter_1 = ch1_handle.read()
    chapter_2 = ch2_handle.read()
    stop_words = swords.read()


# Function Defenitions @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Just for aesthetic purposes @-}
goodies.echo_badge()

### 1. Extract the top most frequent words. ==============================

### 2. Generate visualization. ===========================================

print("▐░░ Processs finished in: %s seconds\n" % round((time.time() - start_time), 3))
