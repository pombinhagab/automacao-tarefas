import pyautogui
import time
from winotify import Notification, audio

notificacao = Notification(
    app_id="Pegar posição do mouse",
    title="Posicione o mouse no local desejado e aguarde 5 segundos."
)
notificacao.set_audio(audio.Default, loop=False)
notificacao.show()

time.sleep(5)

x, y = pyautogui.position()
print("Posição atual do mouse")
print(f"x = {str(x)}" + f" y = {str(y)}")
