def get_release(self):
    from datetime import datetime
    return datetime.now().strftime('%Y%m%d%H')
