async function dashboard() {
  let data = await fetch(
    "http://192.168.1.67:8000/api/v1/resumen?mes=10&ano=2026"
  );
  dataJson = await data.json();
  console.log(dataJson);
  document.getElementById("Total").innerText = "$" + dataJson.Total_general;
}
dashboard();
