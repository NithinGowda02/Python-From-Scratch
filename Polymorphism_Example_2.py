#### **Programming Example in Code**:

#### Consider notifications in a social media app, where different types have the same `send()` method but behave uniquely:


class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Sending Email")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS")

notifications = [EmailNotification(), SMSNotification()]
for notification in notifications:
    notification.send()


# Each notification type behaves differently while sharing a common interface.

