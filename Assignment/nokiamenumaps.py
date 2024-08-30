def main():
    main_menu()

def main_menu():
    introduction = """
NOKIA 3310 MENU MAP
Let us help you learn about your new Nokia phone.
The menu map you see will take you through the main 
menu functions in the order they appear on your phone.

We've included visuals of the 13 menu functions and 
they are numbered 1-13 so you can see the sequence at a glance.
And right next to each menu function screen we've listed the special 
features in your Nokia phone, also in order of appearance so 
they'll be easy to find.

                ********************************

                input 1 for Phone Book
                input 2 for Messages
                input 3 for Chat
                input 4 for Call Register
                input 5 for Tones
                input 6 for Settings
                input 7 for Call Divert
                input 8 for Games
                input 9 for Calculator
                input 10 for Reminders
                input 11 for Clock
                input 12 for Profiles
                input 13 for SIM Services

                ********************************

                What do you want to do?
                """
    print(introduction)
    menu_options = int(input())
    
    if menu_options == 1:
        phone_book_menu()
    elif menu_options == 2:
        messages_menu()
    elif menu_options == 3:
        print("Chat")
    elif menu_options == 4:
        call_register_menu()
    elif menu_options == 5:
        tones_menu()
    elif menu_options == 6:
        settings_menu()
    elif menu_options == 7:
        print("Call Divert")
    elif menu_options == 8:
        print("Games")
    elif menu_options == 9:
        print("Calculator")
    elif menu_options == 10:
        print("Reminders")
    elif menu_options == 11:
        clock_menu()
    elif menu_options == 12:
        print("Profiles")
    elif menu_options == 13:
        print("SIM Services")
    else:
        print("This number is invalid. Thank you")
    
    print("\nThank you for using this service\nNOKIA... connecting people.")

def phone_book_menu():
    phonebook_menu = """
                ********************************
                
                input 1 for Search
                input 2 for Service Nos.
                input 3 for Add name
                input 4 for Erase
                input 5 for Edit
                input 6 for Assign Tone
                input 7 for Send b'card
                input 8 for Options
                input 9 for Speed Dials
                input 10 for Voice Tags
                input 0 to go back to Main menu

                ********************************
                What do you want to do?
                """
    print(phonebook_menu)
    phone_book = int(input())
    
    if phone_book == 1:
        print("Search")
    elif phone_book == 2:
        print("Service Nos.")
    elif phone_book == 3:
        print("Add name")
    elif phone_book == 4:
        print("Erase")
    elif phone_book == 5:
        print("Edit")
    elif phone_book == 6:
        print("Assign Tone")
    elif phone_book == 7:
        print("Send b'card")
    elif phone_book == 8:
        options_menu()
    elif phone_book == 9:
        print("Speed Dials")
    elif phone_book == 10:
        print("Voice Tags")
    elif phone_book == 0:
        main_menu()
    else:
        print("This menu does not exist")

def messages_menu():
    messages_menu = """
                ********************************
                
                input 1 for Write Messages
                input 2 for Inbox
                input 3 for Outbox
                input 4 for Picture Messages
                input 5 for Templates
                input 6 for Smileys
                input 7 for Message Settings
                input 8 for Info Service
                input 9 for Voice mailbox number
                input 10 for Service command editor
                input 0 to go back to Main menu

                ********************************
                What do you want to do?
                """
    print(messages_menu)
    messages = int(input())
    
    if messages == 1:
        print("Write Messages")
    elif messages == 2:
        print("Inbox")
    elif messages == 3:
        print("Outbox")
    elif messages == 4:
        print("Picture Messages")
    elif messages == 5:
        print("Templates")
    elif messages == 6:
        print("Smileys")
    elif messages == 7:
        message_settings_menu()
    elif messages == 8:
        print("Info Service")
    elif messages == 9:
        print("Voice Mailbox Number")
    elif messages == 10:
        print("Service Command Editor")
    elif messages == 0:
        main_menu()
    else:
        print("This menu does not exist")

def call_register_menu():
    call_register_menu = """
                ********************************
                
                input 1 for Missed Calls
                input 2 for Received Calls
                input 3 for Dialled Numbers
                input 4 for Erase recent call lists
                input 5 for Show Call duration
                input 6 for Show Call costs
                input 7 for Call Cost settings
                input 8 for Prepaid Credit
                input 0 to go back to main menu

                ********************************
                What do you want to do?
                """
    print(call_register_menu)
    call_register = int(input())
    
    if call_register == 1:
        print("Missed Calls")
    elif call_register == 2:
        print("Received Calls")
    elif call_register == 3:
        print("Dialled Numbers")
    elif call_register == 4:
        print("Erase recent call lists")
    elif call_register == 5:
        show_call_duration_menu()
    elif call_register == 6:
        show_call_costs_menu()
    elif call_register == 7:
        call_cost_settings_menu()
    elif call_register == 8:
        print("Prepaid Credit")
    elif call_register == 0:
        main_menu()
    else:
        print("This menu does not exist")

def tones_menu():
    tones_menu = """
                ********************************
                
                input 1 for Ringing Tone
                input 2 for Ringing Volume
                input 3 for Incoming Call alert
                input 4 for Composer
                input 5 for Message alert tone
                input 6 for Keypad tones
                input 7 for Warning and game tones
                input 8 for Vibrating alert
                input 9 for Screen saver
                input 0 to go back to Main menu

                ********************************
                What do you want to do?
                """
    print(tones_menu)
    tones_options = int(input())
    
    if tones_options == 1:
        print("Ringing Tone")
    elif tones_options == 2:
        print("Ringing Volume")
    elif tones_options == 3:
        print("Incoming Call alert")
    elif tones_options == 4:
        print("Composer")
    elif tones_options == 5:
        print("Message alert tone")
    elif tones_options == 6:
        print("Keypad tones")
    elif tones_options == 7:
        print("Warning and game tones")
    elif tones_options == 8:
        print("Vibrating alert")
    elif tones_options == 9:
        print("Screen saver")
    elif tones_options == 0:
        main_menu()
    else:
        print("This menu does not exist")

def clock_menu():
    clock_menu = """
                ********************************
                
                input 1 for Alarm Clock
                input 2 for Clock Settings
                input 3 for Date Setting
                input 4 for Stopwatch
                input 5 for Countdown timer
                input 6 for Auto update of date and time
                input 0 to go back to Main menu

                ********************************
                What do you want to do?
                """
    print(clock_menu)
    clock_options = int(input())
    
    if clock_options == 1:
        print("Alarm Clock")
    elif clock_options == 2:
        print("Clock Settings")
    elif clock_options == 3:
        print("Date Setting")
    elif clock_options == 4:
        print("Stopwatch")
    elif clock_options == 5:
        print("Countdown timer")
    elif clock_options == 6:
        print("Auto update of date and time")
    elif clock_options == 0:
        main_menu()
    else:
        print("This menu does not exist")

def settings_menu():
    settings_menu = """
                ********************************
                
                input 1 for Call Settings
                input 2 for Phone Settings
                input 3 for Security Settings
                input 4 for Restore Factory Settings
                input 0 to go back to Main menu

                ********************************
                What do you want to do?
                """
    print(settings_menu)
    settings = int(input())
    
    if settings == 1:
        call_settings_menu()
    elif settings == 2:
        phone_settings_menu()
    elif settings == 3:
        security_settings_menu()
    elif settings == 4:
        print("Restore Factory Settings")
    elif settings == 0:
        main_menu()
    else:
        print("This menu does not exist")

def options_menu():
    options_menu = """
                ********************************
                
                input 1 for Type of View
                input 2 for Memory Status
                input 0 to go back to Phonebook menu

                ********************************
                What do you want to do?
                """
    print(options_menu)
    options = int(input())
    
    if options == 1:
        print("Type of View")
    elif options == 2:
        print("Memory Status")
    elif options == 0:
        phone_book_menu()
    else:
        print("This menu does not exist")

def message_settings_menu():
    message_settings_menu = """
                ********************************
                
                input 1 for Set 1
                input 2 for Common
                input 0 to go back to Messages menu

                ********************************
                What do you want to do?
                """
    print(message_settings_menu)
    message_settings = int(input())
    
    if message_settings == 1:
        set1_menu()
    elif message_settings == 2:
        common_menu()
    elif message_settings == 0:
        messages_menu()
    else:
        print("This menu does not exist")

def set1_menu():
    set1_menu = """
                ********************************
                
                input 1 for Message Centre Number
                input 2 for Messages sent as
                input 3 for Message Validity
                input 0 to go back to Message Settings menu

                ********************************
                What do you want to do?
                """
    print(set1_menu)
    set1 = int(input())
    
    if set1 == 1:
        print("Message Centre Number")
    elif set1 == 2:
        print("Messages sent as")
    elif set1 == 3:
        print("Message Validity")
    elif set1 == 0:
        message_settings_menu()
    else:
        print("This menu does not exist")

def common_menu():
    common_menu = """
                ********************************
                
                input 1 for Delivery Reports
                input 2 for Reply via same centre
                input 3 for Character Support
                input 0 to go back to Message Settings menu

                ********************************
                What do you want to do?
                """
    print(common_menu)
    common = int(input())
    
    if common == 1:
        print("Delivery Reports")
    elif common == 2:
        print("Reply via same centre")
    elif common == 3:
        print("Character Support")
    elif common == 0:
        message_settings_menu()
    else:
        print("This menu does not exist")

def call_settings_menu():
    call_settings_menu = """
                ********************************
                
                input 1 for Automatic Redial
                input 2 for Speed Dialling
                input 3 for Call Waiting Options
                input 4 for Own Number Sending
                input 5 for Phone Line in use
                input 6 for Automatic Answer
                input 0 to go back to Settings menu

                ********************************
                What do you want to do?
                """
    print(call_settings_menu)
    call_settings = int(input())
    
    if call_settings == 1:
        print("Automatic Redial")
    elif call_settings == 2:
        print("Speed Dialling")
    elif call_settings == 3:
        print("Call Waiting Options")
    elif call_settings == 4:
        print("Own Number Sending")
    elif call_settings == 5:
        print("Phone Line in use")
    elif call_settings == 6:
        print("Automatic Answer")
    elif call_settings == 0:
        settings_menu()
    else:
        print("This menu does not exist")

def phone_settings_menu():
    phone_settings_menu = """
                ********************************
                
                input 1 for Language
                input 2 for Cell Info Display
                input 3 for Welcome Note
                input 4 for Network Selection
                input 5 for Lights
                input 6 for Confirm SIM service actions
                input 0 to go back to Settings menu

                ********************************
                What do you want to do?
                """
    print(phone_settings_menu)
    phone_settings = int(input())
    
    if phone_settings == 1:
        print("Language")
    elif phone_settings == 2:
        print("Cell Info Display")
    elif phone_settings == 3:
        print("Welcome Note")
    elif phone_settings == 4:
        print("Network Selection")
    elif phone_settings == 5:
        print("Lights")
    elif phone_settings == 6:
        print("Confirm SIM service actions")
    elif phone_settings == 0:
        settings_menu()
    else:
        print("This menu does not exist")

def security_settings_menu():
    security_settings_menu = """
                ********************************
                
                input 1 for PIN code request
                input 2 for Call Barring Service
                input 3 for Fixed Dialling
                input 4 for Closed User Group
                input 5 for Phone Security
                input 6 for Change Access Codes
                input 0 to go back to Settings menu

                ********************************
                What do you want to do?
                """
    print(security_settings_menu)
    security_settings = int(input())
    
    if security_settings == 1:
        print("PIN code request")
    elif security_settings == 2:
        print("Call Barring Service")
    elif security_settings == 3:
        print("Fixed Dialling")
    elif security_settings == 4:
        print("Closed User Group")
    elif security_settings == 5:
        print("Phone Security")
    elif security_settings == 6:
        print("Change Access Codes")
    elif security_settings == 0:
        settings_menu()
    else:
        print("This menu does not exist")

def show_call_duration_menu():
    call_duration_menu = """
                ********************************
                
                input 1 for Last call duration
                input 2 for All calls' duration
                input 3 for Received calls' duration
                input 4 for Dialled calls' duration
                input 5 for Clear timers
                input 0 to go back to Call Register menu

                ********************************
                What do you want to do?
                """
    print(call_duration_menu)
    call_duration = int(input())
    
    if call_duration == 1:
        print("Last call duration")
    elif call_duration == 2:
        print("All calls' duration")
    elif call_duration == 3:
        print("Received calls' duration")
    elif call_duration == 4:
        print("Dialled calls' duration")
    elif call_duration == 5:
        print("Clear timers")
    elif call_duration == 0:
        call_register_menu()
    else:
        print("This menu does not exist")

def show_call_costs_menu():
    call_costs_menu = """
                ********************************
                
                input 1 for Last call cost
                input 2 for All calls' cost
                input 3 for Clear counters
                input 0 to go back to Call Register menu

                ********************************
                What do you want to do?
                """
    print(call_costs_menu)
    call_costs = int(input())
    
    if call_costs == 1:
        print("Last call cost")
    elif call_costs == 2:
        print("All calls' cost")
    elif call_costs == 3:
        print("Clear counters")
    elif call_costs == 0:
        call_register_menu()
    else:
        print("This menu does not exist")

def call_cost_settings_menu():
    call_cost_settings_menu = """
                ********************************
                
                input 1 for Call cost limit
                input 2 for Show costs in
                input 0 to go back to Call Register menu

                ********************************
                What do you want to do?
                """
    print(call_cost_settings_menu)
    call_cost_settings = int(input())
    
    if call_cost_settings == 1:
        print("Call cost limit")
    elif call_cost_settings == 2:
        print("Show costs in")
    elif call_cost_settings == 0:
        call_register_menu()
    else:
        print("This menu does not exist")

if __name__ == "__main__":
    main()
