# Display main menu
print("""
        LIST OF MENU FUNCTIONS
        1. PHONE BOOK
        2. MESSAGES
        3. CHAT
        4. CALL REGISTER
        5. TONES
        6. SETTINGS
        7. CALL DIVERT
        8. GAMES
        9. CALCULATOR
       10. REMINDERS
       11. CLOCK
       12. PROFILES
       13. SIM SERVICES
""")

main_selection = int(input("Select a menu (1-13): "))

match main_selection:
    case 1:
        print("""
        PHONE BOOK
        1. Search
        2. Service Nos.
        3. Add name
        4. Erase
        5. Edit
        6. Assign tone
        7. Send b’card
        8. Options
        9. Speed dials
        10. Voice tags
        """)
        phonebook = int(input("Select PHONE BOOK option (1-10): "))
        if phonebook == 8:
            print("""
            OPTIONS
            1. Type of view
            2. Memory status
            """)
        option_selection = int(input("Select OPTIONS item (1-2): "))
        if option_selection == 1:
            print("You selected: Type of view")
        elif option_choice == 2:
            print("You selected: Memory status")
        else:
            print("Invalid OPTIONS selection.")

    case 2:
        print("""
        MESSAGES
        1. Write messages
        2. Inbox
        3. Outbox
        4. Picture messages
        5. Templates
        6. Smileys
        7. Message settings
        8. Info Service
        9. Voice Mailbox number
       10. Service command editor
        """)
        msg = int(input("Select MESSAGES option (1-10): "))
        if msg == 7:
            print("""
            MESSAGE SETTINGS
            1. Set
            2. Common
            """)
            msg_set = int(input("Select option (1-2): "))
            if msg_set == 1:
                print("""
                SET
                1. Message centre number
                2. Messages sent as
                3. Message validity
                """)
                set1_selection = int(input("Select set (1-3)"))
                if set1_selection == 1:
                    print("Message centre number")
                elif set1_selection == 2:
                    print("Message sent as")
                elif set1_selection == 3:
                    print("Message validity")
            elif msg_set == 2:
                print("""
                COMMON
                1. Delivery reports
                2. Reply via same centre
                3. Character support
                """)
                common_selection = int(input("Select common (1-3): "))
                if common_selection == 1:
                    print("You selected: Delivery reports")
                elif common_selection == 2:
                    print("You selected: Reply via same centre")
                elif common_selection == 3:
                    print("You selected: Character support")
            else:
                print("invalid input")


    case 3:
        print("CHAT")
    case 4:
        print("""
        CALL REGISTER
        1. Missed calls
        2. Received calls
        3. Dialled numbers
        4. Erase recent call lists
        5. Show call duration
        6. Show call costs
        7. Call cost settings
        8. Prepaid credit
        """)
        reg = int(input("Select CALL REGISTER option (1-8): "))
        if reg == 5:
            print("""
            SHOW CALL DURATION
            1. Last call duration
            2. All calls’ duration
            3. Received calls’ duration
            4. Dialled calls’ duration
            5. Clear timers
            """)
        elif reg == 6:
            print("""
            SHOW CALL COSTS
            1. Last call cost
            2. All calls’ cost
            3. Clear counters
            """)
        elif reg == 7:
            print("""
            CALL COST SETTINGS
            1. Call cost limit
            2. Show costs in
            """)
    case 5:
        print("""
        TONES
        1. Ringing tone
        2. Ringing volume
        3. Incoming call alert
        4. Composer
        5. Message alert tone
        6. Keypad tones
        7. Warning and game tones
        8. Vibrating alert
        9. Screen saver
        """)
    case 6:
        print("""
        SETTINGS
        1. Call settings
        2. Phone settings
        3. Security settings
        4. Restore factory settings
        """)
        sett = int(input("Select SETTINGS option (1-4): "))
        if sett == 1:
            print("""
            CALL SETTINGS
            1. Automatic redial
            2. Speed dialling
            3. Call waiting options
            4. Own number sending
            5. Phone line in use
            6. Automatic answer
            """)
        elif sett == 2:
            print("""
            PHONE SETTINGS
            1. Language
            2. Cell info display
            3. Welcome note
            4. Network selection
            5. Lights
            6. Confirm SIM service actions
            """)
        elif sett == 3:
            print("""
            SECURITY SETTINGS
            1. PIN code request
            2. Call barring service
            3. Fixed dialling
            4. Closed user group
            5. Phone security
            6. Change access codes
            """)
    case 7:
        print("CALL DIVERT")
    case 8:
        print("GAMES")
    case 9:
        print("CALCULATOR")
    case 10:
        print("REMINDERS")
    case 11:
        print("""
        CLOCK
        1. Alarm clock
        2. Clock settings
        3. Date setting
        4. Stopwatch
        5. Countdown timer
        6. Auto update of date and time
        """)
    case 12:
        print("PROFILES")
    case 13:
        print("SIM SERVICES")
    case _:
        print("Invalid input! Try a number between 1 and 13.")
