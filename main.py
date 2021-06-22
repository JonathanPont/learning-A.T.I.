name = input('ATI, What is your name?\n')
print(' Hi', name)

print(" I'm A.T.I, python version.")

print(" You can ask me questions, and give me answers to ones I dont know.")
questions = ["whats your name", "how are you", "who is your creator", "who am i"]
answers = ["ATI, Atifitcial Teachable Intelegence.", "I'm good, thanks", "Jonathan Pont", name]


def next_question():
  
  question = input ("please ask a question\n").lower()

  if (question) in questions:
    print (answers[questions.index(question)])
    next_question()

  else:
    answer = input("I don't know that one yet, what would be a appropriate response. use " + '"(cancel)"' + " to cancel question.\n")

    if answer == "(cancel)":
      print("question and answer canceled")
      next_question()
    
    else:
      questions.append(question)
      answers.append(answer)
      next_question()

next_question()