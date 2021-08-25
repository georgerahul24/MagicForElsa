import os


def check_user_from_file(username):
    try:
        userpth = os.getcwd() + '\\resources\\ users.elsa'
        file = open(userpth, 'r')
        lines = file.read().splitlines()
        part2 = None
        for line in lines:
            parts = line.split('-')
            part1 = parts[0]  #username
            part2 = parts[1]  #passwords
            if part1 == username:
                break
        #Returns password if username is found else returns None
        return part2
    except Exception as e:
        print('It seems that some error has happened', e)


def write_to_file(username, password):
    try:
        userpth = os.getcwd() + '\\resources\\ users.elsa'
        file = open(userpth)
        lines = file.read().splitlines()
        #Check if username is new or old with count variable
        count = 0
        for line in lines:
            parts = line.split('-')
            part1 = parts[0]  # username
            part2 = parts[1]  # passwords
            if part1 == username:
                count += 1
        #if count is zero,it mens that the username exists
        #username should not be empty as it can cause problems when reading it
        #usernames shld not be have the name of program file as history files will overwrite the program files
        if count == 0 and len(username) != 0 and username not in [
                'initial', 'cache', 'users', 'user', 'theme', 'indexer'
        ]:
            userpth = os.getcwd() + '\\resources\\ users.elsa'
            file = open(userpth, 'a')
            file.write(f"\n{username}-{password}")
            file.close()
            print(f"Added user {username} ")
            #returns state = 1 so that program knows that writing was succesful
            state = 1

        else:
            print('User already exists')
            #return state = -1 to know that user wasnt added successfully due to username repetitions,empty username,username conflicts,etc
            state = -1
        return state
    except Exception as e:
        print(e, 'Try again')
