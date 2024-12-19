/**
 * This algorithm performs a Breadth-First Search (BFS) on a graph to determine 
 * if there is a person whose name starts with the letter "M". It uses a queue 
 * to process connections level by level and ensures no person is checked more 
 * than once. If such a person is found, they are identified as a "mango seller".
 */

function search(name) {
    const searchQueue = []; // Queue to store people to be checked
    searchQueue.push(...graph[name]);
    const checked = []; // List to track already checked people

    while (searchQueue.length > 0) {
        const person = searchQueue.shift(); // Remove the first person from the queue
        if (!checked.includes(person)) { // Check if the person has already been verified
            if (isSeller(person)) {
                console.log(`${person} is a mango seller!`);
                return true;
            } else {
                searchQueue.push(...graph[person]); // Add this person's friends to the queue
                checked.push(person); // Add the person to the checked list
            }
        }

        if (searchQueue.length === 0) console.log('There is no mango seller!');
    }
    return false;
}

// Example of the graph structure
const graph = {
    you: ["alice", "bob", "claire"],
    alice: ["peggy"],
    bob: ["anuj", "peggy"],
    claire: ["thom", "jonny"],
    anuj: ["marcelo"],
    peggy: [],
    thom: [],
    jonny: []
};

// Function to check if the person is a seller
function isSeller(name) {
    return name[0] === "M".toLowerCase();
}

search("you");
