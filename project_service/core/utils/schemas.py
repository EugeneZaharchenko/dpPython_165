from marshmallow import Schema, fields, pprint


class ProjectSchema(Schema):
    status = fields.Str()
    name = fields.Str()
    contract_id = fields.UUID()


class PriceSchema(Schema):
    currency_value = fields.Float()
    currency = fields.Str()


class DataNestedSchema(Schema):
    address = fields.Str()
    city = fields.Str()
    square = fields.Float()
    living_square = fields.Float()
    price = fields.Nested(PriceSchema)
    published_date = fields.DateTime()
    rooms = fields.Integer()
    toilets = fields.Integer()


class DataSchema(Schema):
    data = fields.Nested(DataNestedSchema, many=True)


if __name__ == '__main__':
    data = {
        'status': 'create_schema',
        'name': 'eugene',
        'contract_id': 'adsf'
    }

    nested_data = {
        'data': [
            {
                "address": "P.O. Box 664, 3059 Litora Road",
                "city": "Presteigne",
                "square": 237.0,
                "living_square": 161.0,
                "rooms": 3,
                "published_date": "2017-11-22T09:58:00+00:00",
                "price":
                    {
                        "currency_value": 14.83,
                        "currency": "USD"
                    },
                "toilets": 3
            },
            {
                "address": "fsdfasasdfasdf",
                "city": "asdfasfde",
                "square": 23.1,
                "living_square": 1.3,
                "rooms": 5,
                "published_date": "2017-11-22T09:58:00+00:00",
                "price":
                    {
                        "currency_value": 1.83,
                        "currency": "RU"
                    },
                "toilets": 0
            }
        ]
    }

    schema = DataSchema()
    result = schema.load(nested_data)
    pprint(result)
