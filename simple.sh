NOW=$(date -u)
echo "Starting simple script at $NOW"
cd ~
DIR="homework"
if [ ! -d "$DIR" ]; then
        mkdir $DIR
fi
cd $DIR
touch content.txt
echo $NOW >> content.txt
wc -l < content.txt
tail -n1 content.txt
