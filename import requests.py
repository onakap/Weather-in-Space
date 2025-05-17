import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = city_entry.get() 
    API_KEY = "0c3d23bd272f32954cd9805561826976"
    
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    try:
        geo_response = requests.get(geo_url).json()
        if not geo_response:
            messagebox.showerror("Error", "City not found. Try 'City,CountryCode' (e.g., Ajman,AE)")
            return
        
        lat, lon = geo_response[0]['lat'], geo_response[0]['lon']
        
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        weather_response = requests.get(weather_url).json()
        
        temp_label.config(text=f"Temperature: {weather_response['main']['temp']}°C")
        pressure_label.config(text=f"Pressure: {weather_response['main']['pressure']} hPa")
        humidity_label.config(text=f"Humidity: {weather_response['main']['humidity']}%")
        wind_label.config(text=f"Wind Speed: {weather_response['wind']['speed']} m/s")
        desc_label.config(text=f"Description: {weather_response['weather'][0]['description'].title()}")
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch data: {str(e)}")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.configure(bg='#f0f0f0')

tk.Label(root, text="Enter City:", font=('Arial', 12), bg='#f0f0f0').pack(pady=10)
city_entry = tk.Entry(root, font=('Arial', 12), width=20)
city_entry.pack()
search_btn = tk.Button(root, text="Get Weather", command=get_weather, bg='#4CAF50', fg='white')
search_btn.pack(pady=10)

temp_label = tk.Label(root, text="Temperature: --", font=('Arial', 10), bg='#f0f0f0')
temp_label.pack()
pressure_label = tk.Label(root, text="Pressure: --", font=('Arial', 10), bg='#f0f0f0')
pressure_label.pack()
humidity_label = tk.Label(root, text="Humidity: --", font=('Arial', 10), bg='#f0f0f0')
humidity_label.pack()
wind_label = tk.Label(root, text="Wind Speed: --", font=('Arial', 10), bg='#f0f0f0')
wind_label.pack()
desc_label = tk.Label(root, text="Description: --", font=('Arial', 10), bg='#f0f0f0')
desc_label.pack()

root.mainloop()