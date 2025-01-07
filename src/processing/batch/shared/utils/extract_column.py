from pyspark.sql.types import StructType
def extract_fields(schema):
    fields = []
    for field in schema.fields:
        if isinstance(field.dataType, StructType):
            fields.extend(extract_fields(field.dataType))
        else:
            fields.append(field)
    return fields