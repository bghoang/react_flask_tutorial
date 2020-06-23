Simple webapp with React and Flask
Following tutorial from these 2 links: https://www.youtube.com/watch?v=Urx8Kj00zsI and https://www.youtube.com/watch?v=06pWsB_hoD4

Install virtualenv and do flask run to run api.
cd into frontend folder and do npm start to run react app. (might need to do npm install before running the app)

Note:
- Run react app app before running flask server.
- Might need to add this line: "proxy": "http://localhost:5000/" to the end of package.json to fix cors issue.