# RadioLoggingApp

1.	Create virtual environment: 

    python3 -m venv venv
    
    OR
    
    python -m venv venv
    
    NOTE:  On the work laptop, use the following if you experience problems:
    
    python -m venv .venv

2. Point to virtual environment by trashing terminal and opening a new terminal to activate your virtual environment

    You can alternately run the terminal code to do this, but the above is easier

    Command to activate the virtual environment:

            Mac/linux: source ./venv/bin/activate
    
            Windows: venv\bin\activate.bat
  
3. Install requirements.txt (or req.txt for Linux)

    --- ON PERSONAL MACHINE ---

    pip install -r requirements.txt (Python 2)
    
    OR
    
    pip3 install -r requirements.txt (Python 3)
    
    --- ON COMPANY LAPTOP (REGULAR NETWORK) ---
    
    pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
    
    --- ON DEVELOPMENT LINUX SERVER ---

    pip install -r req.txt

4. Create .env file
    
    The file .env.sample shows the template needed to enter your database URL
    
5. Run the app: 

        Normal Mode: flask run
        Development Mode (shows changes without restarting server): FLASK_ENV=development flask run 
        
6.  You should be able to view the app in the browser at: http://127.0.0.1:5000/
        
JUST A NOTE: 

To install anything with pip when using the company laptop, use the following: 

pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org <package_name>
