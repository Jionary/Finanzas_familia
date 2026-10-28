const titleDashboard = document.getElementById("Titulo-dashboard");

async function dashboard() {
  const hoy = new Date();
  const mesActual = hoy.getMonth() + 1;
  const anoActual = hoy.getFullYear();
  const rutaApi = `http://192.168.1.178:8000/api/v1/resumen?mes=${mesActual}&ano=${anoActual}`;
  if (localStorage.usuario_id == 1) {
    titleDashboard.textContent = "Bienvenido Papá";
  } else if (localStorage.usuario_id == 2) {
    titleDashboard.textContent = "Bienvenida Mamá";
  } else if (localStorage.usuario_id == 3) {
    titleDashboard.textContent = "Bienvenido Jio";
  }

  let data = await fetch(rutaApi);
  dataJson = await data.json();
  console.log(dataJson);
  document.getElementById("Total").innerText = "$" + dataJson.Total_general;
  document.getElementById("Gastos-fijos").innerText =
    "$" + dataJson.Gastos_Fijos;
  document.getElementById("Gastos-tickets").innerText =
    "$" + dataJson.Gastos_Tickets;
}
dashboard();
