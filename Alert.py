from winotify import Notification, audio
def Alert(Text):
    icon_path = r"\logo.png"

    toast = Notification(
        app_id="🟢 J.A.R.V.I.S.",
        title=Text,
        duration="short",
        icon=icon_path
    )

    toast.set_audio(audio.Default, loop=False)
    toast.add_actions(label="Click me", launch="https://www.google.com")
    toast.add_actions(label="Dismiss", launch=False)
    toast.show()