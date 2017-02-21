class RockPaperScissors

  # Exceptions this class can raise:
  class NoSuchStrategyError < StandardError ; end

  def self.winner(player1, player2)
    contest= [player1,player2]
    p1Hand= contest[0][1]
    p2Hand= contest[1][1]
    p1name= contest [0][0]
    p2name= contest [1][0]
  
  if p1Hand != "P"
  if p1Hand != "R"
  if p1Hand != "S"
  raise RockPaperScissors::NoSuchStrategyError.new("Strategy must be one of R,P,S")
  end
  end
  end
  
  
  if p2Hand != "P"
  if p2Hand != "R"
  if p2Hand != "S"
  raise RockPaperScissors::NoSuchStrategyError.new("Strategy must be one of R,P,S")
  end
  end
  end
  
  
   
   
   
    case 
    when p1Hand == p2Hand
       winnerName = p1name
       winningHand=p1Hand
    when p1Hand=="P" && p2Hand=="R"
       winnerName = p1name
       winningHand=p1Hand
    when p1Hand=="R" && p2Hand=="S"
       winnerName = p1name
       winningHand=p1Hand
    when p1Hand=="S" && p2Hand=="P"
       winnerName = p1name
       winningHand=p1Hand
    when p1Hand=="P" && p2Hand=="S"
       winnerName = p2name
       winningHand=p2Hand
    when p1Hand=="S" && p2Hand=="R"
       winnerName = p2name
       winningHand=p2Hand
    when p1Hand=="R" && p2Hand=="P"
       winnerName = p2name
       winningHand=p2Hand
    end
  
  
  contestWinner=[winnerName,winningHand]
  return contestWinner
    end






def self.tournament_winner(tournament)

if tournament[0][0].is_a?(Array)

currentPos=0
currentWinnerSpot=0
playerList=[]
roundWinners=[]
tournament.each do |i|
i.each do |j|
j.each do |k|
playerList.push k
end
end
end
rounds=playerList.length/2
rounds=rounds-1
 rounds.times do      
  while currentPos<=playerList.length-3
   matchWinner=RockPaperScissors.winner(playerList[currentPos],playerList[currentPos+1]) 
   roundWinners[currentWinnerSpot]=matchWinner
   currentPos+=2
   currentWinnerSpot+=1
  end 
  currentPos=0
  currentWinnerSpot=0
  playerList=roundWinners

 end
finalWinner=RockPaperScissors.winner(playerList[0],playerList[1])
return finalWinner

else
finalWinner=RockPaperScissors.winner(tournament[0],tournament[1])
return finalWinner
end
end



end




