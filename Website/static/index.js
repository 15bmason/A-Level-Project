function deleteCard(cardId) {
  let url_str = window.location.href;
  let  url = new URL(url_str);
  let search_params = url.searchParams;
  fetch("/delete-card", {
    method: "POST",
    body: JSON.stringify({ cardId: cardId }),
    }).then((_res) => {
      let id = search_params.get('id');
      window.location.href = ("/cards" + "?id=" + id);
    });
  }  

function deleteCardset(cardId) {
  fetch("/delete-cardset", {
    method: "POST",
    body: JSON.stringify({ cardId: cardId }),
  }).then((_res) => {
    window.location.href = "/cardset";
  });
}

function show_pwd(){
    var password = document.getElementById("password");
  if (password.type === "password") {
    password.type = "text";
  } else {
    password.type = "password";
  }
}

function show_pwd_signup(){
    var password = document.getElementById("password1");
    var confirmed_password = document.getElementById("password2");
    if(y.type === "password"){
      password.type = "text";
      confirmed_password.type = "text";
    } else {
      password.type = "password";
      confirmed_password.type = "password";
    }
  }

$('.flip-card .flip-card-inner').click(function() {
  $(this).closest('.flip-card').toggleClass('hover');
  $(this).css('transform, rotateY(180deg)');
});

const setTheme = theme => document.documentElement.className = theme;

if ( window.history.replaceState ) {
  window.history.replaceState( null, null, window.location.href );
}

const btn = document.querySelector(".btn-toggle");
const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");

const currentTheme = localStorage.getItem("theme");
if (currentTheme == "dark") {
  document.body.classList.toggle("dark-theme");
} else if (currentTheme == "light") {
  document.body.classList.toggle("light-theme");
}
window.onload=function(){
  btn.addEventListener("click", function () {
    if (prefersDarkScheme.matches) {
      document.body.classList.toggle("light-theme");
      var theme = document.body.classList.contains("light-theme")
        ? "light"
        : "dark";
    } else {
      document.body.classList.toggle("dark-theme");
      var theme = document.body.classList.contains("dark-theme")
        ? "dark"
        : "light";
    }
    localStorage.setItem("theme", theme);
  });
}
$('.modal').on('show.bs.modal', function (e) {
  var $trigger = $(e.relatedTarget);
document.getElementById("card-id").value = $trigger.data('button');
let id = String($trigger.data('button'));
let index = id.slice(9);
let question = document.getElementById("question_text" + index).textContent;
let answer = document.getElementById("answer_text" + index).textContent;
document.getElementById("modal_question").innerHTML = question;
document.getElementById("modal_answer").innerHTML = answer;
});

console.log(document.getElementById("my_data"));