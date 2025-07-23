print("""
Main Menu:
 1. Phone book
 2. Messages
 3. Chat
 4. Call Register
 5. Tones
 6. Settings
 7. Call Divert
 8. Games
 9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM Services
""")

main = int(input("Enter a number of your choice: "))

match main:
    case 1:
        print("""
Phone Book Section:
 1. Search
 2. Service Nos.
 3. Add Name
 4. Erase
 5. Edit
 6. Assign Tone
 7. Send B'Card
 8. Options
 9. Speed Dials
10. Voice Tags
""")
        phonebook = int(input("Enter a selection: "))
        match phonebook:
            case 1: print("You selected: Search")
            case 2: print("You selected: Service Nos.")
            case 3: print("You selected: Add Name")
            case 4: print("You selected: Erase")
            case 5: print("You selected: Edit")
            case 6: print("You selected: Assign Tone")
            case 7: print("You selected: Send B'Card")
            case 8:
                print("""
Options:
1. Type of View
2. Memory Status
""")
                option = int(input("Enter a selection: "))
                match option:
                    case 1: print("You selected: Type of View")
                    case 2: print("You selected: Memory Status")
                    case _: print("Invalid Options selection")
            case 9: print("You selected: Speed Dials")
            case 10: print("You selected: Voice Tags")
            case _: print("Invalid Phone Book selection")

    case 2:
        print("""
Messages Section:
 1. Write Messages
 2. Inbox
 3. Outbox
 4. Picture Messages
 5. Templates
 6. Smileys
 7. Message Settings
 8. Info Service
 9. Voice Mailbox Number
10. Service Command Editor
""")
        messages = int(input("Enter a selection: "))
        match messages:
            case 1: print("You selected: Write Messages")
            case 2: print("You selected: Inbox")
            case 3: print("You selected: Outbox")
            case 4: print("You selected: Picture Messages")
            case 5: print("You selected: Templates")
            case 6: print("You selected: Smileys")
            case 7:
                print("""
Message Settings:
1. Set 1
2. Common
""")
                setting = int(input("Enter a selection: "))
                match setting:
                    case 1:
                        print("""
Set 1:
1. Message Centre Number
2. Messages Sent As
3. Message Validity
""")
                        s1 = int(input("Enter a selection: "))
                        match s1:
                            case 1: print("You selected: Message Centre Number")
                            case 2: print("You selected: Messages Sent As")
                            case 3: print("You selected: Message Validity")
                            case _: print("Invalid Set 1 selection")
                    case 2:
                        print("""
Common:
1. Delivery Reports
2. Reply via Same Centre
3. Character Support
""")
                        c1 = int(input("Enter a selection: "))
                        match c1:
                            case 1: print("You selected: Delivery Reports")
                            case 2: print("You selected: Reply via Same Centre")
                            case 3: print("You selected: Character Support")
                            case _: print("Invalid Common selection")
                    case _: print("Invalid Message Settings selection")
            case 8: print("You selected: Info Service")
            case 9: print("You selected: Voice Mailbox Number")
            case 10: print("You selected: Service Command Editor")
            case _: print("Invalid Messages selection")

    case 3:
        print("You selected: Chat")

    case 4:
        print("""
Call Register:
1. Missed Calls
2. Received Calls
3. Dialed Numbers
4. Erase Recent Call Lists
5. Show Call Duration
6. Show Call Costs
7. Call Cost Settings
8. Prepaid Credit
""")
        reg = int(input("Enter a selection: "))
        match reg:
            case 1: print("You selected: Missed Calls")
            case 2: print("You selected: Received Calls")
            case 3: print("You selected: Dialed Numbers")
            case 4: print("You selected: Erase Recent Call Lists")
            case 5:
                print("""
Show Call Duration:
1. Last Call Duration
2. All Calls' Duration
3. Received Calls' Duration
4. Dialed Calls' Duration
5. Clear Timers
""")
                dur = int(input("Enter a selection: "))
                match dur:
                    case 1: print("You selected: Last Call Duration")
                    case 2: print("You selected: All Calls' Duration")
                    case 3: print("You selected: Received Calls' Duration")
                    case 4: print("You selected: Dialed Calls' Duration")
                    case 5: print("You selected: Clear Timers")
                    case _: print("Invalid Duration selection")
            case 6:
                print("""
Show Call Costs:
1. Last Call Cost
2. All Calls' Cost
3. Clear Counters
""")
                cost = int(input("Enter a selection: "))
                match cost:
                    case 1: print("You selected: Last Call Cost")
                    case 2: print("You selected: All Calls' Cost")
                    case 3: print("You selected: Clear Counters")
                    case _: print("Invalid Cost selection")
            case 7:
                print("""
Call Cost Settings:
1. Call Cost Limit
2. Show Costs In
""")
                limit = int(input("Enter a selection: "))
                match limit:
                    case 1: print("You selected: Call Cost Limit")
                    case 2: print("You selected: Show Costs In")
                    case _: print("Invalid Call Cost Settings selection")
            case 8: print("You selected: Prepaid Credit")
            case _: print("Invalid Call Register selection")

    case 5:
        print("""
Tones:
1. Ringing Tone
2. Ringing Volume
3. Incoming Call Alert
4. Composer
5. Message Alert Tone
6. Keypad Tones
7. Warning and Game Tones
8. Vibrating Alert
9. Screen Saver
""")
        tone = int(input("Enter a selection: "))
        match tone:
            case 1: print("You selected: Ringing Tone")
            case 2: print("You selected: Ringing Volume")
            case 3: print("You selected: Incoming Call Alert")
            case 4: print("You selected: Composer")
            case 5: print("You selected: Message Alert Tone")
            case 6: print("You selected: Keypad Tones")
            case 7: print("You selected: Warning and Game Tones")
            case 8: print("You selected: Vibrating Alert")
            case 9: print("You selected: Screen Saver")
            case _: print("Invalid Tones selection")

    case 6:
        print("""
Settings:
1. Call Settings
2. Phone Settings
3. Security Settings
4. Restore Factory Settings
""")
        settings = int(input("Enter a selection: "))
        match settings:
            case 1:
                print("""
Call Settings:
1. Automatic Redial
2. Speed Dialing
3. Call Waiting Options
4. Own Number Sending
5. Phone Line in Use
6. Automatic Answer
""")
                cset = int(input("Enter a selection: "))
                match cset:
                    case 1: print("You selected: Automatic Redial")
                    case 2: print("You selected: Speed Dialing")
                    case 3: print("You selected: Call Waiting Options")
                    case 4: print("You selected: Own Number Sending")
                    case 5: print("You selected: Phone Line in Use")
                    case 6: print("You selected: Automatic Answer")
                    case _: print("Invalid Call Settings selection")
            case 2:
                print("""
Phone Settings:
1. Language
2. Cell Info Display
3. Welcome Note
4. Network Selection
5. Lights
6. Confirm SIM Service Actions
""")
                pset = int(input("Enter a selection: "))
                match pset:
                    case 1: print("You selected: Language")
                    case 2: print("You selected: Cell Info Display")
                    case 3: print("You selected: Welcome Note")
                    case 4: print("You selected: Network Selection")
                    case 5: print("You selected: Lights")
                    case 6: print("You selected: Confirm SIM Service Actions")
                    case _: print("Invalid Phone Settings selection")
            case 3:
                print("""
Security Settings:
1. PIN Code Request
2. Call Barring Service
3. Fixed Dialing
4. Closed User Group
5. Phone Security
6. Change Access Codes
""")
                sec = int(input("Enter a selection: "))
                match sec:
                    case 1: print("You selected: PIN Code Request")
                    case 2: print("You selected: Call Barring Service")
          	    case 3: print("You selected: Fixed Dialing")
                    case 4: print("You selected: Closed User Group")
                    case 5: print("You selected: Phone Security")
            		case 6: print("You selected: Change Access Codes")
                    case _: print("Invalid Security Settings selection")
            case 4:
                print("You selected: Restore Factory Settings")
            case _: print("Invalid Settings selection")

    case 7:
        print("You selected: Call Divert")
    case 8:
        print("You selected: Games")
    case 9:
        print("You selected: Calculator")
    case 10:
        print("You selected: Reminders")
    case 11:
        print("""
Clock:
1. Alarm Clock
2. Clock Settings
3. Date Setting
4. Stopwatch
5. Countdown Timer
6. Auto Update of Date and Time
""")
        clock : int(input("Enter a selection: "))
        match clock:
            case 1: print("You selected: Alarm Clock")
            case 2: print("You selected: Clock Settings")
            case 3: print("You selected: Date Setting")
            case 4: print("You selected: Stopwatch")
            case 5: print("You selected: Countdown Timer")
            case 6: print("You selected: Auto Update of Date and Time")
            case _: print("Invalid Clock selection")
    case 12:
        print("You selected: Profiles")
    case 13:
        print("You selected: SIM Services")
    case _:
        print("Invalid Main Menu selection")
