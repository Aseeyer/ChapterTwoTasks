class MenuItem:
    def __init__(self, name, submenu=None):
        self.name = name
        self.submenu = submenu if submenu else []

    def display(self):
        print(f"\n{self.name}:")
        for idx, item in enumerate(self.submenu, start=1):
            print(f"{idx}. {item.name}")
        print("0. Back")

    def select(self, choice):
        if choice == 0:
            return None
        if 1 <= choice <= len(self.submenu):
            return self.submenu[choice - 1]
        else:
            print("Invalid selection")
            return self


class NokiaMenu:
    def __init__(self):
        self.main_menu = self.build_menu()

    def build_menu(self):
        phonebook = MenuItem("Phone Book", [
            MenuItem("Search"),
            MenuItem("Service Nos."),
            MenuItem("Add Name"),
            MenuItem("Erase"),
            MenuItem("Edit"),
            MenuItem("Assign Tone"),
            MenuItem("Send b'card"),
            MenuItem("Options", [
                MenuItem("Type of View"),
                MenuItem("Memory Status")
            ]),
            MenuItem("Speed Dials"),
            MenuItem("Voice Tags")
        ])

        messages = MenuItem("Messages", [
            MenuItem("Write Messages"),
            MenuItem("Inbox"),
            MenuItem("Outbox"),
            MenuItem("Picture Messages"),
            MenuItem("Templates"),
            MenuItem("Smileys"),
            MenuItem("Message Settings", [
                MenuItem("Set 1", [
                    MenuItem("Message Centre Number"),
                    MenuItem("Messages Sent As"),
                    MenuItem("Message Validity")
                ]),
                MenuItem("Common", [
                    MenuItem("Delivery Reports"),
                    MenuItem("Reply via Same Centre"),
                    MenuItem("Character Support")
                ])
            ]),
            MenuItem("Info Service"),
            MenuItem("Voice Mailbox Number"),
            MenuItem("Service Command Editor")
        ])

        call_register = MenuItem("Call Register", [
            MenuItem("Missed Calls"),
            MenuItem("Received Calls"),
            MenuItem("Dialed Numbers"),
            MenuItem("Erase Recent Call Lists"),
            MenuItem("Show Call Duration", [
                MenuItem("Last Call Duration"),
                MenuItem("All Calls' Duration"),
                MenuItem("Received Calls' Duration"),
                MenuItem("Dialed Calls' Duration"),
                MenuItem("Clear Timers")
            ]),
            MenuItem("Show Call Costs", [
                MenuItem("Last Call Cost"),
                MenuItem("All Calls' Cost"),
                MenuItem("Clear Counters")
            ]),
            MenuItem("Call Cost Settings", [
                MenuItem("Call Cost Limit"),
                MenuItem("Show Costs In")
            ]),
            MenuItem("Prepaid Credit")
        ])

        tones = MenuItem("Tones", [
            MenuItem("Ringing Tone"),
            MenuItem("Ringing Volume"),
            MenuItem("Incoming Call Alert"),
            MenuItem("Composer"),
            MenuItem("Message Alert Tone"),
            MenuItem("Keypad Tones"),
            MenuItem("Warning and Game Tones"),
            MenuItem("Vibrating Alert"),
            MenuItem("Screen Saver")
        ])

        settings = MenuItem("Settings", [
            MenuItem("Call Settings", [
                MenuItem("Automatic Redial"),
                MenuItem("Speed Dialing"),
                MenuItem("Call Waiting Options"),
                MenuItem("Own Number Sending"),
                MenuItem("Phone Line in Use"),
                MenuItem("Automatic Answer")
            ]),
            MenuItem("Phone Settings", [
                MenuItem("Language"),
                MenuItem("Cell Info Display"),
                MenuItem("Welcome Note"),
                MenuItem("Network Selection"),
                MenuItem("Lights"),
                MenuItem("Confirm SIM Service Actions")
            ]),
            MenuItem("Security Settings", [
                MenuItem("PIN Code Request"),
                MenuItem("Call Barring Service"),
                MenuItem("Fixed Dialing"),
                MenuItem("Closed User Group"),
                MenuItem("Phone Security"),
                MenuItem("Change Access Codes")
            ]),
            MenuItem("Restore Factory Settings")
        ])

        clock = MenuItem("Clock", [
            MenuItem("Alarm Clock"),
            MenuItem("Clock Settings"),
            MenuItem("Date Setting"),
            MenuItem("Stopwatch"),
            MenuItem("Countdown Timer"),
            MenuItem("Auto Update of Date and Time")
        ])

        return MenuItem("Main Menu", [
            phonebook,
            messages,
            MenuItem("Chat"),
            call_register,
            tones,
            settings,
            MenuItem("Call Divert"),
            MenuItem("Games"),
            MenuItem("Calculator"),
            MenuItem("Reminders"),
            clock,
            MenuItem("Profiles"),
            MenuItem("SIM Services")
        ])

    def run(self):
        current_menu = self.main_menu
        history = []

        while True:
            current_menu.display()
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input")
                continue

            if choice == 0:
                if not history:
                    print("Exiting menu...")
                    break
                current_menu = history.pop()
            else:
                next_menu = current_menu.select(choice)
                if next_menu and next_menu.submenu:
                    history.append(current_menu)
                    current_menu = next_menu
                elif next_menu:
                    print(f"You selected: {next_menu.name}")


if __name__ == "__main__":
    NokiaMenu().run()
