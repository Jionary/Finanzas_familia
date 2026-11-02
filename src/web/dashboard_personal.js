async function dashboardPersonal() {
  let ruta_usuario = 0;
  const rutaApiUsuario = `http://localhost:8000/api/v1/resumen/usuario/${localStorage.usuario_id}`;
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
  let gastosTotalesPersonales =
    dataJson_tickets["gastos_tickets_mes"] +
    dataJson_gastos["gastos_fijos_mensuales"];
  document.getElementById("Total-personal").innerText =
    "$" + gastosTotalesPersonales;
  document.getElementById("Gastos-fijos-personales").innerText =
    "$" + dataJson_gastos.gastos_fijos_mensuales;
  document.getElementById("Gastos-tickets-personales").innerText =
    "$" + dataJson_tickets.gastos_tickets_mes;
}
dashboardPersonal();
