const containerConcepto = document.getElementById("Input-concepto");
const containerMonto = document.getElementById("Input-monto");
const containerDiaPago = document.getElementById("Input-dia-pago");
const containerFrecuencia = document.getElementById("Input-frecuencia");
const containerCategoria = document.getElementById("Input-categoria");
const buttonRegiserGasto = document.getElementById("btn-registrar-gasto");
buttonRegiserGasto.addEventListener("click", registroGastos);
let opcionesCategorias = "";
async function registroGastos() {
  const rutaApiPostGasto = `http://localhost:8000/api/v1/gastos`;
  let concepto = document.getElementById("Input-concepto").value;
  let monto = document.getElementById("Input-monto").value;
  let diaPago = document.getElementById("Input-dia-pago").value;
  let frecuencia = document.getElementById("Input-frecuencia").value;
  let categoria = document.getElementById("Input-categoria").value;
  let gastoToAdd = {
    usuario_id: parseInt(localStorage.usuario_id),
    categoria_id: parseInt(categoria),
    concepto: concepto,
    monto: parseFloat(monto),
    frecuencia: frecuencia,
    dia_pago: parseInt(diaPago),
    activo: 1,
  };
  let headerEnvio = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(gastoToAdd),
  };
  const contenedorMensajeEstado = document.getElementById("mensaje-estado");
  responsePost = await fetch(rutaApiPostGasto, headerEnvio);
  if (responsePost.ok) {
    contenedorMensajeEstado.innerHTML = "Gasto registrado con éxito";
    contenedorMensajeEstado.className =
      "mt-4 text-center font-bold text-green-600";
    setTimeout(() => {
      contenedorMensajeEstado.innerHTML = "";
      containerConcepto.value = "";
      containerMonto.value = "";
      containerDiaPago.value = "";
      containerFrecuencia.value = "";
    }, 3000);
  } else {
    contenedorMensajeEstado.innerHTML = "Fallo al registrar el gasto";
    contenedorMensajeEstado.className =
      "mt-4 text-center font-bold text-red-600";
    setTimeout(() => {
      contenedorMensajeEstado.innerHTML = "";
    }, 3000);
  }
}

async function fetchCategories() {
  const rutaApiCategorias = `http://localhost:8000/api/v1/categorias`;
  const dataCategorias = await fetch(rutaApiCategorias);
  const dataCategoriasJson = await dataCategorias.json();
  console.log(dataCategoriasJson);
  for (let categoria of dataCategoriasJson["Tus categorias son: "]) {
    opcionesCategorias += `<option value="${categoria.id}">${categoria.nombre}</option>`;
  }

  document.getElementById("Input-categoria").innerHTML = opcionesCategorias;
}

fetchCategories();
