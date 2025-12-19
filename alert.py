class NotificationAlert:
    def __init__(self):
        self.notification: list[str] = []

    def alert(self, note: str):
        self.notification.append(note)

    def clear_alert(self):
        self.notification.clear()

    def display_alert(self):
        if not self.notification:
            return None
        else:
            for i in self.notification:
                print(i)


global notification_alert
notification_alert = NotificationAlert()