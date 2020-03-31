# Covid-19 SIR Simulation
# Date: 31.03.2020
# Version 1.0

# to add an origin
# git add origin https://github.com/SanjitRaman/Covid-19-sim.git

# I pull the latest code using:
# git pull --rebase
# Then I can make changes on Visual Studio Code, as I please.

# When I want to add them to the staging (preparation) area on my local computer:
# git add <filename> or git add . to add all changes.

# When I want to commit them to the timeline,
# git commit -m "Enter a commit message"

# To upload the changes back to github:
# git push -u origin master

#START OF PROGRAM

#ds/dt = -bSI/n
#di/dt = bsI/n-gI
#dr/dt = gI

def update(t):
    s += 2

def output():
    print("Susceptible: ")
    print("Infected: ")
    print("Recovered: ")

t = 0
n = 1000
s = 1000
i = 0
r = 0


while (True):
    update(t)
    output(data) # print out some information
    t +=1