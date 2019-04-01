var RUN = true;
var interval =1000;
var date1 = new Date();
var local_time = 6;//(date1.UTCHOURS)+(date1.getTimezoneOffset()/60);
var LEVEL = 1;
var SCORE = 0;
var STATE1 = 1;
var STATE2 = 1;
var STATE3 = 1;
var STATE4 = 1;
var STATE1_score = 0;
var STATE2_score = 10;
var STATE3_score = -5;
var STATE4_score = -10;
var wrong_choice_score = -10;
var no_choice_score = -10;
var level_pass_score = 100;


var event;
var key_value;

//formal arguments
var lev;
var sc;
var randi_last = 5;

function setLevel(lev){
  document.getElementById("level_value").innerHTML = String(lev);
  LEVEL = lev;
}

function setScore(sc){
  document.getElementById("score_value").innerHTML = String(SCORE + sc);
  SCORE = SCORE + sc;
}

//audio
function back_audio(){
  var source;
  if(local_time >=5 && local_time <8){
    source = "../res/audio/morning.mp3";
  }
  else if(local_time >= 8 && local_time <12){
    source = "../res/audio/morning.mp3";
  }
  else if(local_time >= 12 && local_time <3){
    source = "../res/audio/afternoon.mp3";
  }
  else if(local_time >3 && local_time <6){
    source = "../res/audio/morning.mp3";
  }
  else if(local_time >=6 && local_time <8){
    source = "../res/audio/evening.mp3";
  }
  else if(local_time >=8){
    source = "../res/audio/night.mp3";
  }
  document.getElementById("background_audio").setAttribute("src","../res/audio/night.mp3");
  //window.setInterval(document.getElementById("background_audio").play(),document.getElementById("background_audio").duration);
  document.getElementById("background_audio").play();
}

function mole_hit_audio(){
  document.getElementById("mole").setAttribute("src","../res/audio/night.mp3");
  document.getElementById("mole").play();
}

function mole_miss_audio(){
  document.getElementById("mole").setAttribute("src","../res/audio/night.mp3");
  document.getElementById("mole").play();
}

function pause(){
  RUN = false;
  document.getElementById("pause_btn").setAttribute("onclick","resume()");
  document.getElementById("pause_btn").innerHTML= "RESUME";
}

function resume(){
  RUN = true;
  document.getElementById("pause_btn").setAttribute("onclick","pause()");
  document.getElementById("pause_btn").innerHTML= "PAUSE";
}



function mole_appear_audio(){
  document.getElementById("mole").setAttribute("src","../res/audio/appear.mp3");
  document.getElementById("mole").play();
}

function mute(){
  document.getElementById("background_audio").muted=true;
  document.getElementById("mole").muted=true;
  document.getElementById("mute_icon").innerHTML   = "volume_up";
  document.getElementById("mute_btn").setAttribute("onclick","amplify()");
}

function amplify(){
  document.getElementById("background_audio").muted=false;
  document.getElementById("mole").muted=false;
  document.getElementById("mute_icon").innerHTML   = "volume_off";
  document.getElementById("mute_btn").setAttribute("onclick","mute()");
}


function background(){
  back_audio();
  if(local_time >=5 && local_time <8){
    document.body.style.backgroundImage= "url('../res/images/night_sky.png')";
  }
  else if(local_time >= 8 && local_time <12){
    document.body.style.backgroundImage= "url('../res/images/night_sky.png')";
  }
  else if(local_time >= 12 && local_time <15){
    document.body.style.backgroundImage= "url('../res/images/night_sky.png')";
  }
  else if(local_time >=15 && local_time <18){
    document.body.style.backgroundImage= "url('../res/images/night_sky.png')";
  }
  else if(local_time >=18 && local_time <20){
    document.body.style.backgroundImage= "url('../res/images/night_sky.png')";
  }
  else if(local_time >=20){
    document.body.style.backgroundImage= "url('../res/images/night_sky.png')";
  }

}

function random(randi_last=5){
    var randi = Math.floor(Math.random()*(4-2+1))+2;
    while (randi == randi_last){
      randi = Math.floor(Math.random()*(4-2+1))+2;
    }
    randi2 = Math.floor(Math.random()*(LEVEL+1-2+1))+2;;
    STATE1 = 1;
    STATE2 = 1;
    STATE3 = 1;
    STATE4 = 1;
    if(randi == 1)
      STATE1 = randi2;
    else if(randi == 2)
      STATE2 = randi2;
    else if(randi == 3)
      STATE3 = randi2;
    else if(randi == 4)
      STATE4 = randi2;
    else
      STATE4 = STATE4;
    //console.log(String(randi));
    //console.log(String(randi2));

    return(randi)
}


function display_main(){
  if(STATE1 == 1)
    document.getElementById("img1").setAttribute("src","../res/images/mole_hole.png");
  else if(STATE1 == 2)
    document.getElementById("img1").setAttribute("src","../res/images/mole.png");
  else if(STATE1 == 3)
    document.getElementById("img1").setAttribute("src","../res/images/mole_red.png");
  else if(STATE1 == 4)
    document.getElementById("img1").setAttribute("src","../res/images/mole_green.png");


  if(STATE2 == 1)
    document.getElementById("img2").setAttribute("src","../res/images/mole_hole.png");
  else if(STATE2 == 2)
    document.getElementById("img2").setAttribute("src","../res/images/mole.png");
  else if(STATE2 == 3)
    document.getElementById("img2").setAttribute("src","../res/images/mole_red.png");
  else if(STATE2 == 4)
    document.getElementById("img2").setAttribute("src","../res/images/mole_green.png");

  if(STATE3 == 1)
    document.getElementById("img3").setAttribute("src","../res/images/mole_hole.png");
  else if(STATE3 == 2)
    document.getElementById("img3").setAttribute("src","../res/images/mole.png");
  else if(STATE3 == 3)
    document.getElementById("img3").setAttribute("src","../res/images/mole_red.png");
  else if(STATE3 == 4)
    document.getElementById("img3").setAttribute("src","../res/images/mole_green.png");

  if(STATE4 == 1)
    document.getElementById("img4").setAttribute("src","../res/images/mole_hole.png");
  else if(STATE4 == 2)
    document.getElementById("img4").setAttribute("src","../res/images/mole.png");
  else if(STATE4 == 3)
    document.getElementById("img4").setAttribute("src","../res/images/mole_red.png");
  else if(STATE4 == 4)
    document.getElementById("img4").setAttribute("src","../res/images/mole_green.png");

  mole_appear_audio();
}



function win(){
  RUN = false;
  document.getElementById("img1").style.display="none";
  document.getElementById("img2").style.display="none";
  document.getElementById("img3").style.display="none";
  document.getElementById("img4").style.display="none";
  document.getElementById("final").innerHTML = "CONGRATULATION YOU HAVE WON.";
}

function game_over(){
  RUN = false;
  document.getElementById("button_group").style.display="none";
  document.getElementById("final").innerHTML = "GAME OVER";

}



function start(){
  background();
  window.setInterval(main,1500);

}


function click1(event){
  key_value = String(event.key);
  console.log("KEY"+event.key);

  //return(key);
}
var key1;
function click_direct(key1){
  key_value = key1;
}


function main(){

//  while (key_value!="Escape") {
  //  while(RUN){
  if(RUN){
      randi_last = random(randi_last);
      display_main();
      window.setTimeout(score_level_update,1000);
      function score_level_update(){

          if(key_value=='w' || key_value == 'W' ){
            if(STATE1 == 2){
              setScore(STATE2_score);
            }
            else if(STATE1 == 3){
              setScore(STATE3_score);
            }
            else if(STATE1 == 4){
              setScore(STATE4_score);
            }
            else{
              setScore(wrong_choice_score);
              }
            }

          if(key_value=='a' || key_value == 'A' ){
            if(STATE2 == 2){
              setScore(STATE2_score);
            }
            else if(STATE2 == 3){
              setScore(STATE3_score);
            }
            else if(STATE2 == 4){
              setScore(STATE4_score);
            }
            else{
              setScore(wrong_choice_score); //back_audio
              }
            }

            if(key_value=='s' || key_value == 'S' ){
              if(STATE3 == 2){
                setScore(STATE2_score);
              }
              else if(STATE3 == 3){
                setScore(STATE3_score);
              }
              else if(STATE3 == 4){
                setScore(STATE4_score);
              }
              else{
                setScore(wrong_choice_score);
                }
              }

              if(key_value=='d' || key_value == 'D' ){
                if(STATE4 == 2){
                  setScore(STATE2_score);
                }
                else if(STATE4 == 3){
                  setScore(STATE3_score);
                }
                else if(STATE4 == 4){
                  setScore(STATE4_score);
                }
                else{
                  setScore(wrong_choice_score);
                  }
                }
                if(key_value == "none" && (STATE1 == 2 || STATE2 == 2 || STATE3 == 2 ||STATE4 == 2)){
                  setScore(no_choice_score);
                  mole_miss_audio();
                }
                else{
                  mole_hit_audio();
                }
                 if(SCORE >= level_pass_score){
                   setLevel(LEVEL + 1);
                   SCORE = 0;
                   setScore(0);
                 }
                 if(LEVEL > 3){
                   win();
                 }
                 if(SCORE <0){
                   game_over();
                 }

                key_value = "none";
        }
      //}
  //  }
      }
  }

//  while(RUN){
//    random();
//    display_main();
//    window.setTimeout(function,interval);

//  }
//}
