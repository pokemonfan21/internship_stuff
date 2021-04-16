// Create an array for the buttons and sounds. There will be 16 of each, for a 4x4 drum machine.
var buttons = [];
var sounds = [];

let buttonSize = 30;
let notePlaying = 0;

function preload() {
  // Import in the Sounds before any thing else is set up. Upload the sounds into Glitch first, then get the URL.
  // TO DO: REPLACE OUT THE BELOW SOUNDS WITH YOUR OWN.
  sounds.push(loadSound("https://cdn.glitch.com/73626ac0-479e-4f6c-93ee-e5b8bcd9448e%2Fthum.wav?v=1597959292494"));
  sounds.push(loadSound("https://cdn.glitch.com/73626ac0-479e-4f6c-93ee-e5b8bcd9448e%2Fchime1.wav?v=1597958441794"));
  sounds.push(loadSound("https://cdn.glitch.com/73626ac0-479e-4f6c-93ee-e5b8bcd9448e%2Fcrash1.wav?v=1597959278997"));
  sounds.push(loadSound("https://cdn.glitch.com/73626ac0-479e-4f6c-93ee-e5b8bcd9448e%2Fsmall1.wav?v=1597959287505"));
  sounds.push(loadSound("https://cdn.glitch.com/73626ac0-479e-4f6c-93ee-e5b8bcd9448e%2Fsmall1.wav?v=1597959287505"));
  sounds.push(loadSound("https://cdn.glitch.com/73626ac0-479e-4f6c-93ee-e5b8bcd9448e%2Fsnare1.wav?v=1597959282781"));
  sounds.push(loadSound("https://cdn.glitch.com/73626ac0-479e-4f6c-93ee-e5b8bcd9448e%2Fsnare2.wav?v=1597959270026"));
  sounds.push(loadSound("https://cdn.glitch.com/73626ac0-479e-4f6c-93ee-e5b8bcd9448e%2Fthum.wav?v=1597959292494"));
  sounds.push(loadSound("https://cdn.glitch.com/73626ac0-479e-4f6c-93ee-e5b8bcd9448e%2Fchime1.wav?v=1597958441794"));
  sounds.push(loadSound("https://cdn.glitch.com/73626ac0-479e-4f6c-93ee-e5b8bcd9448e%2Fcrash1.wav?v=1597959278997"));
  sounds.push(loadSound("https://cdn.glitch.com/73626ac0-479e-4f6c-93ee-e5b8bcd9448e%2Fsmall1.wav?v=1597959287505"));
  sounds.push(loadSound("https://cdn.glitch.com/73626ac0-479e-4f6c-93ee-e5b8bcd9448e%2Fsmall1.wav?v=1597959287505"));
  sounds.push(loadSound("https://cdn.glitch.com/73626ac0-479e-4f6c-93ee-e5b8bcd9448e%2Fsnare1.wav?v=1597959282781"));
  sounds.push(loadSound("https://cdn.glitch.com/73626ac0-479e-4f6c-93ee-e5b8bcd9448e%2Fsnare2.wav?v=1597959270026"));
  sounds.push(loadSound("https://cdn.glitch.com/73626ac0-479e-4f6c-93ee-e5b8bcd9448e%2Fthum.wav?v=1597959292494"));
  sounds.push(loadSound("https://cdn.glitch.com/73626ac0-479e-4f6c-93ee-e5b8bcd9448e%2Fchime1.wav?v=1597958441794"));
}

function setup() {
  var myCanvas = createCanvas(400,400);
  myCanvas.parent("sketch-holder");
  
  // Create the grid of buttons. Button is a class object (below). The drum machine is a 4 x 4 grid, so we use nested for loops. 
  // The constructor for the button takes in the x, y, button size, and a sound.
  var soundIndex = 0;  // SoundIndex is how we increment through the sounds array we made earlier to get each sound.
  for (let y = 0; y < 4; y++) {
    for (let x = 0; x < 4; x++) {
      let button = new Button(      
        x * 90 + 50,
        y * 90 + 50,
        buttonSize,
        sounds[soundIndex]
      );
      soundIndex++;
      button.display();      // Call this new button's display() function.
      buttons.push(button);  // Add the button to the array of buttons.
    }
  }

  setInterval(playSounds, 500);  // setInterval calls the function playSounds() every 500 milliseconds, or 0.5 seconds. 
  // This is what causes the drum to play each consecutive note. 
}

function draw() {
  background(200, 0, 0);
  
  // Below draws all the buttons
  for (var i = 0; i < buttons.length; i++) {
    buttons[i].display();
  }
}

function mouseClicked() {
  // This for loop checks all the buttons to see if those button's coordinates match the mouse click's coordinates.
  for (let i = 0; i < buttons.length; i++) {
    buttons[i].clicked(mouseX, mouseY);   // mouseX and mouseY are the mouse x and mouse y coordinates of the click
  }
}

// This function plays the sounds of each column every 500 milliseconds (set in setInterval())
function playSounds() {
  for (let x = 0; x < 4; x++) {
    buttons[x * 4 + notePlaying].play();
  }
  notePlaying = notePlaying + 1; // notePlaying increases by one, so next time playSounds() is called, the next column of sounds is played
  if (notePlaying >= 4) {
    notePlaying = 0;
  }
}

// <-------------------------------- BUTTON CLASS -------------------------------->

// This button class contains information about each button, including the sound, color, size, whether it's clicked, and location
class Button {
  constructor(x, y, size, sound) {
    this.x = x;
    this.y = y;
    this.size = size;
    this.sound = sound;
    this.isClicked = false;
  }
  
  display() {
    if (this.isClicked) {
      fill(254, 74, 73);
    } else {
      fill(255, 195, 31);
    }
    strokeWeight(2);
    stroke(251, 255, 241);
    rect(this.x, this.y, this.size, this.size);
  }

  clicked(mX, mY) { // Called from the mouseClicked() function above.
    let d = dist(mX, mY, this.x, this.y);  // dist get's the distance between points. 
    if (d < this.size) {  // If the distance of the click and this square is less than the square size, initiate click.
      if (this.isClicked) {  // If it's clicked already, turn it off. 
        this.isClicked = false;
      } else {                // Otherwise if it's not clicked, play the sound and set it to true.
        this.sound.play();
        this.isClicked = true;
      }
    }
  }
  
  play() {   // Play the sound, called from playSounds() 
    if (this.isClicked == true) {
      this.sound.play();
    }
  }
}