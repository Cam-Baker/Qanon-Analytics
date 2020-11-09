grep data $1 -A 1 | grep id | sed -e 's/",//g' | sed -e 's/        "id": "//g' > $(echo $1 | cut -d'.' -f1 )_tweet_ids.txt
tail -n +3 $(echo $1 | cut -d'.' -f1 )_tweet_ids.txt > tmp
mv tmp $(echo $1 | cut -d'.' -f1 )_tweet_ids.txt
grep -v data $(echo $1 | cut -d'.' -f1 )_tweet_ids.txt > tmp
mv tmp $(echo $1 | cut -d'.' -f1 )_tweet_ids.txt
