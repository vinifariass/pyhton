var firstName = prompt("First name?");
var lastName = prompt("Last name?");
var age = prompt("Age?");
var height = prompt("Height?");
var pet = prompt("Pet name?");
alert("Thank you so much " + firstName + " " + lastName + "! We appreciate your information.");

//LOGIC

// NAME CONDITION

if (firstName[0] === lastName[0]) {
    nameCond = "true";
} else {
    nameCond = "false";
}

// AGE CONDITION

if (age > 20 && age < 30) {
    ageCond = "true";
} else {
    ageCond = "false";
}   

// PET CONDITION

if (pet.charAt(pet.length - 1) === "y") {
    petCond = "true";
} else {
    petCond = "false";
}

// HEIGHT CONDITION

if (height >= 170) {
    heightCond = "true";
} else {
    heightCond = "false";
}

// FOUR CONDITIONS

if (nameCond === "true" && ageCond === "true" && petCond === "true" && heightCond === "true") {
    alert("Welcome Spy!");
} else {
    alert("Nothing to see here!");
}


var headOne = document.querySelector("#one");
headOne.addEventListener("click", function() {
    headOne.style.color = "red";
});
headOne.addEventListener("dblclick", function() {
    headOne.style.color = "blue";
});
headOne.addEventListener("mouseover", function() {
    headOne.style.color = "green";
});


headTwo.addEventListener("mouseout", function() {
    headTwo.style.color = "black";
});

headTwo.addEventListener("dblclick", function() {
    headTwo.style.color = "red";
});