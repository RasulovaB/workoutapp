if(document.readyState == "loading"){
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready()
}

function ready(){
    var removeMuscleButtons = document.getElementsByClassName('remove-button')
    console.log(removeMuscleButtons)
    for(var i = 0; i < removeMuscleButtons.length; i++){
        var button = removeMuscleButtons[i]
        button.addEventListener('click', removeMuscle)
    }

    var addToWorkoutButton = document.getElementById('selected-muscle')
            console.log(addToWorkoutButton.innerText)
            addToWorkoutButton.addEventListener('click', addToCartClicked)
        
    
    
}

function removeMuscle(event){
    var buttonClicked = event.target
    console.log(buttonClicked.innerText)
    buttonClicked.parentElement.remove()
    document.getElementById('total-muscles').innerText = document.getElementsByClassName('remove-button').length
}

function addToCartClicked(event){
    var button = event.target
    var title = button.innerText
    console.log(title)
    addMuscleToCart(title)
}

function addMuscleToCart(title){
    var button = document.createElement('button')
    button.classList.add('btn')
    button.classList.add('image-toggle')
    button.classList.add('btn-block')
    button.classList.add('add-button')
    button.classList.add('remove-button')
    var addedMuscles = document.getElementsByClassName('selected-muscles')[0]
    buttonContents = `<button class="btn image-toggle btn-block add-button remove-button"><i class="fa fa-minus button-icon"></i>${title}</button>`
    button.innerHTML = buttonContents
    addedMuscles.append(button)
    document.getElementById('total-muscles').innerText = document.getElementsByClassName('selected-muscles').length
}

function check_value(string){
    switch(string){
       case "chest":
         document.getElementById("human-fig").innerHTML = "<img src='static/chest.png' class='image-toggle'>";
         document.getElementById("selected-muscle").innerHTML = '<button class="btn image-toggle btn-block add-button"><i class="fa fa-plus button-icon"></i>Chest</button>'
         break;
       case "back":
          document.getElementById("human-fig").innerHTML = "<img src='static/back.png' class='image-toggle'>";
          document.getElementById("selected-muscle").innerHTML = '<button class="btn image-toggle btn-block add-button"><i class="fa fa-plus button-icon"></i>Back</button>'
          break;
       case "arms":
          document.getElementById("human-fig").innerHTML = "<img src='static/arms.png' class='image-toggle'>";
          document.getElementById("selected-muscle").innerHTML = '<button class="btn image-toggle btn-block add-button"><i class="fa fa-plus button-icon"></i>Arms</button>'
          break;
      case "abs":
          document.getElementById("human-fig").innerHTML = "<img src='static/abs.png' class='image-toggle'>";
          document.getElementById("selected-muscle").innerHTML = '<button class="btn image-toggle btn-block add-button"><i class="fa fa-plus button-icon"></i>Abs</button>'
          break;
      case "legs":
          document.getElementById("human-fig").innerHTML = "<img src='static/legs.png' class='image-toggle'>";
          document.getElementById("selected-muscle").innerHTML = '<button class="btn image-toggle btn-block add-button"><i class="fa fa-plus button-icon"></i>Legs</button>'
          break;
      case "shoulders":
          document.getElementById("human-fig").innerHTML = "<img src='static/shoulders.png' class='image-toggle'>";
          document.getElementById("selected-muscle").innerHTML = '<button class="btn image-toggle btn-block add-button"><i class="fa fa-plus button-icon"></i>Shoulders</button>'
          break;
      default:
          document.getElementById("human-fig").innerHTML = "<img src='static/default-human-fig.png' class='image-toggle'>";
          break; 
    }
  }