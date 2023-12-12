import customtkinter as ctk
import datetime
import tkinter.messagebox
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
import time

download_url = 'https://www.tukui.org/elvui'

def update_progress_bar(progress_bar, progress_window):
    progress_bar.set(0)
    for _ in range(10):
        progress_bar.set(progress_bar.get() + 10)
        time.sleep(1)
    progress_bar.set(100)
    tkinter.messagebox.showinfo("Information", "Download abgeschlossen.", parent=progress_window)

def download_file_with_selenium(download_url, progress_bar, progress_window):
    path_to_geckodriver = 'C:/temp/geckodriver.exe'
    options = FirefoxOptions()
    options.add_argument("--headless")
    service = Service(executable_path=path_to_geckodriver)
    driver = webdriver.Firefox(service=service, options=options)

    driver.get(download_url)
    time.sleep(3)

    try:
        download_button = driver.find_element(By.ID, "download-button")
        download_button.click()

        progress_thread = threading.Thread(target=update_progress_bar, args=(progress_bar, progress_window))
        progress_thread.start()
        time.sleep(10)
    finally:
        driver.quit()

def start_download_thread(progress_bar, progress_window):
    download_thread = threading.Thread(target=download_file_with_selenium, args=(download_url, progress_bar, progress_window))
    download_thread.start()

def dummy_function():
    tkinter.messagebox.showinfo("Information", "Diese Funktion wird noch implementiert.")
    
def get_current_date():
    return datetime.datetime.now().strftime("%d.%m.%Y")

def get_elvui_version():
    return "Version 1.0"  # Dummy-Daten

def get_last_backup_date():
    return "01.01.2023"  # Dummy-Daten

def get_oldest_backup_date():
    return "01.01.2022"  # Dummy-Daten

def open_progress_window():
    progress_window = ctk.CTkToplevel(root)
    progress_window.title("Download-Fortschritt")
    progress_window.geometry("300x100")

    progress_bar = ctk.CTkProgressBar(progress_window, width=200)
    progress_bar.pack(pady=20)

    start_download_thread(progress_bar, progress_window)

root = ctk.CTk()
root.title("WoW Backup & ElvUI Management Tool")
root.geometry("400x300")

info_frame = ctk.CTkFrame(root)
info_frame.pack(padx=10, pady=10, fill="x", expand=True)

label_current_date_text = ctk.CTkLabel(info_frame, text="Aktuelles Datum: ")
label_current_date_text.grid(row=0, column=0, sticky="w")
label_current_date = ctk.CTkLabel(info_frame, text=get_current_date())
label_current_date.grid(row=0, column=1, sticky="w")

label_elvui_version_text = ctk.CTkLabel(info_frame, text="Aktuelle ElvUI Version: ")
label_elvui_version_text.grid(row=1, column=0, sticky="w")
label_elvui_version = ctk.CTkLabel(info_frame, text=get_elvui_version())
label_elvui_version.grid(row=1, column=1, sticky="w")

label_last_backup_text = ctk.CTkLabel(info_frame, text="Datum des letzten Backups: ")
label_last_backup_text.grid(row=2, column=0, sticky="w")
label_last_backup = ctk.CTkLabel(info_frame, text=get_last_backup_date())
label_last_backup.grid(row=2, column=1, sticky="w")

label_oldest_backup_text = ctk.CTkLabel(info_frame, text="Datum des ältesten vorhandenen Backups: ")
label_oldest_backup_text.grid(row=3, column=0, sticky="w")
label_oldest_backup = ctk.CTkLabel(info_frame, text=get_oldest_backup_date())
label_oldest_backup.grid(row=3, column=1, sticky="w")

button_frame = ctk.CTkFrame(root)
button_frame.pack(padx=10, pady=10, fill="x", expand=True)

button_create_backup = ctk.CTkButton(button_frame, text="Backup erstellen", command=dummy_function)
button_create_backup.pack(fill="x", pady=5)

button_read_config = ctk.CTkButton(button_frame, text="Aktuelle Konfiguration auslesen", command=dummy_function)
button_read_config.pack(fill="x", pady=5)

button_update_elvui = ctk.CTkButton(button_frame, text="ElvUI aktualisieren", command=open_progress_window)
button_update_elvui.pack(fill="x", pady=5)

button_install_cronjob = ctk.CTkButton(button_frame, text="Windows-CronJob installieren", command=dummy_function)
button_install_cronjob.pack(fill="x", pady=5)

button_update_config = ctk.CTkButton(button_frame, text="Konfiguration aktualisieren", command=dummy_function)
button_update_config.pack(fill="x", pady=5)

root.mainloop()
