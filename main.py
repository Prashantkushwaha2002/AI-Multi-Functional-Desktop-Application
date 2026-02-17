import tkinter as tk
from tkinter import messagebox
from video_module import start_camera
from web_module import open_youtube, open_netflix, open_hotstar, search_google
from voice_module import listen_command
from aws_module import start_ec2
from ai_module import search_web

def handle_search():
    query = search_entry.get()
    search_google(query)

def handle_ai_search():
    query = search_entry.get()
    result = search_web(query)
    messagebox.showinfo("AI Result", result[:500])

def handle_voice():
    command = listen_command()

    if "youtube" in command:
        open_youtube()
    elif "camera" in command:
        start_camera()
    else:
        messagebox.showinfo("Voice Command", command)

def handle_aws():
    result = start_ec2()
    messagebox.showinfo("AWS", result)

root = tk.Tk()
root.title("AI Multi-Functional Application")
root.geometry("550x600")

tk.Label(root, text="AI Multi-Functional Desktop App", font=("Arial", 16)).pack(pady=15)

tk.Button(root, text="Start Camera + Face Detection", command=start_camera).pack(pady=10)
tk.Button(root, text="Start EC2 Instance", command=handle_aws).pack(pady=10)
tk.Button(root, text="Voice Assistant", command=handle_voice).pack(pady=10)

tk.Label(root, text="Search Section").pack(pady=5)
search_entry = tk.Entry(root, width=40)
search_entry.pack(pady=5)

tk.Button(root, text="Google Search", command=handle_search).pack(pady=5)
tk.Button(root, text="AI Web Search", command=handle_ai_search).pack(pady=5)

tk.Label(root, text="Streaming Platforms").pack(pady=10)
tk.Button(root, text="YouTube", command=open_youtube).pack(pady=5)
tk.Button(root, text="Netflix", command=open_netflix).pack(pady=5)
tk.Button(root, text="Hotstar", command=open_hotstar).pack(pady=5)

root.mainloop()
