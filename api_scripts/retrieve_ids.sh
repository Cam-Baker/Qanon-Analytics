while read id; do
	echo "curl -X GET -H 'Authorization: Bearer TOKEN' 'https://api.twitter.com/1.1/statuses/show.json?id=${id}'; echo ''; sleep 1" >> run_commands.sh
done < $1

outfile=$(echo $1 | sed -e 's/_tweet_ids.txt//g')
echo $outfile

i=0
total=0
while read line; do
	eval $line | tee -a ${outfile}_full_tweets.txt
	((i++))
	((total++))
	echo $i
	if [[ "$i" -gt 899 ]]; then
		i=0
		echo "${total} lines read. waiting for 15 minutes"
		sleep 60
	fi
done < run_commands.sh

echo "finished with ${total} total tweets"
rm run_commands.sh

