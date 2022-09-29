# please run the below line in command prompt to install all the libraries
# pip install SpeechRecognition pyaudio requests geopy playsound

import speech_recognition as sr
import requests
from geopy.geocoders import Nominatim
from sys import platform
from playsound import playsound as ps

def assignment1():
    r = sr.Recognizer()

    while True :

        try :
            
            with sr.Microphone() as source1:

                r.adjust_for_ambient_noise(source1, duration=0.2)  # adjust for voice

                audio1 = r.listen(source1)  # listens for user input

                audiotext = r.recognize_google(audio1)
                audiotext = audiotext.lower()

                print(audiotext)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occured")

def assignment2():
    
    geolocator = Nominatim(user_agent="geoapiExercises")

    latitude = input("Enter the latitude : ")
    longitude = input("Enter the longitude : ")

    location = geolocator.reverse(latitude+','+longitude)

    address = location.raw['address']

    print(address.get('country',''))

def assignment3():

    ip_address = requests.get('https://api.ipify.org?format=json')
    ip_address = ip_address.text
    ip_address = ip_address.replace("}","")
    ip_address = ip_address.replace("\"","")
    ip_address = ip_address.replace("{","")
    ip_address = ip_address[3:]

    location = requests.get(f"https://ipapi.co/{ip_address}/json/")
    print(location.text)

def assignment4():

    PATH = input("Enter path of the audio file : ")

    if platform == 'linux':
        ps(PATH)
    elif platform == 'darwin':
        ps(PATH)
    elif platform == 'win32':
        ps(PATH)

def assignment5():
    
    a,b,c = input("Enter length of 3 sides of triangle with space : ").split()
    a,b,c = int(a),int(b),int(c)

    if (a == b) and (a == c) :
        print("Equilateral Triangle")
    elif (b == c) or (a == b) or (a == c):
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")

def assignment6():

    user_input = input("Choose between Sides or Angles : ")
    if user_input.lower() == 'angles' :
        a,b,c = input("Enter length of 3 angles of triangle with space : ").split()
        a,b,c = int(a),int(b),int(c)

        if (a>0 and b>0 and c>0) and (a<179 and b<179 and c<179) and (a+b+c == 180):
            print("Valid Triangle")
        else:
            print("Invalid Triangle")

    elif user_input.lower() == 'sides':

        a,b,c = input("Enter measures of 3 sides of triangle with space : ").split()
        a,b,c = int(a),int(b),int(c)

        if (a+b > c) and (a+c > b) and (b+c > a):
            print("Valid Triangle")
        else:
            print("Invalid Triangle")
        
    else:
        print("Please check spelling!")

def assignment7():
    
    a,b,c = input("Enter the 3 coeifficent of the quadratic equation : ").split()
    a,b,c = int(a),int(b),int(c)

    discriminant = (b*b) - (4*a*c)

    if a != 0:

        if discriminant > 0 :
            root1 = (-b+ (discriminant**0.5))/2*a
            root2 = (-b- (discriminant**0.5))/2*a
            print("Roots are :\n",root1,"\n",root2)
        
        elif discriminant < 0 :
            print("Roots are :\n",-b/(2*a),'+i (',discriminant,')\n',-b/(2*a),"-i (",discriminant,")")

        else:
            print("Root is :\n",-b/(2*a))
    
    else:
        print("Invalid Equation")

def assignment8():
    
    no = int(input("Enter the number (int values only) : "))

    MSB = (no>0)-(no<0)

    if MSB > 0 :
        print("Positive")
    elif MSB < 0 :
        print("Negative")
    else:
        print("Zero")

def assignment9():

    user_input = int(input("Enter number to check odd or even : "))

    bit_number = int(bin(user_input)[2:])

    if bit_number & 1:
        print("Odd")
    else:
        print("Even")


# run the function with respective name 
assignment9()