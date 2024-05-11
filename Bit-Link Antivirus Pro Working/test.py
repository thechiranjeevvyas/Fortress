import tkinter as tk
from tkinter import filedialog, ttk

# Define antivirus function
def scan_folder():
    # Open a folder dialog to select a folder to scan
    folder_path = filedialog.askdirectory()
    if folder_path:
        # Perform scanning operation on the selected folder
        print("Scanning folder:", folder_path)
        # Add your antivirus logic here
        # For demonstration, let's just display the files in a Treeview
        display_files(folder_path)

def display_files(folder_path):
    # Clear previous entries from Treeview
    for item in file_tree.get_children():
        file_tree.delete(item)
    
    # Get list of files in the folder
    import os
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Insert files into Treeview
    for file in files:
        file_tree.insert('', 'end', values=(file,))

# Create the main application window
root = tk.Tk()
root.title("Antivirus")

# Configure color scheme
root.configure(bg="#f0f0f0")
root.option_add("*TButton.Background", "#4CAF50")
root.option_add("*TButton.Foreground", "#ffffff")
root.option_add("*Treeview.Background", "#ffffff")
root.option_add("*Treeview.Foreground", "#000000")

# Create a button to trigger the folder scanning function
scan_button = ttk.Button(root, text="Scan Folder", command=scan_folder)
scan_button.pack(pady=10)

# Create Treeview to display files found during scan
file_tree = ttk.Treeview(root, columns=("Files",), show="headings", height=10)
file_tree.heading("Files", text="Files Found")
file_tree.pack(padx=20, pady=5, fill="both", expand=True)

# Start the Tkinter event loop
root.mainloop()
