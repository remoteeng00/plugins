def load_data(data_folder):
    import os
    import orjson
    from utils.date import add_date

    with open(os.path.join(data_folder, 'data.ndjson'), 'rb') as f:
        for line in f:
            doc = orjson.loads(line)
            # add date transformation here and have the most recent date of all of the dates
            doc = add_date(doc)
            yield doc
