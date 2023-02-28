# Copyright 2023 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# This code from the `apispec` repository (https://github.com/marshmallow-code/apispec)
# Copyright 2015-2020 Steven Loria, Jérôme Lafréchoux, and contributors

import json
import sys

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin  # type: ignore[import]
from flask import Flask
from marshmallow import Schema, fields

# Create an APISpec
spec = APISpec(
    title="Swagger Petstore",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)


# Optional marshmallow support
class CategorySchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)


class PetSchema(Schema):
    category = fields.List(fields.Nested(CategorySchema))
    name = fields.Str()


# Optional security scheme support
api_key_scheme = {"type": "apiKey", "in": "header", "name": "X-API-Key"}
spec.components.security_scheme("ApiKeyAuth", api_key_scheme)


# Optional Flask support
app = Flask(__name__)


@app.route("/random")
def random_pet():
    """A cute furry animal endpoint.
    ---
    get:
      description: Get a random pet
      security:
        - ApiKeyAuth: []
      responses:
        200:
          content:
            application/json:
              schema: PetSchema
    """
    pet = get_random_pet()
    return PetSchema().dump(pet)


def get_random_pet():
    return None


# Register the path and the entities within it
with app.test_request_context():
    spec.path(view=random_pet)


if len(sys.argv) > 1 and sys.argv[1] == "dump-schema":
    print(json.dumps(spec.to_dict(), indent=2))
