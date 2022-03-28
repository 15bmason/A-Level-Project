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

$('.flip-card .flip-card-inner').click(function() {
  $(this).closest('.flip-card').toggleClass('hover');
  $(this).css('transform, rotateY(180deg)');
});

const setTheme = theme => document.documentElement.className = theme;

if ( window.history.replaceState ) {
  window.history.replaceState( null, null, window.location.href );
}

function myFunction() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");
}