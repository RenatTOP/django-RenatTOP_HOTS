//Preloader
window.onload = function () {
  document.body.classList.add("loaded_hiding");
  window.setTimeout(function () {
    document.body.classList.add("loaded");
    document.body.classList.remove("loaded_hiding");
  }, 500);
};

//AOS Effect
try {
  AOS.init();

  AOS.init({
    disable: false,
    offset: 100,
    once: false,
    mirror: false,
  });
} catch (e) {}

try {
  let hero1 = raynor;
  let hero2 = muradin;
  let hero3 = sonya;
  let hero4 = nazeebo;
  let hero5 = uther;
  let hero6 = jaina;
  let hero7 = lucio;
  let hero8 = tychus;
  let hero9 = alexstrasza;
  let hero10 = leoric;
  let hero11 = arthas;
  let hero12 = deathwing;
  let hero13 = alarak;
  let hero14 = tracer;

  let hero = document.querySelectorAll(".rotation")

  hero[0].innerHTML = hero1[10];
  hero[1].innerHTML = hero2[10];
  hero[2].innerHTML = hero3[10];
  hero[3].innerHTML = hero4[10];
  hero[4].innerHTML = hero5[10];
  hero[5].innerHTML = hero6[10];
  hero[6].innerHTML = hero7[10];
  hero[7].innerHTML = hero8[10];
  hero[8].innerHTML = hero9[10];
  hero[9].innerHTML = hero10[10];
  hero[10].innerHTML = hero11[10];
  hero[11].innerHTML = hero12[10];
  hero[12].innerHTML = hero13[10];
  hero[13].innerHTML = hero14[10];
} catch (e) {}

//All stats
try {
  var health = array[0][0];
  var regenHp = array[0][1];
  var mana = array[1][0];
  var regenM = array[1][1];
  var dpa = array[2][0];
  var speedDmg = array[2][1];
  var dps = array[3][0];
  var range = array[3][1];
  var mana1 = array[4][0];
  var cooldown1 = array[4][1];
  var mana2 = array[5][0];
  var cooldown2 = array[5][1];
  var mana3 = array[6][0];
  var cooldown3 = array[6][1];
  var mana4 = array[7][0];
  var cooldown4 = array[7][1];
  var mana5 = array[8][0];
  var cooldown5 = array[8][1];
  var mana6 = array[9][0];
  var cooldown6 = array[9][1];

  // //Basic
  // document.getElementById("mana1").textContent = "Mana: " + mana1;
  // document.getElementById("cooldown1").textContent =
  //   "Cooldown: " + cooldown1 + "s";
  // document.getElementById("mana2").textContent = "Mana: " + mana2;
  // document.getElementById("cooldown2").textContent =
  //   "Cooldown: " + cooldown2 + "s";
  // document.getElementById("mana3").textContent = "Mana: " + mana3;
  // document.getElementById("cooldown3").textContent =
  //   "Cooldown: " + cooldown3 + "s";
  // //Heroic
  // document.getElementById("mana4").textContent = "Mana: " + mana4;
  // document.getElementById("cooldown4").textContent =
  //   "Cooldown: " + cooldown4 + "s";
  // document.getElementById("mana5").textContent = "Mana: " + mana5;
  // document.getElementById("cooldown5").textContent =
  //   "Cooldown: " + cooldown5 + "s";
  // //Trait
  // document.getElementById("mana6").textContent = "Mana: " + mana6;
  // document.getElementById("cooldown6").textContent =
  //   "Cooldown: " + cooldown6 + "s";

  document.getElementById("hp-p").innerHTML = health;
  document.getElementById("rg-hp-p").innerHTML = regenHp;
  document.getElementById("m-p").innerHTML = mana;
  document.getElementById("rg-m-p").innerHTML = regenM;
  document.getElementById("dpa-p").innerHTML = dpa;
  document.getElementById("sd-p").innerHTML = speedDmg;
  document.getElementById("dps-p").innerHTML = dps;
  document.getElementById("r-p").innerHTML = range;
} catch (e) {}

function Lvl() {
  let lvl = document.querySelector("#lvl");
  let vLvl = document.querySelector(".lvl");
  vLvl.innerHTML = lvl.value;

  let hpP = document.querySelector("#hp-p");
  let rgHpP = document.querySelector("#rg-hp-p");
  let mP = document.querySelector("#m-p");
  let rgMP = document.querySelector("#rg-m-p");
  let dpaP = document.querySelector("#dpa-p");
  let dpsP = document.querySelector("#dps-p");
  let lvlValue = Number(lvl.value);

  let allValueLvlStats = (hpP.textContent = Math.round(
    array[0][0] * (1 + 4 / 100) ** lvlValue
  ));
  rgHpP.textContent =
    Math.round(array[0][1] * (1 + 4 / 100) ** lvlValue * 100) / 100;
  mP.textContent = array[1][0] + lvlValue * 10;
  rgMP.textContent = Math.round((array[1][1] + lvlValue / 10) * 100) / 100;
  dpaP.textContent =
    Math.round(array[2][0] * (1 + 4 / 100) ** lvlValue * 10) / 10;
  dpsP.textContent =
    Math.round(array[3][0] * (1 + 4 / 100) ** lvlValue * 10) / 10;

  if (lvlValue == 0) {
    hpP.textContent = health;
    rgHpP.textContent = regenHp;
    mP.textContent = mana;
    rgMP.textContent = regenM;
    dpaP.textContent = dpa;
    dpsP.textContent = dps;
  } else if (lvlValue == 1) {
    allValueLvlStats;
  } else if (lvlValue == 2) {
    allValueLvlStats;
  } else if (lvlValue == 3) {
    allValueLvlStats;
  } else if (lvlValue == 4) {
    allValueLvlStats;
  } else if (lvlValue == 5) {
    allValueLvlStats;
  } else if (lvlValue == 6) {
    allValueLvlStats;
  } else if (lvlValue == 7) {
    allValueLvlStats;
  } else if (lvlValue == 8) {
    allValueLvlStats;
  } else if (lvlValue == 9) {
    allValueLvlStats;
  } else if (lvlValue == 10) {
    allValueLvlStats;
  } else if (lvlValue == 11) {
    allValueLvlStats;
  } else if (lvlValue == 12) {
    allValueLvlStats;
  } else if (lvlValue == 13) {
    allValueLvlStats;
  } else if (lvlValue == 14) {
    allValueLvlStats;
  } else if (lvlValue == 15) {
    allValueLvlStats;
  } else if (lvlValue == 16) {
    allValueLvlStats;
  } else if (lvlValue == 17) {
    allValueLvlStats;
  } else if (lvlValue == 18) {
    allValueLvlStats;
  } else if (lvlValue == 19) {
    allValueLvlStats;
  } else if (lvlValue == 20) {
    allValueLvlStats;
  } else if (lvlValue == 21) {
    allValueLvlStats;
  } else if (lvlValue == 22) {
    allValueLvlStats;
  } else if (lvlValue == 23) {
    allValueLvlStats;
  } else if (lvlValue == 24) {
    allValueLvlStats;
  } else if (lvlValue == 25) {
    allValueLvlStats;
  } else if (lvlValue == 26) {
    allValueLvlStats;
  } else if (lvlValue == 27) {
    allValueLvlStats;
  } else if (lvlValue == 28) {
    allValueLvlStats;
  } else if (lvlValue == 29) {
    allValueLvlStats;
  } else if (lvlValue == 30) {
    allValueLvlStats;
  }
}
