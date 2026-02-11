from odoo import http
from odoo.http import request
import json


class SuscriptionAPI(http.Controller):
    @http.route("/api/suscription", type="http", auth="public")
    def get_suscriptions(self, **kwargs):
        status = kwargs.get("status")

        estados_validos = ["active", "expired", "pending", "cancelled"]
        domain = []

        if status:
            if status not in estados_validos:
                return request.make_response(
                    json.dumps({"error": "Status no válido"}),
                    status=400,
                    headers=[("Content-Type", "application/json")],
                )

            domain.append(("status", "=", status))

        registros = request.env["subscription.subscription"].sudo().search(domain)

        data = []

        for r in registros:
            data.append({"name": r.name, "status": r.status, "price": r.price})

        return request.make_response(
            json.dumps(data), headers=[("Content-Type", "application/json")]
        )
