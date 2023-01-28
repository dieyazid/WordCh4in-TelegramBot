import random

class Game:
    users={}
    def __init__(self):
        with open("words.txt") as f:
            self.words = f.read().splitlines()
        self.duplicated=[]
        self.current_word=""
        self.input_word=""
    
    ### Checkers ###
    def Valid_Check(self,word):
        if word in self.words: 
            # self.duplicated.append(word)
            return True
        else: return False

    def Duplicate_Check(self,word):
        if word in self.duplicated:
            return True
        else: 
            self.duplicated.append(word)
            return False

    def First_Letter_Check(self,word):
        last_letter = self.current_word[-1]
        #check if last letter match the first
        if word[0]!=last_letter:
            return True
        else:
            return False

    def Ai_Turn(self,First=False,Current_Word=any):
        if First==True:
            selected_word= random.choice(self.words)
            self.current_word=selected_word
            self.duplicated.append(selected_word)
            return selected_word
        else:
            if not self.Valid_Check(Current_Word):
                return 'You Lost'
            # Get the last letter of the Current In game word
            last_letter = Current_Word[-1]

            # Find words that start with the last letter
            matching_words = [word for word in self.words if word[0] == last_letter]

            # If there are no matching words, give an error message
            if len(matching_words) == 0:
                return 'You won'
                # return "I don't know any word that start with that letter. You won 😖"
            else:
                for word in matching_words:
                    if self.Duplicate_Check(word):
                        pass
                    else:
                        # self.duplicated.append(word)
                        self.current_word=word
                        return word
                return 'You won'

    def Player_Turn(self,First=False,Current_Word=any):
        if First==True:
            if not self.Valid_Check(Current_Word):
                return 'You Lost'
            else:
                self.current_word=Current_Word
                self.duplicated.append(Current_Word)
        else:
            if not self.Valid_Check(Current_Word):
                return 'Unvalid'
            elif self.First_Letter_Check(Current_Word):
                return 'Letter Fail'
            elif self.Duplicate_Check(Current_Word):
                return 'Duplicated'
            # self.duplicated.append(Current_Word)
            self.current_word=Current_Word
            return 'Valid'


    def valid(self,result,word):
        if result: 
            self.current_word= word
        return result


    def handle_user(user_id):
        if user_id not in Game.users:
            Game.users[user_id] = Game()
        return Game.users[user_id]






