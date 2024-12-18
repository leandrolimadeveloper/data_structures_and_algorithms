// Word Frequency Counter Using a Hash Table in JS

function wordCount(text) {
    // Create a hash table (object) to store the word frequency
    const hashTable = {};

    // Preprocess the text: convert to lowercase, remove simple punctuation, and split into words
    const words = text
        .toLowerCase()
        .replace(/[.,]/g, '') // Remove commas and periods
        .split(' ');

    // Count the frequency of each word
    for (const word of words) {
        if (hashTable[word]) {
            hashTable[word] += 1; // Increment the count if the word already exists
        } else {
            hashTable[word] = 1; // Initialize the count to 1
        }
    }

    return hashTable;
}

// Informative text about JavaScript
const exampleText = `
JavaScript is a programming language widely used for web development.
It allows adding interactivity and dynamism to HTML pages. JavaScript is executed
directly in the user's browser and can manipulate the DOM, validate forms, and perform
asynchronous requests with APIs using AJAX or Fetch. 

Today, JavaScript is one of the most popular programming languages in the world. 
Beyond the client side, JavaScript is also widely used on the server side through Node.js. 
Node.js allows developers to run JavaScript outside the browser, enabling backend development, 
file handling, and real-time applications like chat systems. With frameworks such as Express.js, 
it is possible to create RESTful APIs, manage databases, and build scalable applications. 

JavaScript's versatility makes it a key language for full-stack development, 
allowing developers to use the same language for both frontend and backend development.
`;

// Call the function to count words in the text
const result = wordCount(exampleText);

// Display the result sorted by words
console.log("Word frequency in the informative JavaScript text:");

Object.keys(result)
    .sort()
    .forEach(word => {
        console.log(`${word}: ${result[word]}`);
    });
