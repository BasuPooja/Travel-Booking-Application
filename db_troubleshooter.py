import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import mysql.connector
from mysql.connector import Error
import os
import subprocess
import sys

class DjangoDBTroubleshooter:
    def __init__(self, root):
        self.root = root
        self.root.title("Django Database Connection Troubleshooter")
        self.root.geometry("950x750")
        self.root.resizable(True, True)
        
        # Apply a theme-like style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('Header.TLabel', background='#2c3e50', foreground='white', font=('Arial', 16, 'bold'))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('TEntry', font=('Arial', 10))
        self.style.configure('Success.TLabel', background='#f0f0f0', foreground='green')
        self.style.configure('Error.TLabel', background='#f0f0f0', foreground='red')
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Header
        header = ttk.Label(main_frame, 
                          text="Django Database Connection Troubleshooter", 
                          style='Header.TLabel',
                          padding=(10, 10))
        header.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="ew")
        
        # Connection details frame
        conn_frame = ttk.LabelFrame(main_frame, text="Database Connection Details", padding="10")
        conn_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 15))
        
        # Host
        ttk.Label(conn_frame, text="Host:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.host_var = tk.StringVar(value="PoojaKumari.mysql.pythonanywhere-services.com")
        ttk.Entry(conn_frame, textvariable=self.host_var, width=40).grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # User
        ttk.Label(conn_frame, text="User:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.user_var = tk.StringVar(value="PoojaKumari")
        ttk.Entry(conn_frame, textvariable=self.user_var, width=40).grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Password
        ttk.Label(conn_frame, text="Password:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.password_var = tk.StringVar(value="MySql@12345")
        ttk.Entry(conn_frame, textvariable=self.password_var, show="*", width=40).grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Database
        ttk.Label(conn_frame, text="Database:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.database_var = tk.StringVar(value="PoojaKumari$default")
        ttk.Entry(conn_frame, textvariable=self.database_var, width=40).grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Port
        ttk.Label(conn_frame, text="Port:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.port_var = tk.StringVar(value="3306")
        ttk.Entry(conn_frame, textvariable=self.port_var, width=40).grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Test buttons frame
        test_button_frame = ttk.Frame(conn_frame)
        test_button_frame.grid(row=5, column=0, columnspan=2, pady=10)
        
        ttk.Button(test_button_frame, text="Test MySQL Connection", command=self.test_mysql_connection).pack(side=tk.LEFT, padx=5)
        ttk.Button(test_button_frame, text="Test Django Connection", command=self.test_django_connection).pack(side=tk.LEFT, padx=5)
        
        # Error diagnosis frame
        error_frame = ttk.LabelFrame(main_frame, text="Error Diagnosis & Solutions", padding="10")
        error_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 15))
        
        error_text = """
        🔍 Error Diagnosis: (1044, "Access denied for user 'PoojaKumari'@'%' to database 'PoojaKumari'")
        
        This error typically means:
        1. The database 'PoojaKumari$default' doesn't exist
        2. The user 'PoojaKumari' doesn't have privileges to access the database
        3. The user exists but hasn't been granted permissions on this specific database
        
        ✅ Possible Solutions:
        1. Check if the database exists in your PythonAnywhere MySQL console
        2. Grant privileges to your user on the database:
           GRANT ALL PRIVILEGES ON PoojaKumari$default.* TO 'PoojaKumari'@'%';
        3. Flush privileges:
           FLUSH PRIVILEGES;
        4. Make sure you're using the correct database name format (username$default)
        
        📝 PythonAnywhere Specific Notes:
        - Free accounts can only connect from within PythonAnywhere
        - Database name should be in the format: username$default
        - Check your database name in the PythonAnywhere Databases tab
        """
        
        error_display = scrolledtext.ScrolledText(error_frame, height=12, width=90, font=('Consolas', 9))
        error_display.insert(tk.END, error_text)
        error_display.config(state=tk.DISABLED)
        error_display.grid(row=0, column=0, sticky="nsew")
        
        # Output frame
        output_frame = ttk.LabelFrame(main_frame, text="Connection Test Results", padding="10")
        output_frame.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=(0, 15))
        
        self.output_text = scrolledtext.ScrolledText(output_frame, height=15, width=90, font=('Consolas', 10))
        self.output_text.grid(row=0, column=0, sticky="nsew")
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready to test connections")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
        conn_frame.columnconfigure(1, weight=1)
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        error_frame.columnconfigure(0, weight=1)
        error_frame.rowconfigure(0, weight=1)
        
    def test_mysql_connection(self):
        """Test direct MySQL connection"""
        host = self.host_var.get()
        user = self.user_var.get()
        password = self.password_var.get()
        database = self.database_var.get()
        port = self.port_var.get()
        
        self.output_text.delete(1.0, tk.END)
        self.status_var.set("Testing MySQL connection...")
        self.root.update()
        
        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=int(port)
            )
            
            if connection.is_connected():
                db_info = connection.get_server_info()
                cursor = connection.cursor()
                cursor.execute("SELECT DATABASE()")
                db_name = cursor.fetchone()[0]
                
                result = f"✅ MySQL connection successful!\n"
                result += f"   Server Version: {db_info}\n"
                result += f"   Current Database: {db_name if db_name else 'None'}\n\n"
                
                # Show databases available to the user
                cursor.execute("SHOW DATABASES;")
                databases = cursor.fetchall()
                result += "Available databases:\n"
                for db in databases:
                    result += f"   - {db[0]}\n"
                    
                self.output_text.insert(tk.END, result)
                self.status_var.set("MySQL connection successful!")
                
                cursor.close()
                connection.close()
                
        except Error as e:
            error_msg = f"❌ MySQL connection failed:\n{str(e)}\n\n"
            
            # Add specific troubleshooting tips based on error code
            if "1044" in str(e):
                error_msg += "🔧 Troubleshooting:\n"
                error_msg += "1. Check if the database exists\n"
                error_msg += "2. Verify user has privileges on the database\n"
                error_msg += "3. On PythonAnywhere, database name should be username$default\n"
            elif "1045" in str(e):
                error_msg += "🔧 Troubleshooting:\n"
                error_msg += "1. Check your username and password\n"
                error_msg += "2. Verify the user exists in MySQL\n"
            elif "2003" in str(e):
                error_msg += "🔧 Troubleshooting:\n"
                error_msg += "1. Check the host address\n"
                error_msg += "2. Verify MySQL server is running\n"
                error_msg += "3. Check if the port is correct\n"
                
            self.output_text.insert(tk.END, error_msg)
            self.status_var.set("MySQL connection failed!")
    
    def test_django_connection(self):
        """Test Django database connection"""
        self.output_text.delete(1.0, tk.END)
        self.status_var.set("Testing Django database connection...")
        self.root.update()
        
        try:
            # Set environment variables for the test
            env = os.environ.copy()
            
            # Run a simple Django check command
            result = subprocess.run([
                sys.executable, 'manage.py', 'check', '--database', 'default'
            ], capture_output=True, text=True, cwd=os.getcwd(), env=env)
            
            if result.returncode == 0:
                self.output_text.insert(tk.END, f"✅ Django database connection successful!\n\n")
                self.output_text.insert(tk.END, result.stdout)
                self.status_var.set("Django connection successful!")
            else:
                self.output_text.insert(tk.END, f"❌ Django database connection failed:\n\n")
                self.output_text.insert(tk.END, result.stderr)
                self.status_var.set("Django connection failed!")
                
        except Exception as e:
            self.output_text.insert(tk.END, f"Error testing Django connection: {str(e)}")
            self.status_var.set("Django connection test error")

if __name__ == "__main__":
    root = tk.Tk()
    app = DjangoDBTroubleshooter(root)
    root.mainloop()