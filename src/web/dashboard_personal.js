async function dashboardPersonal() {
  let ruta_usuario = 0;
  const rutaApi_tickets = `http://localhost:8000/api/v1/tickets/usuario/${localStorage.usuario_id}`;
  const rutaApi_gastos = `http://localhost:8000/api/v1/gastos-fijos/usuario/${localStorage.usuario_id}`;
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

  let data_tickets = await fetch(rutaApi_tickets);
  let data_gastos = await fetch(rutaApi_gastos);
  let dataJson_tickets = await data_tickets.json();
  let dataJson_gastos = await data_gastos.json();
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
