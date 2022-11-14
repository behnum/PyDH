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
# Returns a list containing all the words w/o punctuations
def get_all_words(content):
    text = content.translate(str.maketrans("", "", string.punctuation))
    return text.split()


# Removes stop words from a list
def rem_stop_words(list):
    list = [x.lower() for x in list]
    split_text_no_sw = [word for word in list if word not in stop_words]
    return split_text_no_sw


# Returns top n words
def top_words(input, num_words):
    split_text = get_all_words(input)
    counters = Counter(rem_stop_words(split_text))
    most_freq = counters.most_common(num_words)
    return most_freq


# Generates a curated list of rows to visualise
def generate_rows(words, chapter):
    result_list = []
    for i in range(len(words)):
        item_length = len(words[i][0])
        result_list.append([words[i][0], words[i][1], item_length, chapter])
    return result_list


# Handles vis generation via pandas, seaborn, and matplotlib
def dispense_chart(type):
    if type == "bar":
        # set the plot style
        sns.set(style="whitegrid")
        palette = sns.color_palette(goodies.colors)

        # plot a bar chart
        sns.barplot(
            x=data_frame["Frequency"],
            y=data_frame["Word"],
            palette=palette,
            saturation=1,
            errorbar=None,
        )

        plt.title(
            r"$\bf{"
            + "Top\,20\,Words\,in\,the\,Two\,Chapters"
            + "}$"
            + "\nRed: Chapter 1, Blue: Chapter 2"
        )
        plt.savefig("top_words_barplot.png")
        # plt.show() # Optional
        return
    elif type == "pie":
        word = data_frame["Word"]
        freq = data_frame["Frequency"]

        plt.pie(freq, labels=word, explode=goodies.explode, colors=goodies.colors)

        plt.title(
            r"$\bf{"
            + "Top\,20\,Words\,in\,the\,Two\,Chapters"
            + "}$"
            + "\nRed: Chapter 1, Blue: Chapter 2"
        )

        # plt.legend() # Optional
        plt.savefig("top_words_piechart.png")
        # plt.show() # Optional
        return
    else:
        print(f'\n\n▐░░ Chart type "{type}" not found.')
        return


# Just for aesthetic purposes @-}
goodies.echo_badge()

### 1. Extract the top most frequent words. ==============================
export_filename = "data.csv"
header_fields = ["Word", "Frequency", "Length", "Chapter"]
gen_ch1 = generate_rows(top_words(chapter_1, 10), 1)
gen_ch2 = generate_rows(top_words(chapter_2, 10), 2)

with open(export_filename, "w") as csvfile:
    csvwriter = csv.writer(csvfile)  # Createa csv writer obj
    csvwriter.writerow(header_fields)  # writing the field

    csvwriter.writerows(gen_ch1)  # writing the data rows
    csvwriter.writerows(gen_ch2)  # writing the data rows

print(f"▐░░ Data file has been successfully saved as {export_filename}")
print(f"▐░░ Generating visualisation(s) now ...\n")

### 2. Generate visualization. ===========================================

print("▐░░ Processs finished in: %s seconds\n" % round((time.time() - start_time), 3))
