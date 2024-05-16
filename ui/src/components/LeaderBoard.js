// Create and append the leaderboard container
const leaderboardContainer = document.createElement('div');
leaderboardContainer.className = 'leaderboard';
document.body.appendChild(leaderboardContainer);

// Create and append the top three users section
const topThreeSection = document.createElement('div');
topThreeSection.className = 'top-three';
const topThreeHeading = document.createElement('h2');
topThreeHeading.textContent = 'Top 3 Users';
topThreeSection.appendChild(topThreeHeading);
const topThreeList = document.createElement('ul');
topThreeList.id = 'top-three-list';
topThreeSection.appendChild(topThreeList);
leaderboardContainer.appendChild(topThreeSection);

// Create and append the extended list section
const extendedListSection = document.createElement('div');
extendedListSection.className = 'extended-list';
const extendedListHeading = document.createElement('h3');
extendedListHeading.textContent = 'All Users';
extendedListSection.appendChild(extendedListHeading);
const allUsersList = document.createElement('ul');
allUsersList.id = 'all-users-list';
extendedListSection.appendChild(allUsersList);
leaderboardContainer.appendChild(extendedListSection);

// Add styles using JavaScript
const styles = `
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}
.leaderboard {
    width: 300px;
    margin: 50px auto;
    text-align: center;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.top-three {
    font-size: 1.5em;
}
.extended-list {
    margin-top: 20px;
}
`;
const styleSheet = document.createElement('style');
styleSheet.type = 'text/css';
styleSheet.innerText = styles;
document.head.appendChild(styleSheet);

// Function to populate the leaderboard
function populateLeaderboard(users) {
    // Sort users by score in descending order
    users.sort((a, b) => b.score - a.score);

    // Get the top 3 users
    const topThree = users.slice(0, 3);

    // Display the top 3 users
    const topThreeList = document.getElementById('top-three-list');
    topThree.forEach(user => {
        const listItem = document.createElement('li');
        listItem.textContent = `${user.username}: ${user.score}`;
        topThreeList.appendChild(listItem);
    });

    // Display all users
    const allUsersList = document.getElementById('all-users-list');
    users.forEach(user => {
        const listItem = document.createElement('li');
        listItem.textContent = `${user.username}: ${user.score}`;
        allUsersList.appendChild(listItem);
    });
}

// Example users data
const users = [
    { username: 'Alice', score: 85 },
    { username: 'Bob', score: 92 },
    { username: 'Charlie', score: 88 },
    { username: 'Dave', score: 75 },
    { username: 'Eve', score: 95 }
];

// Populate the leaderboard with example data
populateLeaderboard(users);
