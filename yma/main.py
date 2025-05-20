from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import datetime

class NotesApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.note_input = TextInput(hint_text="اكتب مذكرتك هنا", multiline=True, size_hint=(1, 0.8))
        self.layout.add_widget(self.note_input)
        save_button = Button(text="حفظ الملاحظة", size_hint=(1, 0.2))
        save_button.bind(on_press=self.save_note)
        self.layout.add_widget(save_button)
        return self.layout

    def save_note(self, instance):
        note = self.note_input.text.strip()
        if note:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("notes.txt", "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] {note}\n\n")
            self.note_input.text = ""

if __name__ == '__main__':
    NotesApp().run()
