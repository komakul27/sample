print("welocme")

git clone <repo-url>
cd practice_check/
echo "i am sai" > sai.txt
git add sai.txt
git commit -m "the file is added"
git checkout -b feature
git push origin feature
git checkout main
git pull origin main
