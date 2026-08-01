function helloWorld() {
    console.log("Hello World");
}

function remove() {

    var remName = prompt("What name you want to remove?");
    var index = ResizeObserverEntry.indexOf(remName);
    roster.splice(index, 1);
}

// Create a function called display that displays the roster in the console.
function display() {
    console.log(roster);
}

//Start by askiong if they want to use the web app
var useApp = prompt("Do you want to use the web app?");
if (useApp === "yes") {
    var action = prompt("What do you want to do?");
    if (action === "add") {
        add();
    } else if (action === "remove") {
        remove();
    } else if (action === "display") {
        display();
    }
} else {
    console.log("Thank you for using the web app!");
}