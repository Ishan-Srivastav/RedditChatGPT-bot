# RedditChatGPT-bot
A reddit bot which uses praw and openai to integrate chatgpt in reddit comment by prompting !askgpt| in the comments

--------------------------
First change the config.py file as instructed in the file
this step is needed to authenticate and sign in to reddit and access the comments

It is recommended to have a different reddit account to comment other than the one in use as the script accepts responses from everyone except the user

This can be changed by removing the last condition in the second line of run_bot function {and comment.author != reddit.user.me()}
