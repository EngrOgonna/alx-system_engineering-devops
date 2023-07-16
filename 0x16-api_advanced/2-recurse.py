import requests

def count_keywords(subreddit, keywords):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    data = response.json()

    titles = [post["data"]["title"] for post in data["data"]["children"]]
    keyword_count = {keyword: 0 for keyword in keywords}

    for title in titles:
        words = title.lower().split()
        for keyword in keywords:
            if keyword.lower() in words:
                keyword_count[keyword] += 1

    for keyword, count in sorted(keyword_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{keyword}: {count}")

    after = data["data"]["after"]
    if after is not None:
        count_keywords(subreddit, keywords)
