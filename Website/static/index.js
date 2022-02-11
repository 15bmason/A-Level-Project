function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }

function show_pwd(){
    var x = document.getElementById("password");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

function show_pwd_signup(){
    var x = document.getElementById("password1");
    var y = document.getElementById("password2");
    if(y.type === "password"){
      x.type = "text";
      y.type = "text";
    } else {
      x.type = "password";
      y.type = "password";
    }
  }

function number_shown(){
  var x = document.getElementById("")
  window.location.href("/")
}

function check_rot_lock(){
  var flashcard = document.getElementById("flip-card:hover");
  var checkbox = document.getElementById("rot-lock");
  const checked_style= {
    transform: rotateY(0)
  }
  if(checkbox.checked == true){
    Object.assign(flashcard.style, checked_style);
  }
}

const setTheme = theme => document.documentElement.className = theme;