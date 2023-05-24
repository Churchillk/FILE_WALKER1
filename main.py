try:
    import pyttsx3
    import os
    from time import sleep
    from keyboard import press_and_release, write
except:
    pass

try:
    def keyboards(path_enter):
        try:  # this function will start up file manager automatically and show me the folders location
            press_and_release("right windows")
            sleep(0.5)
            write(current_path)  # this line will write the cuirrent path that the folder was found
            sleep(0.5)
            press_and_release("enter")
            sleep(0.5)
            write(Seek)
            sleep(0.5)
            press_and_release("Enter")
            sleep(0.5)
        except ModuleNotFoundError as err:
            print(err)
        try:
            os.chdir(f'{current_path}\\{Seek}')  # here i have changed the current working directory to the folder found
            os.mkdir(f'{os.getcwd()}\\SUCCESS')  # here i have created a new folder in the folder music lounge
        except:
            talker = pyttsx3.init()
            talker.say("folder exist")
            talker.runAndWait()
except:
    pass
while True:
    Seek = input("enter name of file you wanna look for: ")
    os.chdir(r"C:\\")  # here i have changed the current working directory
    where_to_walk = os.getcwd()  # here we tell the loop where to search by getting the current working directory

    # the loop below prints the path, folders in each path and the files in each folder
    for current_path, folders, files_in_folder in os.walk(where_to_walk):
        # the below if statement controls the loop, if their is a folder named anaconda
        # the loop will skip the folder and say passed
        # the if below will stop the loop incase the folder named Music is located
        if Seek in folders or Seek in files_in_folder:
            print("found at path: ", current_path)
            print("found at index: ", folders.index(Seek))
            sleep(0.5)
            try:
                keyboards(current_path)  # here i have called the keyboards function
            except:
                pass
            break
        print("current path is:  ", current_path)
        print("folders are: ", folders)
        print("files in the current folder are: ", files_in_folder)
        print(
            "______________________________________________________________________________________________________________________________________________________")
