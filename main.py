
import linecache #package to read lines

#function to open and read files
def read_files(file_path):
    with open(file_path, 'r') as file:
        text = file.read() #read files
        text = text.lower() #lowercase all text 
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

#function for determining 
def bias_detector(text):
    
    words = text.split()  # Split text into words
    total_words = len(words)  # Total word count


    # add the number of keywords found in a file
    right_count = sum(keyword in text for keyword in right_leaning_keywords)
    left_count = sum(keyword in text for keyword in left_leaning_keywords)
    neutral_count = sum(keyword in text for keyword in neutral_keywords)

    #calculate the percentage of bias based on total words
    if total_words > 0:
        right_percentage = (right_count / total_words) * 100 
        left_percentage = (left_count / total_words) * 100 
        neutral_percentage = (neutral_count / total_words) * 100 

    # Determine bias based on the higher count 
    if right_count > left_count and neutral_count:
        bias = "Right Leaning"
    elif left_count > right_count and neutral_count:
        bias = "Left Leaning"
    else:
        bias = "Neutral"

    #returns the bias result
    return {
        "bias": bias,
        "right_percentage": right_percentage,
        "left_percentage": left_percentage,
        "neutral_percentage": neutral_percentage,
        "total_words": total_words
    }
#iterate through each given article in file_path
for fpath in file_paths:
    text = read_files(fpath)
    
    title_line = linecache.getline(fpath, 1).strip() #extract the first line of each article(containing title)

    result = bias_detector(text) #call the bias detector function

    #displays the results
    print(" ")
    print(f"Article Title: {title_line}") #print title of article
    print(f"Bias Detection Result: {result["bias"]}") #print the article bias
    print(f"Right-Leaning Bias Percentage: {result['right_percentage']:.2f}%") #print the percentage of bias percentage for each side
    print(f"Left-Leaning Bias Percentage: {result['left_percentage']:.2f}%")
    print(f"Neutral Bias Percentage: {result['neutral_percentage']:.2f}%")
    print(f"Total Words: {result['total_words']}") #total word count
    print(" ")

