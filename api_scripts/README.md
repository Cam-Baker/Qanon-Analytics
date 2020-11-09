# Overview

These scripts help grab and parse tweets related to the Qanon movement. I grabbed tweet id's corresponding to the following hashtags using Twitter's [filtered stream](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/introduction).

- Qanon  
- WWG1WGA  
- wwg  
- wga 

Tweets were mined from early-mid September until November 9th. I grabbed tweets for 10 minutes on the top of and the middle of each hour. This was done using the following cronjob.

`*/30 * * * * export PATH=$PATH:/usr/local/bin/:/Users/cbaker4/opt/miniconda3/bin:/Users/cbaker4/opt/miniconda3/condabin:/Library/Frameworks/Python.framework/Versions/3.8/bin/ && source activate python && cd /Users/cbaker4 && sh run_tweets.sh`

I also include some sample output of the pipeline as `sample.csv`.

## run_tweets.sh

Runs the Twitter provided `filter_stream.py` for 10 minutes, putting the output into an outfile prepended with the current date and time.

## get_ids.sh

Because twitter does not return the full content of the tweet, we need to make an api call against the tweet id to get the full content. This script parses out the tweet id's for a list of jsons (as provided by `run_tweets.sh`).

## retrieve_ids.sh

This script generates an HTTP request for the full content of each tweet and the runs them. It also sleeps for 1 second between each call. Originally, I had the sleep time at 0.1 seconds, but this raised issues with api abuse.

## parse_tweets.py

I parse the information I need from the full json output of the content, and write it as a csv.
