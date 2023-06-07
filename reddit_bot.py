import praw
import config
import time
import openai
import os

SUBREDDIT = "ADD SUBREDDIT TO BE MONITERED HERE"
openai.api_key = config.open_ai_secret_key


def authenticate_reddit():
    print("Authenticating....")
    reddit = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.reddit_client_id,
                client_secret = config.reddit_client_secret,
                user_agent = "bot 1")
    print("Authenticated successfully as {} \n \n \n \n".format(reddit.user.me()))
    return reddit

def ask_gpt(str):
    message = []
    message.append({"role": "user", "content": str})
    response = openai.ChatCompletion.create(model = "gpt-3.5-turbo", 
                                            messages = message)
    reply = response["choices"][0]["message"]["content"]
    return reply

def run_bot(reddit,comment_read):
    for comment in reddit.subreddit(SUBREDDIT).comments(limit = 10):
        if "!askgpt|" in comment.body and comment.id not in comment_read and comment.author != reddit.user.me():
            print(comment.body + "\n \n")
            message = comment.body.split("|")
            reply = ""
            for question in message:
                if message != "!askgpt":
                    reply += "|" + ask_gpt(question) + "|"
                comment.reply(reply)
            comment_read.append(comment.id)
            with open("comments_replied.txt", "a") as f:
                f.write(comment.id + "\n")
    
    print(comment_read)
    
    time.sleep(10)

def saved_comments():
    if not os.path.isfile("comments_replied.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = filter(None, comments_replied_to)
    return comments_replied_to


if __name__ == '__main__':
    log = authenticate_reddit() 
    comment_reply = list(saved_comments())
    print(comment_reply)
    while True:
        run_bot(reddit=log, comment_read=comment_reply)


