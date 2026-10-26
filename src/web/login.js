const boton_papa = document.getElementById("btn-papa");
const boton_mama = document.getElementById("btn-mama");
const boton_jio = document.getElementById("btn-jio");

function iniciarSesion(id_usuario) {
  localStorage.setItem("usuario_id", id_usuario);
  window.location.href = "dashboard.html";
}

boton_papa.addEventListener("click", function () {
  iniciarSesion("1");
});
boton_mama.addEventListener("click", function () {
  iniciarSesion("2");
});
boton_jio.addEventListener("click", function () {
  iniciarSesion("3");
});
