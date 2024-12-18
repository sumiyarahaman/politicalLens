Project Description: The purpose of this project is to take urls of new articles from the internet and determine political bias of the articles using a rule based approach. In this process, I utilized a predefined list of words for each side and compared it to words in the article. I determined political bias by the highest count of words from a specific predefined list(right, left, or neutral). Additionally, the program calculates the bias percentage based on total word count for each side. This is displayed along with the bias result. 

How To Use:
Prerequisites-
Install Python 3.9 or higher.
Install the required dependencies: 
pip install newspaper3k nltk
import nltk
nltk.download('punkt')

Steps- 
Add urls into urls list in data.py with the URLs of the articles you want to analyze or use the provided URLS

Execute data.py to download articles and save their content.

Add text files for each article (article1.txt, article2.txt, etc.) in file_paths list in main.py 

Run the main.py script and view results for each article 

The output in the console should display the title of each article, percentage of keywords present for each side, and bias results


![Problem Formulation for the Project](politicalLens/ProblemFormulation.png)
