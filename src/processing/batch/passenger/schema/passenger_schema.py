from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType

passenger_schema = StructType([
    StructField("after", StructType([
        StructField("passenger_id", IntegerType(), True),
        StructField("passportno", StringType(), True),
        StructField("firstname", StringType(), True),
        StructField("lastname", StringType(), True)
    ]), True)
])


def extract_fields(schema):
    fields = []

    if isinstance(schema, StructType):
        for field in schema.fields:  # On itère sur les champs du StructType
            # Si le champ n'est pas un StructType imbriqué, on ajoute le nom du champ à la liste
            if not isinstance(field.dataType, StructType):
                fields.append(field.name)
            else:
                # Si c'est un StructType, on appelle récursivement pour extraire les champs à l'intérieur
                fields.extend(extract_fields(field.dataType))

    return fields

# Test
