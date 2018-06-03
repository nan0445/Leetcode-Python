class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand)%W!=0:
            return False
        n = len(hand)/W
        #return n
        hand.sort()
        for i in range(0,n):
            x = hand[0]
            del hand[0]
            for j in range(1,W):
                x += 1
                if x not in hand:
                    return False
                else:
                    del hand[hand.index(x)]
                
        return True
