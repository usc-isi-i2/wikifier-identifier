from storage.redis_manager import RedisManager
import sys
import logging

class GraphBuilder():
    def __init__(self, host, port, verse_similarity):
        self.redisManager = RedisManager(host, port)

    def get_identifiers(self,data):
        ids = data['ids'] if 'ids' in data.keys() else {}
        # Check empty
        if not ids:
            return {}
        data = self.redisManager.getKeys(keys=ids, prefix="identifiers:")
        final = dict()
        for key in data:
            final[key] = list(data[key])
        return final

