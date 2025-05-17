import requests
import tkinter as tk
from tkinter import messagebox
import random

def get_weather():
    city = city_entry.get()
    API_KEY = "0c3d23bd272f32954cd9805561826976"

    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    try:
        geo_response = requests.get(geo_url).json()
        if not geo_response:
            messagebox.showerror("Oops!", "City not found. Try 'City,CountryCode' (e.g., Ajman,AE)")
            return

        lat, lon = geo_response[0]['lat'], geo_response[0]['lon']

        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        weather_response = requests.get(weather_url).json()

        temp_label.config(text=f"🌡️ Temp: {weather_response['main']['temp']}°C")
        pressure_label.config(text=f"🔵 Pressure: {weather_response['main']['pressure']} hPa")
        humidity_label.config(text=f"💧 Humidity: {weather_response['main']['humidity']}%")
        wind_label.config(text=f"🌬️ Wind: {weather_response['wind']['speed']} m/s")
        desc_label.config(text=f"🌌 Sky: {weather_response['weather'][0]['description'].title()}")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch data: {str(e)}")

def draw_stars(canvas, num_stars=80):
    for _ in range(num_stars):
        x = random.randint(0, 420)
        y = random.randint(0, 500)
        r = random.randint(1, 2)
        canvas.create_oval(x, y, x + r, y + r, fill="white", outline="white")

# Create root window
root = tk.Tk()
root.title("☄️ Space Weather")
root.geometry("420x500")
root.resizable(False, False)

# Starfield background using Canvas
canvas = tk.Canvas(root, width=420, height=500, bg="black", highlightthickness=0)
canvas.place(x=0, y=0)
draw_stars(canvas)

# Overlay UI Frame (transparent-like feel)
frame = tk.Frame(root, bg="#000000", highlightbackground="white", highlightthickness=1)
frame.place(relx=0.5, rely=0.5, anchor="center", width=360, height=420)

# Fonts and colors
FONT_TITLE = ("Courier New", 16, "bold")
FONT_MAIN = ("Courier New", 12)
FONT_LABEL = ("Courier New", 11)
WHITE = "white"
BLACK = "black"

# Title
tk.Label(frame, text="🪐 Weather In Space", font=FONT_TITLE, bg=BLACK, fg=WHITE).pack(pady=(20, 10))

# City entry
city_entry = tk.Entry(frame, font=FONT_MAIN, bg=BLACK, fg=WHITE,
                      insertbackground="white", justify="center",
                      relief="flat", highlightthickness=1, highlightbackground="white", width=25)
city_entry.pack(pady=10, ipady=6)

# Button
search_btn = tk.Button(frame, text="Locate Weather", font=FONT_MAIN,
                       bg=BLACK, fg=WHITE, activebackground="#222", activeforeground="white",
                       relief="ridge", borderwidth=1, command=get_weather, cursor="hand2", width=18)
search_btn.pack(pady=10, ipady=4)

# Weather info labels
temp_label = tk.Label(frame, text="🌡️ Temp: --", font=FONT_LABEL, bg=BLACK, fg=WHITE)
pressure_label = tk.Label(frame, text="🔵 Pressure: --", font=FONT_LABEL, bg=BLACK, fg=WHITE)
humidity_label = tk.Label(frame, text="💧 Humidity: --", font=FONT_LABEL, bg=BLACK, fg=WHITE)
wind_label = tk.Label(frame, text="🌬️ Wind: --", font=FONT_LABEL, bg=BLACK, fg=WHITE)
desc_label = tk.Label(frame, text="🌌 Sky: --", font=FONT_LABEL, bg=BLACK, fg=WHITE)

for lbl in [temp_label, pressure_label, humidity_label, wind_label, desc_label]:
    lbl.pack(pady=3)

# Footer
tk.Label(frame, text="by ibrvhi✦", font=("Courier New", 9), bg=BLACK, fg="#aaaaaa").pack(side="bottom", pady=8)

root.mainloop()
