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
    ticket_id = repo.guardar(ticket)
    print(f"¡Éxito total! Ticket guardado en SQLite con ID: {ticket_id}")
    print(f"Monto total calculado automáticamente: ${ticket.monto_total}")