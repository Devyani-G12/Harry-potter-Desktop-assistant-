import threading
from janu_icon import DraggableIcon
from janu_detect import start_listening

icon = DraggableIcon("hp.png")

t = threading.Thread(target=start_listening, args=(icon,), daemon=True)
t.start()

icon.mainloop()
