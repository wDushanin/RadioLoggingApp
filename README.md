# RadioLoggingApp

1.	Create virtual environment: 

    python3 -m venv venv

2. Point to virtual environment by trashing terminal and opening a new terminal to activate your virtual environment

    You can alternately run the terminal code to do this, but the above is easier

    Command to activate the virtual environment:

            Mac/linux: source ./venv/bin/activate
    
            Windows: venv\bin\activate.bat
  
3. Install requirements.txt

    Run pip install -r requirements.txt (Python 2), or pip3 install -r requirements.txt (Python 3)

4. Run the app: 

        Normal Mode: flask run
        Development Mode (shows changes without restarting server): FLASK_ENV=development flask run 
