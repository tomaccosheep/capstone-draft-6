function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
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

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

/*------------------------Declare Variables------------------*/

// Declares the size of various stats: the four main buttons, costs for
// those buttons, and an update counter
// {{
// 3 stats
var well_being = 0;
var money = 0;
var popularity = 0;

// things owned
var veg = 1;
var pizza = 1;
var pizzar = 0
var shoe = 0;
var partner = 0;

// relative cost

var veg_cost_money = 1;
var pizza_cost_money = 10;
var pizzar_cost_money = 10000;
var shoes_cost_money = 100;
var partner_cost_money = 500;
var partner_cost_pop = 50;

// cs demand collects automatically
var cs_demand = 0;

// counter
var update_count = 0;
// }}

// Disable click-dragging pictures
// {{
$('img').on('dragstart', function(event) { event.preventDefault(); });
// }}

/* Update the game. Add points made by machines and update points html.
Every 20th run,
add one machine to reserved machines, and then change the "reserved
machines" html, and then restart the counter. */
// {{
function update() {
    update_count += 1;
    well_being += popularity * .002;
    if (update_count >= 20) {
        cs_demand += 1 + popularity;
        $("#collecting").html("CS Tutor Demand: " + Math.round(cs_demand));
        update_count = 0;
    }
    $("#wellnum").html((Math.round(well_being * 100)/100));
    
}
// }}


/*----------------------HOVER-------------------------*/

$("#wellstat").hover(function() {
    $("#infodiv").html("This is your well-being. You should try to have more well-being.");
    }, function(){ $("#infodiv").html(" ");
});    

$("#moneystat").hover(function() {
    $("#infodiv").html("This is how much money you have.");
    }, function(){ $("#infodiv").html(" ");
});    

$("#popstat").hover(function() {
    $("#infodiv").html("This is how popular you are. Being popular helps you have a sense of well-being.");
    }, function(){ $("#infodiv").html(" ");
});    


$("#clickobj").hover(function() {
    $("#infodiv").html("You will receive $10 for every night you babysit. You can babysit an unlimited amount.")
    }, function(){ $("#infodiv").html(" ");
});    


$("#vegobj").hover(function() {
    $("#infodiv").html("Does eating vegetables increase your well-being?<br />Cost: $" + (Math.round(veg_cost_money * 100)/100));
    }, function(){ $("#infodiv").html(" ");
});    


$("#pizzaobj").hover(function() {
    $("#infodiv").html("Does eating pizza increase your well-being?<br />Cost: $" + (Math.round(pizza_cost_money * 100)/100));
    }, function(){ $("#infodiv").html(" ");
});    

$("#pizzarobj").hover(function() {
    $("#infodiv").html("Your very own pizza restaurant! It's sure to bring money and popularity!<br />Cost: $" + (Math.round(pizzar_cost_money * 100)/100));
    }, function(){ $("#infodiv").html(" ");
});    

$("#shoeobj").hover(function() {
    $("#infodiv").html("Cool shoes immediately make people more popular!<br />Cost: $" + (Math.round(shoes_cost_money * 100)/100));
    }, function(){ $("#infodiv").html(" ");
});    


$("#dateobj").hover(function() {
    $("#infodiv").html("Increases your popularity, and gives a short-term boost to well-being. Dating is more effective if you're already popular.<br />Cost: $" + (Math.round(partner_cost_money * 100)/100) + " and " + (Math.round(partner_cost_pop * 100)/100) + " popularity.");
    }, function(){ $("#infodiv").html(" ");
});    


$("#collecting").hover(function() {
    $("#infodiv").html("This is how much demand there is for your CS tutoring skills. Demand goes up when you are more popular.");
    }, function(){ $("#infodiv").html(" ");
});    


$("#study20").hover(function() {
    $("#infodiv").html("Help someone study, and you will receive $" + Math.round(cs_demand * .2));
    }, function(){ $("#infodiv").html(" ");
});    


$("#test80").hover(function() {
    $("#infodiv").html("Take a test for a lazy CS student, and you will receive $" + Math.round(cs_demand * .8));
    }, function(){ $("#infodiv").html(" ");
});    


$("#save").hover(function() {
    $("#infodiv").html("Click this to save the game.<br />Important: Make sure you bookmark this URL, because this URL will redirect you to your saved game. Without this URL, you will lose your game.")
    }, function(){ $("#infodiv").html(" ");
});    


/*-------------------------CLICK---------------------------*/

$("#clickobj").click(function() {
    money += 10;
    $("#moneynum").html((Math.round(money * 100)/100));
}); 

$("#vegobj").click(function() {
    if (money >= veg_cost_money) {
        veg += 1;
        $("#vegobj").html("Buy Vegetable (" + Math.round(veg - 1) + ")");
        well_being += (veg/(.95*veg))*pizza;
        $("#wellnum").html((Math.round(well_being * 100)/100));
        money -= veg_cost_money;
        veg_cost_money *= 95;
        $("#infodiv").html("Does eating vegetables increase your well-being?<br />Cost: $" + (Math.round(veg_cost_money * 100)/100));
        $("#moneynum").html((Math.round(money * 100)/100));
    }

}); 

$("#pizzaobj").click(function() {
    if (money >= pizza_cost_money) {
        pizza += 1;
        $("#pizzaobj").html("Buy Pizza (" + Math.round(pizza - 1) + ")");
        well_being += ((veg/(.99*veg))*pizza);
        $("#wellnum").html((Math.round(well_being * 100)/100));
        money -= pizza_cost_money;
        pizza_cost_money *= 1.13;
        $("#infodiv").html("Does eating pizza increase your well-being?<br />Cost: $" + (Math.round(pizza_cost_money)));
        $("#moneynum").html((Math.round(money * 100)/100));
    }
}); 

$("#pizzarobj").click(function() {
    if (money >= pizzar_cost_money) {
        pizzar += 1;
        $("#pizzarobj").html("Buy Pizza Restaurant (" + Math.round(pizzar) + ")");
        money -= pizzar_cost_money;
        pizzar_cost_money *= 1.13;
        $("#infodiv").html("Your very own pizza restaurant! It's sure to bring money and popularity!<br />Cost: $" + (Math.round(pizzar_cost_money * 100)/100));
        $("#moneynum").html((Math.round(money * 100)/100));
    }
}); 

$("#shoeobj").click(function() {
    if (money >= shoes_cost_money) {
        shoe += 2;
        $("#shoeobj").html("Buy Cool Shoes (" + Math.round(shoe) + ")");
        popularity += 10;
        $("#popnum").html(popularity);
        money -= shoes_cost_money;
        shoes_cost_money *= 1.37;
        $("#infodiv").html("Cool shoes immediately make people more popular!<br />Cost: $" + (Math.round(shoes_cost_money * 100)/100));
        $("#moneynum").html((Math.round(money * 100)/100));
    }
}); 


$("#dateobj").click(function() {
    if ((money >= partner_cost_money) && (popularity >= partner_cost_pop)) {
    partner += 1;
    $("#dateobj").html("Get Dating Partner (" + Math.round(partner) + ")");
    money -= partner_cost_money;
    popularity -= partner_cost_pop;
    partner_cost_money *= 1.09;
    partner_cost_pop *= 30;
    well_being += 50;
    $("#popnum").html(popularity);
    $("#infodiv").html("Increases your popularity, and gives a short-term boost to well-being. Dating is more effective if you're already popular.<br />Cost: $" + (Math.round(partner_cost_money * 100)/100) + " and " + (Math.round(partner_cost_pop * 100)/100) + " popularity.");
        $("#moneynum").html((Math.round(money * 100)/100));
    }
}); 




/*
$("#pic_size").click(function() {
    if (points >= size_cost) {
        click_size += .05;
        $("#size").html("Click size: " + (Math.round(click_size * 100)/100));
        points -= size_cost;
        $("#stat2").html((Math.round(points * 100)/100));
        size_cost *= 1.2;
        $("#price_size").html("Cost: " + (Math.round(size_cost * 100)/100) + " points");
    }
});

$("#pic_machine").click(function() {
    if (points >= machine_cost) {
        machines += 1;
        $("#machines").html("Machines: " + (Math.round(machines * 100)/100));
        points -= machine_cost;
        $("#stat2").html((Math.round(points * 100)/100));
        machine_cost *= 1.35;
        $("#price_machines").html("Cost: " + (Math.round(machine_cost * 100)/100) + " points");
    }
});

$("#pic_speed").click(function() {
    if (points >= speed_cost) {
        speed += 5;
        $("#speed").html("Speed: " + (Math.round(speed * 100)/100) + "%")
        points -= speed_cost;
        $("#stat2").html((Math.round(points * 100)/100));
        speed_cost *= 1.25;
        $("#price_speed").html("Cost: " + (Math.round(speed_cost * 100)/100) + " points");
    }
});
// }}

*/
$("#study20").click(function() {
    $(".flashcard").css('display', 'flex');
	var my_url = window.location.href;
	my_key = (my_url.split("index")[1]).split('/')[1]
    $.ajax({url: "/ajax/question_hw/" + my_key + '/', success: function(result){
            $("#overcard-question").html(result.repeat_me);
        }})
}); 

$("#test80").click(function() {
    $(".flashcard").css('display', 'flex');
}); 



$(".cardFinished").click(function() {
    $(".flashcard").css('display', 'none');
    $("#overcard-question").html(' ');
    $.ajax({url: "/ajax/check_homework/", success: function(result){
        if (result.repeated === true) {
            console.log('add machines');
        }
    }});
}); 



$("#save").click(function() {

    var myObject = new Object();
    myObject.well_being = well_being;
    myObject.money = money;
    myObject.popularity = popularity;
    myObject.veg = veg;
    myObject.pizza = pizza;
    myObject.pizzar = pizzar;
    myObject.shoe = shoe;
    myObject.partner = partner;
    myObject.veg_cost_money = veg_cost_money;
    myObject.pizza_cost_money = pizza_cost_money;
    myObject.pizzar_cost_money = pizzar_cost_money;
    myObject.shoes_cost_money = shoes_cost_money;
    myObject.partner_cost_money = partner_cost_money;
    myObject.partner_cost_pop = partner_cost_pop;
    myObject.cs_demand = cs_demand;
    myObject.update_count = update_count;
	var my_url = window.location.href;
	my_key = (my_url.split("index")[1]).split('/')[1]
    var myString = JSON.stringify(myObject);
    $.ajax({
        type: "POST",
        url: '/ajax/save/' + my_key + '/',
        success: console.log('sent json'),
        dataType: 'json',
        data: myString,
    });
}); 




updateSpeed = setInterval(update, 10);



