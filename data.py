from newspaper import Article
import nltk
nltk.download('punkt')

urls = [
    "https://www.cnn.com/2024/12/08/politics/fact-check-trump-meet-the-press/index.html",
    "https://www.foxnews.com/entertainment/snl-slammed-classless-united-healthcare-murder-segment-weekend-update",
    "https://www.npr.org/2024/12/06/nx-s1-5218583/how-many-species-could-go-extinct-from-climate-change-it-depends-on-how-hot-it-gets",
    "https://thefederalist.com/2024/12/06/venezuelan-busted-for-extorting-illegals-in-pa-exposes-evil-side-effect-of-bidens-open-borders/",
    "https://apnews.com/article/trump-immigration-tariffs-pardons-abortion-prosecutions-riot-72c08269f0a870d20e29033319201e22",
    "https://www.politico.eu/article/donald-trump-aukus-kill-us-uk-aussie-sub-defense-deal/",
    "https://news.yahoo.com/news/democrats-republicans-congress-worried-gabbard-032356249.html",
    "https://news.yahoo.com/news/world-warming-faster-expected-scientists-190042831.html",
    "https://www.bloomberg.com/news/articles/2024-12-09/china-shifts-monetary-policy-stance-for-first-time-since-2011?srnd=homepage-americas",
    "https://nypost.com/2024/12/08/us-news/new-house-bill-would-ban-insurers-from-limiting-anesthesia-coverage/",
    "https://www.huffpost.com/entry/chip-roy-pete-hegseth-trump-defense-secretary-pick_n_6753d6e1e4b0807fc897c5b0",
    "https://planetdetroit.org/2024/10/ai-energy-carbon-emissions/#:~:text=Lots%20of%20water,hour%20of%20energy%20they%20consume."
  
]


header = {
     "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}


for url in urls:
    toi_article = Article(url, language="en") 
    toi_article.download()
    toi_article.parse()
    toi_article.nlp()
    
    content = f"""
    Article's Title:
    {toi_article.title}
    
    Article's Text:
    {toi_article.text}
    
    Article's Summary:
    {toi_article.summary}
    
    Article's Keywords:
    {', '.join(toi_article.keywords)}
    """
    
    save_file = "articles.txt"
    with open(save_file, "a", encoding="utf-8") as file: 
        file.write(content + "\n")

