console.log("Connected");

//Restart Button
var restart = document.querySelector("#restart");
restart.addEventListener("click", restartGame);
function restartGame() {
    console.log("Restart button clicked");
}

//Grabs all squares
var squares = document.querySelectorAll("td");
// Clear all squares
function clearBoard() {
    for (var i = 0; i < squares.length; i++) {
        squares[i].textContent = "";
    }
}
restart.addEventListener("click", clearBoard);
// Check the square markers
var cellOne =document.querySelector("#one");


function changeMarker() {
    if(this.textContent === "") {
        this.textContent = "X";
    } else if(this.textContent === "X") {
        this.textContent = "O";
    } else {
        this.textContent = "";
    }
}
for (var i = 0; i < squares.length; i++) {
    squares[i].addEventListener("click", changeMarker);
}
// For loop to add event listeners to all squares
