class User:
    # Define the fields and methods for your object here.
    def __init__(self,new_username,new_userID):
        self.username = new_username
        self.userID = new_userID
        self.friends = []

    def get_username(self):
        return self.username

    def get_userID(self):
        return self.userID

    def get_friends(self):
        return self.friends

    def add_friends(self, friendID):
        self.friends.append(friendID)


class Network:
    # Define the fields and methods for your object here.
    def __init__(self):
        self.users = []

    def num_users(self):
        return len(self.users)

    def add_users(self, username):
        userID = len(self.users)
        self.users.append(User(username,userID))

    def get_userID(self, username):
        for user in self.users:
            if username == user.get_username():
                userID = user.get_userID()
        return userID


    def add_connections(self, user1, user2):
        user1ID = self.get_userID(user1)
        user2ID = self.get_userID(user2)
        user1 = self.users[user1ID]
        user2 = self.users[user2ID]
        self.users[user2ID].add_friends(user1ID)
        self.users[user1ID].add_friends(user2ID)

    def print_users(self):
        print("This is the network!")
        for user in self.users:
            print("\tUser {}: {}".format(user.get_userID(), user.get_username()))

    def print_connections(self, username):
        user = self.users[self.get_userID(username)]
        connections = user.get_friends()
        print("\t {}'s connections:".format(user.get_username()))
        for friendID in connections:
            friend = self.users[friendID]
            print("\t {}".format(friend.get_username()))

def main():
    # Define the program flow for your user interface here.
    mynetwork = Network()
    done = False
    while not done:

        action = input("\n What would you like to do? Add a user(u), Add a Connection(c), Print Users (p), Print Connections(pc), Exit(e)")
        if action == "u":
            username = input("What username, loser?")
            mynetwork.add_users(username)

        elif action == "c":

            if mynetwork.num_users()<2:
                print("ERROR! Don't have enough users. MAKE FRIENDS!")
                continue

            else:
                user1 = input("First User?")
                user2 = input("Second User?")
            mynetwork.add_connections(user1,user2)

        elif action == "p":
            mynetwork.print_users()

        elif action == "e":
            print("Bye Felicia . . .")
            done = True

        elif action == "pc":
            user = input("Which User?")
            mynetwork.print_connections(user)

        else:
            print("Error. Not recognized action. READ THE LIST!")
            #done=True

# Runs your program.
if __name__ == '__main__':
    main()
