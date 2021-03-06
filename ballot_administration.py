from political_parties import *
from territorial_distribution import *


#This method allows the admin to add a new ballot into a district
def addBallot():
    prov = input("Province name: ")
    can = input("Canton name: ")
    dis = input("District where you want this ballot: ")
    type = input("Legislative or Presidential?(p/l): ")
    votes = 0
    parties = []
    for party in partiesList:
        partySpecs = {"name": party["name"], "votes": votes}
        parties.append(partySpecs)

    f = False
    if type == "l":
        for p in provinces:
            if prov == p["name"]:
                cantons = p["cantons"]
                for c in cantons:
                    if can == c["name"]:
                        districts = c["districts"]
                        for d in districts:
                            if dis == d["name"]:
                                ballotListl = d["lBallot"]
                                ballotParties = []
                                i = 0
                                while i < len(parties):
                                    party = input("Name of the party you want to add: ")
                                    if party == parties[i]["name"]:
                                        ballotParties.append(parties[i])
                                        yn = input("Want to add another party?(Y/n): ")
                                        if yn == "Y" or yn == "y":
                                            i = 0
                                        else:
                                            if len(ballotListl) == 0:
                                                ballot = {"province": prov, "canton": can, "district": dis,
                                                          "type": type, "parties": ballotParties}
                                                ballotListl.append(ballot)
                                                f = True
                                                break
                                            else:
                                                print("That district already has a legislative ballot... Check it out")
                                    i += 1


    elif type == "p":
        for p in provinces:
            if prov == p["name"]:
                cantons = p["cantons"]
                for c in cantons:
                    if can == c["name"]:
                        districts = c["districts"]
                        for d in districts:
                            if dis == d["name"]:
                                ballotListp = d["pBallot"]
                                ballotParties = []
                                i = 0
                                while i < len(parties):
                                    party = input("Name of the party you want to add: ")
                                    if party == parties[i]["name"]:
                                        ballotParties.append(parties[i])
                                        yn = input("Want to add another party?(Y/n): ")
                                        if yn == "Y" or yn == "y":
                                            i = 0
                                        else:
                                            if len(ballotListp) == 0:
                                                ballot = {"province": prov, "canton": can, "district": dis,
                                                          "type": type, "parties": ballotParties}
                                                ballotListp.append(ballot)
                                                f = True
                                                break
                                            else:
                                                print("That district already has a presidential ballot... Check it out")
                                    i += 1


    if f == False:
        print("Something went wrong...\n")

    print(provinces)
    return True

#This method allows the admin to edit a ballot(add or delete a party in an existent ballot)
def editBallot():
    prov = input("Province name: ")
    can = input("Canton name: ")
    dis = input("District name: ")
    type = input("Legislative or Presidential?(p/l): ")
    a_d = input("Do you want to add or delete a party?(a/d): ")
    votes = 0

    listParties = []
    for party in partiesList:
        partySpecs = {"name": party["name"], "votes": votes}
        listParties.append(partySpecs)

    f = False
    if type == "l":
        if a_d == "a":
            for p in provinces:
                if prov == p["name"]:
                    cantons = p["cantons"]
                    for c in cantons:
                        if can == c["name"]:
                            districts = c["districts"]
                            for d in districts:
                                if dis == d["name"]:
                                    lballot = d["lBallot"]
                                    parties = lballot[0]["parties"]
                                    party = input("New party: ")
                                    i = 0
                                    while i < len(listParties):
                                        if party == listParties[i]["name"]:
                                            j = 0
                                            while j < len(parties):
                                                if party != parties[j]["name"]:
                                                    parties.append(listParties[i])
                                                    f = True
                                                j += 1
                                        i += 1
        elif a_d == "d":
            for p in provinces:
                if prov == p["name"]:
                    cantons = p["cantons"]
                    for c in cantons:
                        if can == c["name"]:
                            districts = c["districts"]
                            for d in districts:
                                if dis == d["name"]:
                                    lballot = d["lBallot"]
                                    parties = lballot[0]["parties"]
                                    party = input("Party you want to delete: ")
                                    i = 0
                                    while i < len(parties):
                                        if party == parties[i]["name"]:
                                            parties.remove(parties[i])
                                            f = True
                                        i += 1
    elif type == "p":
        if a_d == "a":
            for p in provinces:
                if prov == p["name"]:
                    cantons = p["cantons"]
                    for c in cantons:
                        if can == c["name"]:
                            districts = c["districts"]
                            for d in districts:
                                if dis == d["name"]:
                                    pballot = d["pBallot"]
                                    parties = pballot[0]["parties"]
                                    party = input("New party: ")
                                    i = 0
                                    while i < len(listParties):
                                        if party == listParties[i]["name"]:
                                            j = 0
                                            while j < len(parties):
                                                if party != parties[j]["name"]:
                                                    parties.append(listParties[i])
                                                    f = True
                                                j += 1
                                        i += 1
        elif a_d == "d":
            for p in provinces:
                if prov == p["name"]:
                    cantons = p["cantons"]
                    for c in cantons:
                        if can == c["name"]:
                            districts = c["districts"]
                            for d in districts:
                                if dis == d["name"]:
                                    pballot = d["pBallot"]
                                    parties = pballot[0]["parties"]
                                    party = input("Party you want to delete: ")
                                    i = 0
                                    while i < len(parties):
                                        if party == parties[i]["name"]:
                                            parties.remove(parties[i])
                                            f = True
                                        i += 1


    if f == False:
        print("Something went wrong...\n")
    return True

#This method allows the admin to delete a ballot from a district
def deleteBallot():
    prov = input("Province name: ")
    can = input("Canton name: ")
    dis = input("Disctrict where you want this ballot: ")
    type = input("Legislative or Presidential?(p/l): ")

    f = False
    if type == "l":
        for p in provinces:
            if prov == p["name"]:
                cantons = p["cantons"]
                for c in cantons:
                    if can == c["name"]:
                        districts = c["districts"]
                        for d in districts:
                            if dis == d["name"]:
                                d["lBallot"] = []
                                f = True
    elif type == "p":
        for p in provinces:
            if prov == p["name"]:
                cantons = p["cantons"]
                for c in cantons:
                    if can == c["name"]:
                        districts = c["districts"]
                        for d in districts:
                            if dis == d["name"]:
                                d["pBallot"] = []
                                f = True


    if f == False:
        print("Something went wrong...\n")
    return True
