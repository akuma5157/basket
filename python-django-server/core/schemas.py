"""
Do not modify this file. It is generated from the Swagger specification.

Container module for JSONSchema definitions.
This does not include inlined definitions.

The pretty-printing functionality provided by the json module is superior to
what is provided by pformat, hence the use of json.loads().
"""
import json

# When no schema is provided in the definition, we use an empty schema
__UNSPECIFIED__ = {}

ApiResponse = json.loads("""
{
    "properties": {
        "code": {
            "format": "int32",
            "type": "integer"
        },
        "message": {
            "type": "string"
        },
        "type": {
            "type": "string"
        }
    },
    "type": "object"
}
""")

Time = json.loads("""
{
    "type": "string"
}
""")

