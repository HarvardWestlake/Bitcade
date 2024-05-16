// leaderboard.js
document.addEventListener('DOMContentLoaded', () => {
    console.log("DOM fully loaded and parsed");

    const users = [
        { username: 'Alice', score: 85 },
        { username: 'Bob', score: 92 },
        { username: 'Charlie', score: 88 },
        { username: 'Dave', score: 75 },
        { username: 'Eve', score: 95 }
    ];

    // Sort users by score in descending order
    users.sort((a, b) => b.score - a.score);
    console.log("Users sorted:", users);

    // Get the top 3 users
    const topThree = users.slice(0, 3);
    console.log("Top 3 users:", topThree);

    // Display the top 3 users
    const topThreeList = document.getElementById('top-three-list');
    if (topThreeList) {
        topThree.forEach(user => {
            const listItem = document.createElement('li');
            listItem.textContent = `${user.username}: ${user.score}`;
            topThreeList.appendChild(listItem);
        });
    } else {
        console.error("Element with id 'top-three-list' not found");
    }

    // Display all users
    const allUsersList = document.getElementById('all-users-list');
    if (allUsersList) {
        users.forEach(user => {
            const listItem = document.createElement('li');
            listItem.textContent = `${user.username}: ${user.score}`;
            allUsersList.appendChild(listItem);
        });
    } else {
        console.error("Element with id 'all-users-list' not found");
    }
});
