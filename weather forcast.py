import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests

def getting_API(lat, long):
    access_key = '262b3c444b5f430193fe33f7164c0874'
    url = f'https://api.weatherbit.io/v2.0/current?lat={lat}&lon={long}&key={access_key}&include=minutely'
    r = requests.get(url)

    if r.status_code == 200:
        info = r.json()
        data = info.get('data')
        #print(data)
        return data
    else:
        return None

def fetch_weather():
    lat = lat_entry.get()
    long = long_entry.get()

    try:
        lat = float(lat)
        long = float(long)
    except ValueError:
        messagebox.showwarning(title='Invalid entry' ,message="Latitude and Longitude must be numeric values")

        return

    if -90 <= lat <= 90 and -180 <= long <= 180:
        data = getting_API(lat, long)
        if data:
            for all_data in data:
                temp = all_data.get('app_temp')
                wind_speed = all_data.get('wind_spd')
                wind_direction = all_data.get('wind_cdir_full')
                city = all_data.get('city_name')
                weather_condition=all_data['weather']['description']
            # Update the existing label with weather info
            weather_label.config(text=f'CITY NAME: {city}\n\nTEMPERATURE: {temp} °C\n\nWIND SPEED: {wind_speed} m/s\n\nWIND DIRECTION: {wind_direction}\n\nWEATHER CONDITION: {weather_condition}')

        else:
            messagebox.showerror(title='Error', message='50 searches per day limit reached...\nTry again next day')

    else:
        messagebox.showwarning(title='Invalid values' ,message="Latitude must be in the range [-90, 90]\nLongitude must be in the range [-180, 180]")

# Create tkinter window
window = tk.Tk()
window.title("Weather App")
window.geometry('280x300+300+150')
window.iconbitmap('icon.ico')
window.resizable(False,False)

#background_image
img=Image.open('cloud.jpg')
bg_img=ImageTk.PhotoImage(img)

#background image label
bg_lab=tk.Label(window, image=bg_img)
bg_lab.place(relheight=1 , relwidth=1)

# Create labels
lat_label = tk.Label(window, text="Enter Latitude:" ,font='Arial 12 ' , bg='#6897bb' , fg='white' , relief='ridge' , borderwidth=3 , justify='left')
lat_label.grid(row=0, column=0, padx=10, pady=5 , sticky='w')

long_label = tk.Label(window, text="Enter Longitude:",font='Calibiri 12 ' , bg='#6897bb' , fg='white'  , relief='ridge',borderwidth=3)
long_label.grid(row=1, column=0, padx=10, pady=5 , sticky='w')

# Create entry fields
lat_entry = tk.Entry(window)
lat_entry.grid(row=0, column=1, padx=10, pady=5 , sticky='ew')

long_entry = tk.Entry(window)
long_entry.grid(row=1, column=1, padx=10, pady=5 , sticky='ew')

# Create fetch weather button
fetch_button = tk.Button(window, text="Fetch Weather", command=fetch_weather, font='timesnewroman 10 bold' , bg='#003366' , fg='white' , relief='raised', borderwidth=5)
fetch_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Create an empty label for displaying weather info
weather_label = tk.Label(window, text='', wraplength=250, justify="left", font='timesnewroman 10 bold', bg='#6897bb', fg='white', relief='sunken', borderwidth=4)
weather_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky='w')

# Run the tkinter event loop
window.mainloop()
