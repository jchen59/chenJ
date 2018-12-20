//Jiayang Chen, Jabir Chowdhury
//SoftDev1 pd7
//K29 -- Sequential Progression II: Electric Boogaloo...
//2018-12-19

var fibonacci = (n) => {
    var first = 0;
    var second = 1;
    for (i = 0; i < n; i++) {
	var temp = second;
	second += first;
	first = temp;
    }
    console.log(first);
    return first;
}

var gcd = (a,b) => {
    var max = 1;
    for (i = 1; i <= Math.min(a,b); i++) {
	if (a % i == 0 && b % i == 0) {
	    max = i;
	}
    }
    console.log(max);
    return max;
}


var randomStudent = () => {
    var names = ["Marcene Bradly", "Harold Bivens", "Jamel Degregorio", "Eunice Lastinger", "Loura Nickelson", "Ruthanne Oxford","Bret Goodpaster",  "Terri Fray",  "Sanford Feenstra",  "Stella Taber",  "Benito Hocutt",  "Katerine Bolenbaugh",  "Darrell Thorpe",  "Helga Wrona",  "Denny Bonet",  "Sumiko Hennessy",  "Lavada Sottile",  "Karina Woodall",  "Karyn Gutierres","Quiana Kottwitz"];
    var i = Math.floor(Math.random() * names.length);
    console.log(names[i]);
    return names[i];
}

document.getElementById('fibb').addEventListener("click" , function () {
  var term = document.getElementById('fibid').value;
  var retval = fibonacci(term);
  document.getElementById("results").innerHTML = "fibonacci(" + term + ") is " + retval;
});


document.getElementById('gcd').addEventListener("click" , function() {
  var a = document.getElementById('a').value;
  var b = document.getElementById('b').value;
  var retval = gcd(a , b);
  document.getElementById("gcd_results").innerHTML = "The gcd of " + a + " and " + b + " is " + retval;
});


document.getElementById('random').addEventListener("click" , function(){
  var retval = randomStudent();
  document.getElementById("rand").innerHTML = retval;
});
