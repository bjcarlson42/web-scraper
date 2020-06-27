var jcontent = {
    'firstName': 'Ben',
    "likes": "18"
}

var firstname = document.getElementById('firstname');
var likes = document.getElementById('likes');

firstname.innerHTML = jcontent.firstName;
likes.innerHTML = jcontent.likes;