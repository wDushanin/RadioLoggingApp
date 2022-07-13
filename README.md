# RadioLoggingApp

1.	Create virtual environment: 

    python3 -m venv venv
    
    OR
    
    py -m venv venv

2. Point to virtual environment by trashing terminal and opening a new terminal to activate your virtual environment

    You can alternately run the terminal code to do this, but the above is easier

    Command to activate the virtual environment:

            Mac/linux: source ./venv/bin/activate
    
            Windows: venv\bin\activate.bat
  
3. Install requirements.txt

    pip install -r requirements.txt (Python 2)
    
    OR
    
    pip3 install -r requirements.txt (Python 3)
    
    OR (when using company laptop)
    
    pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

4. Run the app: 

        Normal Mode: flask run
        Development Mode (shows changes without restarting server): FLASK_ENV=development flask run 
        
JUST A NOTE: 

To install anything with pip when using the company laptop, use the following: 

pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org <package_name>
