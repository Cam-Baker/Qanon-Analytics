date | cut -f 2,3,4,5 -d' ' > tmp
outfile=$(sed -E 's/ |\:/_/g' tmp ).json
rm tmp
gtimeout 10m python -u filtered_stream.py >> /Users/cbaker4/tweet_jsons/$outfile
