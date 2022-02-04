from app import app
from flask import request, Response, jsonify
from database import run_query


@app.route('/get_properties', methods=['GET'])
def get_properties():
    data = []
    year_filter = request.args.get('year')
    city_filter = request.args.get('city')
    status_filter = request.args.get('status')
    query = """
        SELECT
            property.address,
            property.city,
            status.name,
            property.price,
            property.description
        FROM
            property
        inner join (
            SELECT
                property.id property_id,
                max(status_history.update_date) max_date,
                status_history.status_id
            FROM
                property
            inner join status_history on
                status_history.property_id = property.id
            GROUP BY
                property.id
        ) b on property.id = b.property_id
        inner join status on
            b.status_id = status.id
        WHERE
            status.name in ('pre_venta','en_venta','vendido')
    """

    if year_filter is not None:
        query += """
            AND property.year = {year}
        """.format(year=year_filter)
    if city_filter is not None:
        query += """
            AND property.city = '{city}'
        """.format(city=city_filter)
    if status_filter is not None:
        query += """
            AND status.name = '{status}'
        """.format(status=status_filter)

    try:
        result = run_query(query)
        for record in result:
            data.append({
                "address": record[0],
                "city": record[1],
                "status": record[2],
                "price": record[3],
                "description": record[4],
            })

        return jsonify(data), 200
    except Exception as e:
        return Response(str(e), status=400)
