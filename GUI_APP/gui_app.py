from kivy.app import App
import json
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

Window.size = (600, 600)


class MyApp(App):
    def build(self):
        self.title = 'Mouser Part Search App'
        self.layout = BoxLayout(orientation="vertical")
        self.result_textinput = TextInput(
            multiline=True,
            readonly=True,
            font_size=14,
            halign="left",
            height=400,
        )
        self.part_textinput = TextInput(multiline=False, size_hint=(1, 0.2))
        self.part_textinput_lable = Label(text="Enter Part Number Below", size_hint=(1, 0.2))
        self.button = Button(text="Press to search for part", height=50)
        self.button.bind(on_press=self.send_query)
        self.layout.add_widget(self.result_textinput)
        self.layout.add_widget(self.part_textinput_lable)
        self.layout.add_widget(self.part_textinput)
        self.layout.add_widget(self.button)
        return self.layout

    def clear_text_field(self):
        self.result_textinput.text = ""

    def on_request_success(self, request, result):
        if not result:
            self.result_textinput.text = "No results found"
            return
        formatted_result = json.dumps(result, indent=4)
        self.result_textinput.text = formatted_result
        self.result_textinput.cursor = (0, 0)

    def on_request_failure(self, request, result):
        self.result_textinput.text = "Failed to get response"

    def send_query(self, instance):
        part_number = self.part_textinput.text
        self.clear_text_field()
        headers = {"Content-type": "application/json"}
        params = {"query": part_number}
        UrlRequest(
            f'http://127.0.0.1:8000/search?query={params.get("query")}',  # replace with your actual server URL
            req_headers=headers,
            on_success=self.on_request_success,
            on_failure=self.on_request_failure,
            on_error=self.on_request_failure,
            method="POST",
        )


if __name__ == "__main__":
    MyApp().run()
