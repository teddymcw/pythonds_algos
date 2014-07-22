#!/usr/bin/env python

def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(change+1):
        print("begin calc coins for amount = {0}".format(cents))

        coinCount = cents
        currentCoinList = [c for c in coinValueList if c <= cents]
        print("current coin list: {0}".format(currentCoinList))

        for j in currentCoinList: #[c for c in coinValueList if c <= cents]:
            print("begin loop for coin denom: {0}".format(j))
            print("if use denom = {0} then best # of coins for remaining amount is {1}".format(j, minCoins[cents-j]))
            print("total coin count for this solution is: {0}".format(minCoins[cents-j]+ 1))

            if minCoins[cents-j] + 1 < coinCount:
                print("found fewer coin count than previous solution, update coin count to reflect better solution... ")
                print("existing coinCount = {0}".format(coinCount))
                coinCount = minCoins[cents-j] + 1
                print("coinCount now = {0}".format(coinCount))
            print(" ")

        print("reviewed all denoms ... update minCoin w/ best sol found ...")
        minCoins[cents] = coinCount
        print("updated minCoins, it is now: {0}".format(minCoins))
        print("----")

    return minCoins

if __name__ == "__main__":
    amount = 4
    coinList = [1, 5, 10, 25]
    coinCount = [0]*(amount+1)

    coinTable = dpMakeChange(coinList, amount, coinCount)

    print(coinTable)
    print("the min number of coin for {0} is {1}".format(amount,
        str(coinTable[amount])))