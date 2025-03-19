import os
import time
import threading
import pygetwindow as gw
import web_dict

def arrange_linkedin_overleaf():
    os.system(f'start chrome --new-window {web_dict["LinkedIn"]} --new-tab {web_dict["Handshake"]} --new-tab {web_dict["Overleaf"]}')
    time.sleep(1)  # Allow time for the window to open
    window = next((w for w in gw.getAllWindows() if "LinkedIn" in w.title or "Overleaf" in w.title), None)
    if window:
        window.restore()  # Unmaximize if needed
        time.sleep(0.5)
        window.moveTo(0, 0)
        window.resizeTo(2560, 1440)
    else:
        print("Could not find LinkedIn/Overleaf window.")

def arrange_chatgpt():
    os.system(f'start chrome --new-window {web_dict["ChatGPT"]}')
    time.sleep(2)
    window = next((w for w in gw.getAllWindows() if "ChatGPT" in w.title), None)
    if window:
        window.restore()
        # time.sleep(0.5)
        window.moveTo(2560, 0)  # Second display starts at x=2560
        window.resizeTo(1280, 1440)
    else:
        print("Could not find ChatGPT window.")

def arrange_notion():
    os.system(f'start chrome --new-window {web_dict["Notion"]}')
    time.sleep(4)
    # Debug print: list window titles to verify detection
    all_titles = [w.title for w in gw.getAllWindows()]
    print("Window Titles:", all_titles)
    window = next((w for w in gw.getAllWindows() if "Rishikesh Applications" in w.title), None)
    if window:
        window.restore()
        time.sleep(0.5)
        window.moveTo(2560 + 1280, 0)  # Top-right half on second display
        window.resizeTo(1280, 720)
    else:
        print("Could not find Notion window.")

def arrange_youtube():
    os.system(f'start chrome --new-window {web_dict["Youtube"]}')
    time.sleep(1)
    window = next((w for w in gw.getAllWindows() if "YouTube" in w.title), None)
    if window:
        window.restore()
        window.moveTo(2560 + 1280, 720)  # Bottom-right half on second display
        window.resizeTo(1280, 720)
    else:
        print("Could not find YouTube window.")

def main():
    threads = []
    threads.append(threading.Thread(target=arrange_linkedin_overleaf))  # Create a thread for arranging LinkedIn and Overleaf
    threads.append(threading.Thread(target=arrange_chatgpt))  # Create a thread for arranging ChatGPT
    threads.append(threading.Thread(target=arrange_notion))  # Create a thread for arranging Notion
    threads.append(threading.Thread(target=arrange_youtube))  # Create a thread for arranging YouTube

    for t in threads:
        t.start()  # Start each thread
    for t in threads:
        t.join()  # Wait for all threads to complete
    print("All windows arranged.")

if __name__ == "__main__":
    main()

