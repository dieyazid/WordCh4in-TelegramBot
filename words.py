import random

class Game:
    users={}
    def __init__(self):
        with open("words.txt") as f:
            self.words = f.read().splitlines()
        self.duplicated=[]
        self.current_word=""
        self.input_word=""

    
    def word_checker(self, word,first=False):
        print(self.current_word)
        input_word = word.lower()
        if not first:
            last_letter = self.current_word[-1]
            #check if last letter match the first
            if input_word[0]!=last_letter:
                return False
            #check if input word is duplicate
            if input_word in self.duplicated :
                return False
        #check if word is in dictanory 
        if input_word in self.words: 
            self.duplicated.append(input_word)
            return True
        else: return False

    def ai_first_turn(self):
        selected_word= random.choice(self.words)
        self.current_word= selected_word
        self.words.remove(selected_word)
        self.word_checker(selected_word)
        return selected_word

    def player_first_turn(self,word):
        return self.valid(self.word_checker(word,first=True),word)


    def ai_turn(self,user_input):
        # Get the last letter of the input
        last_letter = user_input[-1]

        # Find words that start with the last letter
        matching_words = [word for word in self.words if word[0] == last_letter]

        # If there are no matching words, give an error message
        if len(matching_words) == 0:
            return "I don't know any word that start with that letter. You won 😖"
        else:
            # Randomly choose a word from the matching words
            chosen_word = random.choice(matching_words)
            self.duplicated.append(chosen_word)
            return chosen_word
        
    def player_turn(self, word):
        nword=word.lower()
        return self.valid(self.word_checker(nword),nword)


    def valid(self,result,word):
        if result: 
            self.current_word= word
            self.duplicated.append(word)
        return result


    def handle_user(user_id):
        if user_id not in Game.users:
            Game.users[user_id] = Game()
        return Game.users[user_id]





