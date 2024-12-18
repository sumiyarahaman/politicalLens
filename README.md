Project Description: The purpose of this project is to take urls of new articles from the internet and determine political bias of the articles using a rule based approach. In this process, I utilized a predefined list of words for each side and compared it to words in the article. I determined political bias by the highest count of words from a specific predefined list(right, left, or neutral). Additionally, the program also determines the percentages of bias for each side based on the total word count. 

How to use:
Install Python 3.9 or higher.
Install the required dependencies:
pip install newspaper3k nltk
import nltk
nltk.download('punkt')

Steps
Update the urls list in the script with the URLs of the articles you want to analyze or use the give urls

Execute the Python script to download articles and save their content

Output-
Text files for each article (article1.txt, article2.txt, etc.) saved in the current working directory.
A console output displaying the bias results for each article with bias percentage for each side based on total word count.

Articles are categorized as-
Right Leaning: More right-leaning keywords detected.
Left Leaning: More left-leaning keywords detected.
Neutral: No significant leaning detected.

