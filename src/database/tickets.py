from src.database.connection import get_connection
from src.models.tickets import Ticket, Item

class TicketRepository:
    def guardar(self, ticket:Ticket) -> int:
        list_items = []
        with get_connection() as conn:
            ticket_header = (ticket.usuario_id, ticket.establecimiento, ticket.fecha, ticket.monto_total, ticket.notas)
            cursor = conn.execute("INSERT INTO tickets (usuario_id, establecimiento, fecha, monto_total, notas) VALUES(?,?,?,?,?)", ticket_header)
            ticket_id = cursor.lastrowid
            for item in ticket.items:
                item_to_insert = (ticket_id, item.categoria_id, item.concepto, item.cantidad, item.precio_unitario)
                list_items.append(item_to_insert)
            conn.executemany("INSERT INTO tickets_items (ticket_id, categoria_id, concepto, cantidad, precio_unitario) VALUES (?, ?, ?, ?, ?)", list_items)
        return ticket_id

    def obtener_por_id(self, ticket_id: int) -> Ticket:
        with get_connection() as conn:
            consulta_id = conn.execute("SELECT id, usuario_id, establecimiento, fecha, monto_total, notas FROM tickets WHERE id = ?", (ticket_id,))
            ticket_extraer = consulta_id.fetchone()
            if ticket_extraer:
                items = []
                consulta_items = conn.execute("SELECT concepto, cantidad, precio_unitario, categoria_id, id FROM tickets_items WHERE ticket_id = ?", (ticket_id,))
                items_extraidos = consulta_items.fetchall()
                for item in items_extraidos:
                    items.append(Item(item[0], item[1] ,item[2], item[3], item[4]))
                return Ticket(
                    usuario_id=ticket_extraer[1],
                    establecimiento=ticket_extraer[2],
                    fecha=ticket_extraer[3],
                    items=items,
                    monto_total=ticket_extraer[4],
                    notas=ticket_extraer[5],
                    id=ticket_extraer[0]
                )
        return None
            
if __name__ == "__main__":
    item1 = Item("Videojuego", 2, 500, 3)
    item2 = Item("Huevos", 10, 10, 1)
    item3 = Item("Medicina", 2, 250, 4)
    items = [item1, item2, item3]
    ticket = Ticket(
        usuario_id=3,
        establecimiento="Perisur",
        fecha="2026-10-22",
        items=items,
        notas="Compra de prueba"
    )
    repo = TicketRepository()
    """ticket_id = repo.guardar(ticket)
    print(f"¡Éxito total! Ticket guardado en SQLite con ID: {ticket_id}")
    print(f"Monto total calculado automáticamente: ${ticket.monto_total}")"""

    # Probar la lectura desde la base de datos
    ticket_recuperado = repo.obtener_por_id(1)
    print(f"Ticket recuperado de la BD: {ticket_recuperado.establecimiento}")
    print(f"Cantidad de ítems recuperados: {len(ticket_recuperado.items)}")
    for item in ticket_recuperado.items:
        print(f"  - {item.concepto}: ${item.precio_unitario}")