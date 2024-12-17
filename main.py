import os
import linecache #package to read lines

#function to open and read files
def read_files(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        text = text.lower()
    return text

file_paths = ['article1.txt', 'article2.txt', 'article3.txt', 'article4.txt'] #list of files 


# Predefined keyword input list for bias
right_leaning_keywords = [
    "illegal immigration", "border security", "america first", "tariffs", 
    "traditional values", "fentanyl crisis", "government overreach", "smugglers"
]

left_leaning_keywords = [
    "climate change", "social justice", "healthcare", "equity", "diversity", 
    "renewable energy", "global warming", "biodiversity loss", "human rights"
]

neutral_keywords = [
    "election", "federal government", "congress", "trade agreements", 
    "inflation rates", "species extinction", "nasa data"
]


def bias_detector(text):

    # add the number of keywords found in a file
    right_count = sum(keyword in text for keyword in right_leaning_keywords)
    left_count = sum(keyword in text for keyword in left_leaning_keywords)
    neutral_count = sum(keyword in text for keyword in neutral_keywords)

    # Determine bias based on the higher count 
    if right_count > left_count and neutral_count:
        bias = "Right Leaning"
    elif left_count > right_count and neutral_count:
        bias = "Left Leaning"
    else:
        bias = "Neutral"

    #returns the bias result
    return {
        "bias": bias
    }

#iterate through each given article

for fpath in file_paths:
    text = read_files(fpath)
    
    title_line = linecache.getline(fpath, 1).strip() #extract the first line of each article 

    result = bias_detector(text)

    print(" ")
    print(f"Article Title: {title_line}") 
    print(f"Bias Detection Result: {result}")
    print(" ")

