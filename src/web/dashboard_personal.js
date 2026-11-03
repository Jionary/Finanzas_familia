async function dashboardPersonal() {
  const hoy = new Date();
  const mesActual = hoy.getMonth() + 1;
  const anoActual = hoy.getFullYear();
  const rutaApiUsuario = `http://localhost:8000/api/v1/resumen/usuario/${localStorage.usuario_id}?mes=${mesActual}&ano=${anoActual}`;
  const tituloDashboardPersonal = document.getElementById(
    "Titulo-dashboard-personal"
  );
  if (localStorage.usuario_id == 1) {
    tituloDashboardPersonal.textContent = "Bienvenido Papá";
  } else if (localStorage.usuario_id == 2) {
    tituloDashboardPersonal.textContent = "Bienvenida Mamá";
  } else if (localStorage.usuario_id == 3) {
    tituloDashboardPersonal.textContent = "Bienvendio Jio";
  }
  let data = await fetch(rutaApiUsuario);
  let dataJson = await data.json();
  document.getElementById("Total-personal").innerText =
    "$" + dataJson.Total_usuario;
  document.getElementById("Gastos-fijos-personales").innerText =
    "$" + dataJson.Gastos_Fijos;
  document.getElementById("Gastos-tickets-personales").innerText =
    "$" + dataJson.Gastos_Tickets;
}
dashboardPersonal();
