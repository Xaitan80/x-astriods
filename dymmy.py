def file_type_getter(file_extension_tuples):
    ext_to_type = {}
    for file_type, extensions in file_extension_tuples:
        for ext in extensions:
            ext_to_type[ext] = file_type
    return lambda ext: ext_to_type.get(ext, "unknown")