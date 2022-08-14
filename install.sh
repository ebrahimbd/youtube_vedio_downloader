if python3 -c 'import pkgutil; exit(not pkgutil.find_loader("pip"))'; then
    pip install -r requirements.txt
    clear
    python3 yt.py

else
    dpkg install python3 
    pip install -r requirements.txt
    clear
    python3 yt.py

fi

