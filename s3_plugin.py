#!/usr/bin/python3
class FilterModule(object):
    def filters(self):
        return {'my_s3_filter': self.top_folders}

    def top_folders(self, s3_keys):
        base= set()
        for key in s3_keys:
            if "/" in key:
                base_folders = key.split("/")[0]
                base.add(base_folders)
        return list(base)