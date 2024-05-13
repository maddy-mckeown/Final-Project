// import { WORDS } from "./words.js";

const NUMBER_OF_GUESSES = 5;
// let guessesRemaining = NUMBER_OF_GUESSES;
let currentGuess = [];
let nextLetter = 0;

let guessesRemaining = 5;

// Get words by making fetch request to server => ajax call
//fetch('/url-where-you-query-your-database-for-words').then()
// create a route on the server => Word.query.all() => doing that query on the server
// once we get response from our server, then we create the game board

document.addEventListener("keyup", (e) => {

    // if (guessesRemaining === 0) {
    //     return
    // }

    let pressedKey = String(e.key)
    // if (pressedKey === "Backspace" && nextLetter !== 0) {
    //     deleteLetter()
    //     return
    // }

    if (pressedKey === "Enter") {
        // TODO ?? - make it so that when user presses enter key, their guess is submitted
        // checkGuess()
        // checkWord??
        // return
    }

    // let found = pressedKey.match(/[a-z]/gi)
    // if (!found || found.length > 1) {
    //     return
    // } else {
    //     insertLetter(pressedKey)
    // }
})

// let rightGuessString = WORDS[Math.floor(Math.random() * WORDS.length)]
// console.log(rightGuessString)

// function initBoard() {
//     let board = document.getElementById("key-board");

//     for (let i = 0; i < NUMBER_OF_GUESSES; i++) {
//         let row = document.createElement("div")
//         row.className = "letter-row"
        
//         for (let j = 0; j < 5; j++) {
//             let box = document.createElement("div")
//             box.className = "letter-box"
//             row.appendChild(box)
//         }

//         board.appendChild(row)
//     }
// }
// function getWord() {
    // let rand_word = document.querySelector('#random-word').value; 
//     fetch("/words.json")

//   .then((response) => {
//     return response.json();
//   })
//   .then((responseData) => {
//     document.querySelector('#key-board').innerText = responseData;
//     console.log(responseData)
//   });
// }

// initBoard()

function winGame(is_win) {
    const winInfo = {
        is_win: is_win,
        num_guesses: guessesRemaining,
    };

    fetch('/scores', {
        method:'POST',
        body: JSON.stringify(winInfo),
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then((response)=> response.json())
    .then((responseJson) => {
        // start a new game => redirect the user to the game page again
        console.log(responseJson.success);
        // redirect them back to game page to play another round
        window.location.href = "/game";
    });
}
    // if is_win is true, the user won => do this
        // make fetch request to the server, passing in num guesses and is_win
        // make sure the database knows they go it right
    // else if is_win is false the user lost => do something else
    // either way we are giving them the option of a new game



function insertLetter() {
    //need to iterate over letters? loop? helppppp
}


// create a function to check guessed word
    // check if the letter inputs match the random word
    // grab onto the "letter-1", "letter-2" values
    // check if each letter matches the letter in random word

function checkWord(evt) {
    evt.preventDefault();
    console.log(evt.target.id); // in theory should have the id of the form
    // console.log(evt.submitter); // <button>? <form element>
    let random_word = document.querySelector('#random-word').value;
    // evt => form event, which includes the input values
    // console.log(evt);
    // console.log(random_word);
    // These are the user's guessed letters
    let firstLetter = evt.target[0].value; //this is grabbing onto the data in the first input field
    let secondLetter = evt.target[1].value; 
    let thirdLetter = evt.target[2].value;
    let fourthLetter = evt.target[3].value;
    let fifthLetter = evt.target[4].value;
    // "e", "a", "r", "t", "h" => this is the user's guess
    // word is something like "musty"
    // word is "mouse"
    // assume user's guess is correct,
    // look at each letter and if it's not the same, then user's guess is incorrect
    let userGuessCorrect = true;
    if (random_word[0] != firstLetter) {
        userGuessCorrect = false;
        // if letter not in right position, then check if letter found in word at all?
        if (random_word.includes(firstLetter)) {
            // change color of evt.target[0] to green
            evt.target[0].style.backgroundColor = 'green';
            // shouldn't be able to edit previous guess
            // evt.target[0].disabled = true;
        } else {
            evt.target[0].style.backgroundColor = 'grey';
        }
    } else if (random_word[0] === firstLetter) {
        evt.target[0].style.backgroundColor = 'pink';
    }


    if (random_word[1] != secondLetter) {
        userGuessCorrect = false;
        if (random_word.includes(secondLetter)) {
            // change color of evt.target[1] to grey/black
            evt.target[1].style.backgroundColor = 'green';
            // evt.target[1].disabled = true;
        } else {
            evt.target[1].style.backgroundColor = 'grey';
        }
    } else if (random_word[1] === secondLetter) {
        evt.target[1].style.backgroundColor = 'pink';
    }


    if (random_word[2] != thirdLetter) {
        userGuessCorrect = false;
        if (random_word.includes(thirdLetter)) {
            // change color of evt.target[2] to grey/black
            evt.target[2].style.backgroundColor = 'green';
            // evt.target[2].disabled = true;
        } else {
            evt.target[2].style.backgroundColor = 'grey';
        }
    } else if (random_word[2] === thirdLetter) {
        evt.target[2].style.backgroundColor = 'pink';
    }

    if (random_word[3] != fourthLetter) {
        userGuessCorrect = false;
        if (random_word.includes(fourthLetter)) {
            // change color of evt.target[3] to grey/black
            evt.target[3].style.backgroundColor = 'green';
            // evt.target[3].disabled = true;
        } else {
            evt.target[3].style.backgroundColor = 'grey';
        }
    } else if (random_word[3] === fourthLetter) {
        evt.target[3].style.backgroundColor = 'pink';
    }

    if (random_word[4] != fifthLetter) {
        userGuessCorrect = false;
        if (random_word.includes(fifthLetter)) {
            // change color of evt.target[4] to grey/black
            evt.target[4].style.backgroundColor = 'green';
            // evt.target[4].disabled = true;
        } else {
            evt.target[4].style.backgroundColor = 'grey';
        }
    } else if (random_word[4] === fifthLetter) {
        evt.target[4].style.backgroundColor = 'pink';
    }

    // all the inputs won't be editable
    evt.target[0].disabled = true;
    evt.target[1].disabled = true;
    evt.target[2].disabled = true;
    evt.target[3].disabled = true;
    evt.target[4].disabled = true;
    // hide this form's submit button
    // submit button hiding
    evt.submitter.style.display = 'none';
    // show next form's submit button

   
    if (userGuessCorrect) {
        alert("Congratulations! You have increased your score!");
        winGame(true);
    }
    else {
        guessesRemaining -= 1;
        if (guessesRemaining <= 0) {
            alert("Oh no! Would you like to play another round?");
            winGame(false);
        }
    }

        // then call function that will pop up message about user winning and end game
        // maybe ask user if they want to play another round

}



    // increment guess counter, move user to next form
    // TODO - how to show users their guesses?

    // when the user submits their guess, we want to indicate which letters are correct/not in the right spot
    // when the letter is in the right spot, change the input backgroundColor to pink
    // letter in the wrong spot turns backgroundColor black
    // letter not in word does nothing
    // alert(userGuessCorrect);


// add event listeners to the forms
let formGuess1 = document.querySelector('#guess-1');
formGuess1.addEventListener('submit', checkWord);
// TODO - this is where to addEventListeners
let formGuess2 = document.querySelector('#guess-2');
formGuess2.addEventListener('submit', checkWord);

let formGuess3 = document.querySelector('#guess-3');
formGuess3.addEventListener('submit', checkWord);

let formGuess4 = document.querySelector('#guess-4');
formGuess4.addEventListener('submit', checkWord);

let formGuess5 = document.querySelector('#guess-5');
formGuess5.addEventListener('submit', checkWord);

// a way for the user to type and then have it only read/submit that info
// hiding and unhiding the submit buttons
// if that works, then style the buttons so they're towards the bottom of the card