from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.label import Label
import requests
import json
postAPIUrl='https://api-cl2e.onrender.com/api/changeLight'
entryData=requests.get('https://api-cl2e.onrender.com/api/getLights')
response=entryData.json()
print(response)
lightState1=response[0]['state']
lightState2=response[1]['state']
lightState3=response[2]['state']
lightState4=response[3]['value']
print(lightState1)
print(lightState2)
print(lightState3)
if(lightState1):
    lightState1Text="Açık"
else:
    lightState1Text="Kapalı"
if(lightState2):
    lightState2Text="Açık"
else:
    lightState2Text="Kapalı"
if(lightState3):
    lightState3Text="Açık"
else:
    lightState3Text="Kapalı"

class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)
        def changeLightState1(self):
            global lightState1
            global lightState1Text
            data = {
                "lightID": 1,
                "state": not lightState1
            }
            lightState1=not lightState1
            headers = {"Content-Type": "application/json"}
            response = requests.post(postAPIUrl, headers=headers, data=json.dumps(data))
            print(response.json())
            if(lightState1):
                lightState1Text="1 Açık"
            else:
                lightState1Text="1 Kapalı"
            L1.text=lightState1Text
        def changeLightState2(self):
            global lightState2
            global lightState2Text
            data = {
                "lightID": 2,
                "state": not lightState2
            }
            lightState2=not lightState2
            headers = {"Content-Type": "application/json"}
            response = requests.post(postAPIUrl, headers=headers, data=json.dumps(data))
            print(response.json())
            if(lightState2):
                lightState2Text="2 Açık"
            else:
                lightState2Text="2 Kapalı"
            L2.text=lightState2Text
        def changeLightState3(self):
            global lightState3
            global lightState3Text
            data = {
                "lightID": 3,
                "state": not lightState3
            }
            lightState3=not lightState3
            headers = {"Content-Type": "application/json"}
            response = requests.post(postAPIUrl, headers=headers, data=json.dumps(data))
            print(response.json())
            if(lightState3):
                lightState3Text="3 Açık"
            else:
                lightState3Text="3 Kapalı"
            L3.text=lightState3Text
        def changeDim(self,instance):
            data ={
                "value":int(slider.value)
            }
            headers = {"Content-Type": "application/json"}
            response = requests.post('https://api-cl2e.onrender.com/api/changeAdjust',headers=headers,data=json.dumps(data))
            print(response.json())
            
        
        xd=self.remove_widget
        L1=Button(
                text='1 '+lightState1Text,
                size_hint=(.3, .3),
                pos_hint={'center_x': .3, 'center_y': .3},
                on_release=changeLightState1)
        self.add_widget(L1)
        L2=Button(
                text='2 '+lightState2Text,
                size_hint=(.3, .3),
                pos_hint={'center_x': .7, 'center_y': .7},
                on_release=changeLightState2)
        self.add_widget(L2)
        L3=Button(
                text='3 '+lightState3Text,
                size_hint=(.3, .3),
                pos_hint={'center_x': .3, 'center_y': .7},
                on_release=changeLightState3)
        self.add_widget(L3)
        slider=Slider(
            min=0, 
             max=255,
             value=lightState4,
             orientation= 'horizontal',
             pos_hint= {'center_x': 0.7,'center_y': 0.3},
             size_hint= (.3, .3),
             value_track=True, 
             value_track_color=[1, 1, 0, 1],
             on_release=changeDim)
        self.add_widget(slider)
        slider.bind(on_touch_up=changeDim)

class MainApp(App):

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            Color(0, 0, 0, 1)  # green; colors range from 0-1 not 0-255
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    MainApp().run()