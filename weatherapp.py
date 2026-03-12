from tkinter import *
import requests

api_key="749096654386ca47251533fa86505d6d"

def  get_weather():
    city=city_entry.get()
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    data=requests.get(url).json()

    if data["cod"]==200:
        temp.set(data["main"]["temp"])
        pressure.set(data["main"]["pressure"])
        humidity.set(data["main"]["humidity"])
        wind.set(data["wind"]["speed"])
        cloud.set(data["clouds"]["all"])
        desc.set(data["weather"][0]["description"])
    else:
        temp.set("error")
        pressure.set("error")
        humidity.set("error")   
        wind.set("error")
        cloud.set("error")
        desc.set("city not found")

def  get_forecast():
    city=city_entry.get()
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={"city"}&appid={api_key}&units=metric"
    data=requests.get(url).json()

    forecast_text=""
    if data["cod"] == "200":
        for i in range(0,5):
            forecast_text +=f"{data['list'][i]['dt_txt']} Temp:{data['list'][i]['main']['temp']}^c\n"
        forecast_label.config(text=forecast_text)
    else:
        forecast_label.config(text="city not found")
def reset():
    city_entry.delete(0,END) 
    temp.set("")
    pressure.set("")
    humidity.set("")
    wind.set("")
    cloud.set("")
    desc.set("")
    forecast_label.config(text="")


root=Tk()
root.title("weather application")
root.geometry("400x500")
root.configure(bg="lightblue")           

temp=StringVar()            
pressure =StringVar()
humidity =StringVar()
wind =StringVar()
cloud =StringVar()
desc =StringVar()


Label(root, text="Weather Detection and Forecast",bg="lightblue",
font=("arial",14,"bold")).pack(pady=10)

Label(root,text="Enter City Name",bg="lightblue").pack()
city_entry=Entry(root,width=30)
city_entry.pack(pady=5)

Button(root,text="Get Weather",bg="green",fg="white",
command=get_weather).pack(pady=5)
Button(root,text="Weather Forecast",
bg="orange",fg="white",
command=get_forecast).pack(pady=5)

Label(root,text="Temperature",
bg="lightblue").pack()      
Entry(root, textvariable=temp).pack()

Label(root,text="pressure",
bg="lightblue").pack()
Entry(root, textvariable=pressure).pack()

Label(root,text="Humidity",
bg="lightblue").pack()      
Entry(root,textvariable=humidity).pack()

Label(root,text="wind", 
bg="lightblue").pack()
Entry(root,textvariable=wind).pack()

Label(root,text="cloudiness",
bg="lightblue").pack()
Entry(root,textvariable=wind).pack()

Label(root,text="description",
bg="lightblue").pack()
Entry(root,textvariable=desc).pack()

forecast_label=Label(root,text="",
bg="lightblue")
forecast_label.pack(pady=10)

Button(root,text="Reset",bg="red",fg="white",command=reset).pack(pady=10)

root.mainloop()




