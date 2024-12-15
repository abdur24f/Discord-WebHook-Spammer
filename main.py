import time, requests, pyfiglet, threading
print(pyfiglet.figlet_format("KINGMAN"))

msg = input("@everyone@everyone@everyone@everyone@everyone@everyone: ")
webhook = input("https://discord.com/api/webhooks/1298796536138043472/lTQBHezjEAQ9up50A8dnUbVz7oRwrfBzsyuE56UcUxgpjaHR8RX5bqOvJ0v5L4IItUl0: ")
th = int(input('Number of thread ? (200 recommended): '))
sleep = int(input("Sleeping time ? (recommended 2): "))
def spam():
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("Bad Webhook :" + webhook)
        time.sleep(sleep)
    
for x in range(th):
    t = threading.Thread(target = spam)
    t.start()
