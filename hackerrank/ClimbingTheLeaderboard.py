"""
An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number 1  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
"""
def climbingLeaderboard(ranked, player):
    playerRankings = []
    ranked = sorted(set(ranked), reverse=True)
    topRanking = False
    for score in player:
        rank = 1
        for r in ranked:
            if score >= r:
                playerRankings.append(rank)
                topRanking = True
                break
            rank += 1
        if not topRanking:
            playerRankings.append(rank)
    return playerRankings

#used set instead of list to condense the number of elements to be checked, but still having timing issues. i guess when turning a list into a set, ordering is not maintained so i am forced to sort the set. this may be my issue for exceeding the time limit, or there is an easier way to do this     

"""
def climbingLeaderboard(ranked, player):
    playerRankings = []
    for score in player:
        rank = 1
        for i in range(len(ranked)):
            if score >= ranked[i]:
                playerRankings.append(rank)
                break
            else:
                try:
                    if ranked[i] == ranked[i+1]:
                        continue
                    else:
                        rank+=1
                except:
                    rank+=1
                    playerRankings.append(rank)
    return playerRankings
"""

#timeout cases failing
