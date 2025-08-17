l1=["What is the capital of France?","Who wrote the play 'Romeo and Juliet'?","What is the largest planet in our solar system?","Which element has the chemical symbol 'O'?","Who is known as the 'Father of Computers'?","What is the smallest country in the world by land area?","Which ocean is the largest by surface area?","What is the hardest natural substance on Earth?","Who painted the Mona Lisa?","Which planet is known as the Red Planet?","What is the longest river in the world?","Who discovered penicillin?","What is the largest desert in the world?","Which country is known as the Land of the Rising Sun?","What is the main ingredient in traditional Japanese miso soup?"]

l2=[["A) Berlin"," B)Madrid"," C) Paris"," D) Rome"],["A) William Shakespeare","B) Charles Dickens","C) Mark Twain","D) Jane Austen"],["A) Earth","B) Mars","C) Jupiter","D) Saturn"],["A) Gold","B) Oxygen","C) Osmium","D) Oganesson"],["A) Alan Turing","B) Charles Babbage","C) Bill Gates","D) Steve Jobs"],["A) Monaco","B) Vatican City","C) San Marino","D) Liechtenstein"],["A) Atlantic Ocean","B) Indian Ocean","C) Arctic Ocean","D) Pacific Ocean"],["A) Gold","B) Iron","C) Diamond","D) Platinum"],["A) Vincent van Gogh","B) Pablo Picasso","C) Leonardo da Vinci","D) Claude Monet"],["A) Venus","B) Mars","C) Mercury","D) Neptune"],["A) Amazon River","B) Nile River","C) Yangtze River","D) Mississippi River"],["A) Marie Curie","B) Alexander Fleming","C) Louis Pasteur","D) Isaac Newton"],["A) Sahara Desert","B) Arabian Desert","C) Gobi Desert","D) Antarctic Desert"],["A) China","B) Japan","C) South Korea","D) Thailand"],["A) Tofu","B) Seaweed","C) Miso paste","D) Rice"]]

l3=["C","A","C","B","B","B","D","C","C","B","B","B","D","B","C"]

l4=["C) Paris","A) William Shakespeare","C) Jupiter","B) Oxygen","B) Charles Babbage","B) Vatican City","D) Pacific Ocean","C) Diamond","C) Leonardo da Vinci","B) Mars","B) Nile River","B) Alexander Fleming","D) Antarctic Desert","B) Japan","C) Miso paste"]

l5=["1000Rs.","2000Rs.","3000Rs.","5000Rs.","10,000Rs.","20,000Rs.","40,000Rs.","80,000Rs.","1,60,000Rs.","3,20,000Rs.","6,40,000Rs.","12,50,000Rs.","25,00,000Rs.","50,00,000Rs.","1,00,00,000Rs."]

print("Start:")
for i in range(len(l1)):
    print(i+1)
    print(l1[i])
    print(l2[i])
    ans=input("Select the correct option for the answer:")
    if(ans==l3[i]):
        print(f"Correct ansswer!!! {l4[i]}")
        print(f"Congratulations!! You won{ l5[i]}")
    else:
        print("Wrong answer")
        if(i==4):
            print("You lost!!")
            print("Game ends")
            exit()
        elif(i==9):
            print("Game ends")
            print("Congratulations !!  You won 10,000Rs.")
            exit()
        elif(i==14):
            print("Game ends here")
            print("Congratulations !!  You won 3,20,000Rs.")
            exit()