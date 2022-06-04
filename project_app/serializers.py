from xml.dom.minidom import Identified
from rest_framework import serializers
from .models import Record
import hashlib

class RecordSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        h=hashlib.blake2b(digest_size=16)
        h.update(str(obj.id).encode('utf8'))
        p=h.hexdigest()
        p='-'.join([p[:8], p[8:12], p[12:16], p[16:20], p[20:]])
        
        return p

    class Meta:
        model = Record
        fields = ('__all__')