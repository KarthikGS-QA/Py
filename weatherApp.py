import requests
import tkinter as tk

api_key="576ccf72619666442f4bcae474dbc803"
# temp=""
# humidity=""
# Pressure=""

def fetchInfo():
    # cityName=input("Enter a city Name :  \n")

    cityName=t1.get()

    url=f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={api_key}"

    resp=requests.get(url)


    # print(resp.json())
    # print(f"response = {resp}")

    if resp.status_code==200:
        result=resp.json()
        # print(result)

        x=result['main']
        temp=str(x['temp']-273)
        humidity=str(x['humidity'])
        Pressure=str(x['pressure'])

        msg=f"Temparature : {x['temp']-276}\nHumidity  : {x['humidity']}\nPressure  :{x['pressure']}"
        print(f"\n---------------Weather info of city  {cityName} is ----------------")
        print(msg)
        textTemp.delete(0, tk.END)
        textTemp.insert(0, temp)

        textPressure.delete(0, tk.END)
        textPressure.insert(0, Pressure)
        

        textHumidity.delete(0, tk.END)
        textHumidity.insert(0, humidity)

    else:
        print(f"Sorry city name {cityName} is wrong !")
        msg=f"Sorry city name {cityName} is wrong !"
        textTemp.delete(0, tk.END)
        textPressure.delete(0, tk.END)
        textHumidity.delete(0, tk.END)
        lblResult.config(text=msg, fg ="red", font=('calibri',15))
    


window =tk.Tk()

window.title("Weather Info App")
window.geometry('500x400')

lbl=tk.Label(window,text="Enter a city name : ",fg ="blue")
lbl.place(x=100,y=50)

t1=tk.Entry(window)
t1.place(x=230,y=50)


btn=tk.Button(window,text="Fetch Weather Info ",command=fetchInfo)
btn.place(x=200,y=100)

lblResult=tk.Label(window)
lblResult.place(x=200,y=350)

lblTemp=tk.Label(window,text="Temparature : ")
lblTemp.place(x=100,y=200)

textTemp=tk.Entry(window)
textTemp.place(x=200,y=200)

lblPressure=tk.Label(window,text="Pressure : ")
lblPressure.place(x=100,y=250)

textPressure=tk.Entry(window)
textPressure.place(x=200,y=250)

lblHumidity=tk.Label(window,text="Humidity : ")
lblHumidity.place(x=100,y=300)

textHumidity=tk.Entry(window)
textHumidity.place(x=200,y=300)

window.mainloop()