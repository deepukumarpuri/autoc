echo "Cloning Repo...."
git clone https://github.com/deepukumarpuri/autoc.git /autoc
cd /autoc
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 channelbot.py
