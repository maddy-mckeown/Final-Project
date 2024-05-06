// import { WORDS } from "./words.js";

const NUMBER_OF_GUESSES = 6;
let guessesRemaining = NUMBER_OF_GUESSES;
let currentGuess = [];
let nextLetter = 0;

// Get words by making fetch request to server => ajax call
//fetch('/url-where-you-query-your-database-for-words').then()
// create a route on the server => Word.query.all() => doing that query on the server
// once we get response from our server, then we create the game board

document.addEventListener("keyup", (e) => {

    if (guessesRemaining === 0) {
        return
    }

    let pressedKey = String(e.key)
    if (pressedKey === "Backspace" && nextLetter !== 0) {
        deleteLetter()
        return
    }

    if (pressedKey === "Enter") {
        checkGuess()
        return
    }

    let found = pressedKey.match(/[a-z]/gi)
    if (!found || found.length > 1) {
        return
    } else {
        insertLetter(pressedKey)
    }
})

// let rightGuessString = WORDS[Math.floor(Math.random() * WORDS.length)]
// console.log(rightGuessString)

function initBoard() {
    let board = document.getElementById("key-board");

    for (let i = 0; i < NUMBER_OF_GUESSES; i++) {
        let row = document.createElement("div")
        row.className = "letter-row"
        
        for (let j = 0; j < 5; j++) {
            let box = document.createElement("div")
            box.className = "letter-box"
            row.appendChild(box)
        }

        board.appendChild(row)
    }
}
function getWord() {
    let rand_word = document.querySelector('#random-word').value 
//     fetch("/words.json")

//   .then((response) => {
//     return response.json();
//   })
//   .then((responseData) => {
//     document.querySelector('#key-board').innerText = responseData;
//     console.log(responseData)
//   });

}

initBoard()

function insertLetter() {
    //need to iterate over letters? loop? helppppp
}


// create a function to check guessed word
    // check if the letter inputs match the random word
    // grab onto the "letter-1", "letter-2" values
    // check if each letter matches the letter in random word

function checkWord(evt) {
    evt.preventDefault();
    let random_word = document.querySelector('#random-word').value;
    // evt => form event, which includes the input values
    // console.log(evt);
    // console.log(evt.target[0].value);
    // These are the user's guessed letters
    let firstLetter = evt.target[0].value; //this is grabbing onto the data in the first input field
    let secondLetter = evt.target[1].value; 
    let thirdLetter = evt.target[2].value;
    let fourthLetter = evt.target[3].value;
    let fifthLetter = evt.target[4].value;
    // "e", "a", "r", "t", "h" => this is the user's guess
    // word is something like "musty"
    // assume user's guess is correct,
    // look at each letter and if it's not the same, then user's guess is incorrect
    let userGuessCorrect = true;
    if (random_word[0] != firstLetter) {
        userGuessCorrect = false;
    }
    if (random_word[1] != secondLetter) {
        userGuessCorrect = false;
    }
    if (random_word[2] != thirdLetter) {
        userGuessCorrect = false;
    }
    if (random_word[3] != fourthLetter) {
        userGuessCorrect = false;
    }
    if (random_word[4] != fifthLetter) {
        userGuessCorrect = false;
    }

    // TODO - how to show users their guesses?
    alert(userGuessCorrect);
}

// add event listeners to the forms
let formGuess1 = document.querySelector('#guess-1');
formGuess1.addEventListener('submit', checkWord);
// TODO - this is where to addEventListeners
let formGuess2 = document.querySelector('#guess-2');
formGuess2.addEventListener('submit', checkWord);



