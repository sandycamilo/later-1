function bookSearch(e){
  e.preventDefault()
  console.log('this function runs');
  // location.href="{% url 'book-detail' object.id %}"
  // var a = "{{ object.book_title }}";
  // console.log('a', a);
  // var search = 'Becoming';
  var search = document.getElementById('id_book_title_or_author_name').value;
  document.getElementById('results').innerHTML = "";

  $.ajax({
    url: "https://www.googleapis.com/books/v1/volumes?q=" + search,
    dataType: "json",
    type:'GET',
    success: function(data) {

      for(i=0; i<data.items.length; i++) {

        results.innerHTML += "<h2>" + "Title: " + data.items[i].volumeInfo.title + "</h2>";
        results.innerHTML += "<h2>" + "Authors: " + data.items[i].volumeInfo.authors + "</h2>";
        results.innerHTML += "<img src=" + data.items[i].volumeInfo.imageLinks.thumbnail + "/>";
        results.innerHTML += "<h2>" + "Published Date: " + data.items[i].volumeInfo.publishedDate + "</h2>";
        results.innerHTML += "<h2>" + "Publisher: " + data.items[i].volumeInfo.publisher + "</h2>";
        results.innerHTML += "<h2>" + "Description: " + data.items[i].volumeInfo.description + "</h2>";
        // creating a button
        results.innerHTML += "<button type='button' onclick='selectBook(\"" + data.items[i].volumeInfo.title + "\")'>Add</button>";


      }
    }
  });

}

document.getElementById('save-btn').addEventListener("click", bookSearch)

function selectBook(title) {
  console.log("Hello World");
  console.log("accepting data");
  console.log(title);

  function getCookie(name) {

  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
  }

  var csrftoken = getCookie('csrftoken');
  var jsonString = JSON.stringify(title);
  var xhttp = new XMLHttpRequest();
  xhttp.open("POST", "/listApp/new/", true);
  xhttp.responseType = "json";
  xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhttp.setRequestHeader("X-CSRFToken", csrftoken);
  xhttp.send(jsonString);
}