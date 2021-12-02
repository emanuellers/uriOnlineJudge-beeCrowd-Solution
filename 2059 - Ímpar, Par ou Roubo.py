readPlayersInput = input()
playersChoices = readPlayersInput.split()
choice = int(playersChoices[0])
playerOneNumber = int(playersChoices[1])
playerTwoNumber = int(playersChoices[2])
playerOneChoice = int(playersChoices[3])
playerTwoChoice = int(playersChoices[4])

sumResult = playerOneNumber + playerTwoNumber
oddOrEven = (sumResult % 2 == 0  and choice == 1) or (sumResult % 2 !=0  and choice == 0)
onlyOneWrong = (playerOneChoice == 1 and playerTwoChoice == 0)  or (playerOneChoice == 0 and playerTwoChoice ==1) 
stole = (playerOneChoice == 0 and playerTwoChoice == 0)

if (stole and oddOrEven) or onlyOneWrong :
    print("Jogador 1 ganha!")
else:
    print("Jogador 2 ganha!")
