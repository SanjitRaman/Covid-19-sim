to add an origin
git add origin https://github.com/SanjitRaman/Covid-19-sim.git

I pull the latest code using:
git pull --rebase
Then I can make changes on Visual Studio Code, as I please.

When I want to add them to the staging (preparation) area on my local computer:
git add <filename> or git add . to add all changes.

When I want to commit them to the timeline,
git commit -m "Enter a commit message"

To upload the changes back to github:
git push -u origin master