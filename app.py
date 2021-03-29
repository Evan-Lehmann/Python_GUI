


import tkinter as tk
from tkinter import *
import requests
import json
import urllib.request 
from PIL import Image, ImageTk
import tkinter.font as font
import pkg_resources.py2_warn



root = Tk()
root.title("City Info")
root.geometry("1500x900")
root.configure(bg="white",)
root.minsize(width=1500, height=900)
root.maxsize(width=1500, height=900)
root.iconbitmap(default='icon.ico')

img7 = Image.open("bg.png")  # PIL solution
img7 = img7.resize((1500, 900), Image.ANTIALIAS) #The (250, 250) is (height, width)
img7 = ImageTk.PhotoImage(img7) # convert to PhotoImage
#image = C.create_image(1500,0, anchor = NE, image = img)

label = Label(root, image=img7)
label.place(relwidth=1, relheight=1, anchor='nw')




def format_response(city_json):
    
    

    try:
        city = city_json['records'][0]['fields']['name']
        state = city_json['records'][0]['fields']['admin1_code']
        country = city_json['records'][0]['fields']['country']
        pop = city_json['records'][0]['fields']['population']
        lt = city_json['records'][0]['fields']['latitude']
        lg = city_json['records'][0]['fields']['longitude']


        if city_json['records'][0]['fields']['country'] == "United States":
  
            final_str = 'City: %s -\nState: %s \nCountry: %s \nPopulation: %s \nLatitude: %s \nLongitude %s ' % (city, state, country, pop, lt, lg)
    
        else: 
             final_str = 'City: %s -\nCountry: %s \nPopulation: %s \nLatitude: %s \nLongitude: %s' % (city, country, pop, lt, lg)
  
    except:
        final_str = 'Sorry, we could not find that city.'
    #final_str = 'hello'
    return final_str


def format_response2(city_json):
    
    

    try:
        city = city_json['records'][0]['fields']['name']
        state = city_json['records'][0]['fields']['admin1_code']
        country = city_json['records'][0]['fields']['country']
        pop = city_json['records'][0]['fields']['population']
        lt = city_json['records'][0]['fields']['latitude']
        lg = city_json['records'][0]['fields']['longitude']


        if city_json['records'][0]['fields']['country'] == "United States":
  
            final_str = '       State: %s \nCountry: %s \nPopulation: %s \nLatitude: %s \nLongitude %s ' % (state, country, pop, lt, lg)
    
        else: 
             final_str = '      Country: %s \nPopulation: %s \nLatitude: %s \nLongitude: %s' % (country, pop, lt, lg)
  
    except:
        final_str = ''
    #final_str = 'hello'
    return final_str


def format_response3(city_json):
    
    

    try:
        city = city_json['records'][0]['fields']['name']
        state = city_json['records'][0]['fields']['admin1_code']
        country = city_json['records'][0]['fields']['country']
        pop = city_json['records'][0]['fields']['population']
        lt = city_json['records'][0]['fields']['latitude']
        lg = city_json['records'][0]['fields']['longitude']


        if city_json['records'][0]['fields']['country'] == "United States":
  
            final_str = '       Country: %s \nPopulation: %s \nLatitude: %s \nLongitude %s ' % (country, pop, lt, lg)
    
        else: 
             final_str = '      Population: %s \nLatitude: %s \nLongitude: %s' % (pop, lt, lg)
  
    except:
        final_str = ''
    #final_str = 'hello'
    return final_str




def format_response4(city_json):
    
    

    try:
        city = city_json['records'][0]['fields']['name']
        state = city_json['records'][0]['fields']['admin1_code']
        country = city_json['records'][0]['fields']['country']
        pop = city_json['records'][0]['fields']['population']
        lt = city_json['records'][0]['fields']['latitude']
        lg = city_json['records'][0]['fields']['longitude']


        if city_json['records'][0]['fields']['country'] == "United States":
  
            final_str = '       Population: %s \nLatitude: %s \nLongitude %s ' % (pop, lt, lg)
    
        else: 
             final_str = '      Latitude: %s \nLongitude: %s' % (lt, lg)
  
    except:
        final_str = ''
    #final_str = 'hello'
    return final_str



def format_response5(city_json):
    
    

    try:
        city = city_json['records'][0]['fields']['name']
        state = city_json['records'][0]['fields']['admin1_code']
        country = city_json['records'][0]['fields']['country']
        pop = city_json['records'][0]['fields']['population']
        lt = city_json['records'][0]['fields']['latitude']
        lg = city_json['records'][0]['fields']['longitude']


        if city_json['records'][0]['fields']['country'] == "United States":
  
            final_str = '       Latitude: %s \nLongitude %s ' % (lt, lg)
    
        else: 
             final_str = '      Longitude: %s' % (lg)
  
    except:
        final_str = ''
    #final_str = 'hello'
    return final_str





def format_response6(city_json):
    
    

    try:
        city = city_json['records'][0]['fields']['name']
        state = city_json['records'][0]['fields']['admin1_code']
        country = city_json['records'][0]['fields']['country']
        pop = city_json['records'][0]['fields']['population']
        lt = city_json['records'][0]['fields']['latitude']
        lg = city_json['records'][0]['fields']['longitude']


        if city_json['records'][0]['fields']['country'] == "United States":
  
            final_str = '       Longitude: %s ' % (lg)
    
        else: 
             final_str = ''
  
    except:
        final_str = ''
    #final_str = 'hello'
    return final_str


def get_pop(city):
    city_key = '4eef031b14489ddb6612553f7e7e6d2d415581b3'
    url = 'https://public.opendatasoft.com/api/records/1.0/search/?dataset=geonames-all-cities-with-a-population-1000&q=&sort=population&facet=timezone&facet=country'
    params = {'APPID': city_key, 'q': city}
    response = requests.get(url, params=params)
    city = response.json()  
    label1['text'] = format_response(city)
    l2['text'] = format_response2(city)
    l3['text'] = format_response3(city)
    l4['text'] = format_response4(city)
    l5['text'] = format_response5(city)
    l6['text'] = format_response6(city)





def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection


image = Image.open('bg.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)



  
label = tk.Label(label, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)



font2 = font.Font(family='Mulish', size=14)

entry = Entry(label, font=font2,  borderwidth=0, fg='gray15')
entry.place(relwidth=0.3, relheight=0.035, relx=0.03475, rely=0.15575,) 
entry.bind('<Return>', (lambda event: get_pop(entry.get()))) 

img = Image.open("search.png")
img = img.resize((36, 33), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)

button = Button(label, borderwidth=0, image=photo, command=lambda: get_pop(entry.get()))# command=lambda:on_button(self.entry.get()))
button.place(relwidth= 0.0225, relheight=0.0397, rely=0.1525, relx=0.334)

font1 = font.Font(family='Mulish', size=21,)




label1 = Label(label, font=font1, bg='white', fg='grey15', anchor='nw', justify='left',)
label1.place(relx=0.2625, rely=0.352575, relwidth=0.475, relheight=0.5075/12,)

l2 = Label(label, font=font1, bg='white', fg='grey15', anchor='nw', justify='left',)
l2.place(relx=0.2625, rely=0.399575, relwidth=0.475, relheight=0.5075/12,)

l3 = Label(label, font=font1, bg='white', fg='grey15', anchor='nw', justify='left',)
l3.place(relx=0.2625, rely=0.446575, relwidth=0.475, relheight=0.5075/12,)

l4 = Label(label, font=font1, bg='white', fg='grey15', anchor='nw', justify='left',)
l4.place(relx=0.2625, rely=0.493575, relwidth=0.475, relheight=0.5075/12,)


l5 = Label(label, font=font1, bg='white', fg='grey15', anchor='nw', justify='left',)
l5.place(relx=0.2625, rely=0.540575, relwidth=0.475, relheight=0.5075/12,)

l6 = Label(label, font=font1, bg='white', fg='grey15', anchor='nw', justify='left',)
l6.place(relx=0.2625, rely=0.587575, relwidth=0.475, relheight=0.5075/12,)


root.mainloop() 
