
from app.models.dbmodel import *
from app.controls.query import *
import schedule
import time

# Function to run the query periodically
def run_task_schedule():
    """_summary_
    run task while UI exist
    """
    while True:
        try:
            querySqlServer()
            print("loop")
            time.sleep(300)  # Sleep for 4 second
        except Exception as e:
            print(e)
            time.sleep(10)
            
# Function to stop the background task
def stop_task():
    """_summary_
    top task when click event close ui
    """
    global background_thread
    if background_thread:
        background_thread.cancel()

def homeViewQT():
    """_summary_
    desktop view
    """
    from app.templates.index import HomeApp
    root = HomeApp()
    root.protocol("WM_DESTROY", stop_task)
    root.mainloop()

# pyinstaller --onefile --hidden-import schedule --hidden-import pyodbc --hidden-import openpyxl --hidden-import pymongo --hidden-import threading --hidden-import pymssql --hidden-import datetime --hidden-import pillow main.py

