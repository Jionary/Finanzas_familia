//Botones
const btnRegistro = document.getElementById("btn-registro");
btnRegistro.addEventListener("click", registro);
const btnAddItem = document.querySelector(".btn-agg-item");
btnAddItem.addEventListener("click", addDivToRegisterItem);
//Contenedor de los items mas event listener para borrar
const contenedor = document.getElementById("Contenedor-items");
contenedor.addEventListener("click", function (event) {
  if (event.target.classList.contains("btn-borrar-item")) {
    event.target.closest(".Fila-items").remove();
  }
});
//Opciones para insertar al select de categorias
let opcionesGlobales = "";
//Traigo el usuario id para definir los colores del dashboard
const usuarioId = localStorage.getItem("usuario_id") || "4";
const temasPorUsuario = {
  1: "bg-red-500 hover:bg-red-600",
  2: "bg-purple-500 hover:bg-purple-600",
  3: "bg-blue-500 hover:bg-blue-600",
  4: "bg-black hover:bg-gray-900",
};
const temaUsuario = temasPorUsuario[usuarioId] || temasPorUsuario["4"];
//Funcion principal para guardar el registro del ticket
async function registro() {
  const rutaApiPostTicket = `http://localhost:8000/api/v1/tickets`;
  let establecimiento = document.getElementById("Input-establecimiento").value;
  let fecha = document.getElementById("Input-fecha-ticket").value;
  let notas = document.getElementById("Input-notas").value;
  let itemsExtracted = document.querySelectorAll(".Fila-items");
  let itemsArray = [];
  for (let item of itemsExtracted) {
    let concepto = item.querySelector(".Input-concepto").value;
    let cantidad = parseInt(item.querySelector(".Input-cantidad").value);
    let precioUnitario = parseFloat(
      item.querySelector(".Input-precio-unitario").value
    );
    let categoria = parseInt(item.querySelector(".Input-categoria").value);
    let itemToAdd = {
      categoria_id: categoria,
      concepto: concepto,
      cantidad: cantidad,
      precio_unitario: precioUnitario,
    };
    itemsArray.push(itemToAdd);
  }

  let dataToRegisterTicket = {
    usuario_id: parseInt(usuarioId),
    establecimiento: establecimiento,
    fecha: fecha,
    notas: notas,
    items: itemsArray,
  };
  let headerEnvio = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dataToRegisterTicket),
  };
  respuestaPost = await fetch(rutaApiPostTicket, headerEnvio);
  const contenedorMensajeEstado = document.getElementById("mensaje-estado");
  if (respuestaPost.ok) {
    contenedorMensajeEstado.innerHTML = "Ticket registrado con éxito";
    contenedorMensajeEstado.className =
      "mt-4 text-center font-bold text-green-600";
    setTimeout(() => {
      contenedorMensajeEstado.innerHTML = "";
    }, 3000);
  } else {
    contenedorMensajeEstado.innerHTML =
      "Fallo al realizar el registro del ticket";
    contenedorMensajeEstado.className =
      "mt-4 text-center font-bold text-red-600";
    setTimeout(() => {
      contenedorMensajeEstado.innerHTML = "";
    }, 3000);
  }
}
//Funcion para clonar el html cada que se quiera agregar un item
function addDivToRegisterItem() {
  contenedor.insertAdjacentHTML(
    "beforeend",
    `<div class="Fila-items grid grid-cols-2 md:grid-cols-4 gap-3 p-4 border border-gray-200 rounded-lg shadow-sm bg-gray-50 mb-4">
          <input
            type="text"
            name="Concepto"
            placeholder="Ingrese el concepto"
            class="Input-concepto border border-gray-300 rounded px-3 py-2 w-full focus:outline-blue-500"
          />
          <input
            type="number"
            name="Cantidad"
            placeholder="Ingrese la cantidad"
            class="Input-cantidad border border-gray-300 rounded px-3 py-2 w-full focus:outline-blue-500"
          />
          <input
            type="number"
            name="Precio_unitario"
            placeholder="Ingrese el precio unitario"
            class="Input-precio-unitario border border-gray-300 rounded px-3 py-2 w-full focus:outline-blue-500"
          />
          <select
            type="number"
            name="Categoria"
            placeholder="Ingrese la categoria"
            class="Input-categoria border border-gray-300 rounded px-3 py-2 w-full focus:outline-blue-500"
          >${opcionesGlobales}</select>
          <button
            class="btn-borrar-item col-span-2 md:col-span-4 w-full ${temaUsuario} text-white font-bold py-2 px-4 rounded"
          >
            Borrar item
          </button>
        </div>`
  );
}
//Funcion para pintar las categorias trayendolas desde el backend
async function drawCategories() {
  rutaApiCategorias = `http://localhost:8000/api/v1/categorias`;
  let dataCategorias = await fetch(rutaApiCategorias);
  let dataJsonCategorias = await dataCategorias.json();
  console.log(dataJsonCategorias);
  for (let categoria of dataJsonCategorias["Tus categorias son: "]) {
    opcionesGlobales += `<option value="${categoria.id}">${categoria.nombre}</option>`;
  }
  document.querySelector(".Input-categoria").innerHTML = opcionesGlobales;
}
//Fucnion que cambia los colores de manera dinamica segun el usuario_id
function aplicarEstilosDinamicos() {
  if (btnRegistro) {
    btnRegistro.className = `w-full text-white font-bold py-2 px-4 rounded shadow transition-colors duration-200 ${temaUsuario}`;
  }
  if (btnAddItem) {
    btnAddItem.className = `btn-agg-item w-full text-white font-bold py-2 px-4 rounded shadow transition-colors duration-200 ${temaUsuario}`;
  }
  document.querySelectorAll(".btn-borrar-item").forEach((btn) => {
    btn.className = `btn-borrar-item col-span-2 md:col-span-4 w-full text-white font-bold py-2 px-6 rounded transition-colors duration-200 ${temaUsuario}`;
  });
}
//Llamado de funciones
drawCategories();
aplicarEstilosDinamicos();
