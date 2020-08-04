# SocialMediaAnalysis
Please note: this repository is for academic and research purposes.
This repository uses web crawlers to scrape comments on social media platforms and analyze them for sentiment, polarization, subjectivity, emotion, and importance. Correlation Explanation is an algorithm used for topic modeling. The topics can then be tracked for trends over time. There is also a document summarization algorithm based on frequency.
Collect Data -> EDA -> Modeling

## TikTok Scraper

#### Requirements:
1. Create a TikTok account with Facebook as this is the sign in strategy of the crawler.
2. Install Selenium.
3. Download chrome driver here https://sites.google.com/a/chromium.org/chromedriver/downloads. Make sure to match the driver version with your chrome browser version. Unzip, make note of its path.
4. Path to chromedriver is marked in the code, be sure to change this.
5. Change path to save JSON file if you'd like.
6. Jupyter Notebook is preferred. Scripts are currently .ipynb

#### Inputs:
Before executing, make sure to change the hashtag variable to the url to that of the trend to be scraped. The url is set to "https://www.tiktok.com/tag/stimuluscheck?lang=en&loginType=facebook". 
Simply change hashtag to "https://www.tiktok.com/tag/Entrepreneur?lang=en&loginType=facebook".
Username and password are requested by the main method.

#### Outputs:
The crawler will dump a list format of the content into a json file. The json file is not in dictionary format, it is simply a list with superior formatting. Each post is separated by "New Post" in the list. Sample data is provided. An example of using this program is provided in main method. Caption, likes, comments, username, emojis, and replies are stored.

#### Limitations/Execution: 
1. The most popular 30 video links are gathered, then scraping the entire visible page.
2. For debugging purposes, the browser is not headless.
3. We attempted to use the requests library to fetch user data but were unable to automate the process due to a dynamically generated key.
4. Replies to comments are limited to four levels deep. This means that if there are many replies to comments, it will gather 16 of those replies before moving to the next comment.
5. It is difficult to differentiate between replies to comments and new comments unless the replier tags the user.
6. Execution time is slow due to the nested for loop clicking each view more reply. 

## Reddit Scraper

#### Requirements:
1. To access Reddit API, you must get approved for an API access token. The client ID and secret key are parameters of the scraper.
2. Install praw for API calls and data collection.
3. Change storage path of the csv files accordingly.
4. Jupyter Notebook if preferred. Current program is in .ipynb.

#### Inputs:
Client ID, secret ID, and desired subreddit are inputs in the main method. Make sure to change file names of both post and comments files to match the subreddit as well. An example of the code usage is in the main method.

#### Outputs:
The function outputs eleven csv files.

One csv contains details of the ten hottest posts from the subreddit. It collects: title, score, id, subreddit, url, number of comments, and body.

10 csv files are then created, each dedicated to one post from the ten hottest posts within that subreddit. Within the csv, the first level comments are scraped, followed by all replies, followed by all replies to replies until there are none left.
csv files are index 0 to 9, csv file 0 relating to hottest post 1 of the subreddit.


#### Limitations/Execution:
The main limitation is that replies are not collected under the comment they are replying to.
User data is also not collected.
However, this script executes quickly.

## Facebook Scraper
This Facebook Scraper was made for tutorial/research purposes on crawling with Selenium.

#### Requirements:
1. Selenium
2. Chromedriver (make sure to change path in code)
3. Facebook Account

#### Inputs:
Username, password, mbasic url link to public Facebook page, and number of posts deep.

#### Outputs:
JSON file with all posts content, comments, replies, likes, and timestamps from x amount of posts in list format.

#### Limitations/Execution:
1. mBasic Facebook URLs must be used for ease of crawling.
2. Likes, comments, usernames, replies, post content, and timestamps are collected.
3. Reply conversations with more than one reply have the first/source comment duplicated.
4. All comments from the first page of comments are scraped, then the replies, then 'Show more' is clicked and more comments/replies are scraped.
5. When a comment only has one reply, that reply is not scraped.
6. The number of likes are scraped but separated by unicode in the JSON file. ie. '9/u001Likes'
7. Unicode is scraped.
8. Emojis are scraped.
9. The parameter 'deep' indicates how many times 'Show more posts' will be clicked, thus how many posts will be scraped.
10. The script is dependent on a part of the link matching (marked in class), this must be changed to match the source code.
