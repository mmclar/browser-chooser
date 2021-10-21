virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
sudo desktop-file-install ~/projects/browser-chooser/browser-chooser.desktop 
sudo update-desktop-database 
