
function grabJSON () {
  var obj = JSON.parse(json/newdata.json);

  document.getElementById("user").innerHTML =
  "Name: " + obj.articles.title;
}
