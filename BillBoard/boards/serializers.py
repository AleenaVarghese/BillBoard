from rest_framework import serializers

from .models import BillBoard

class BoardSerializer(serializers.ModelSerializer):
     class Meta:
        model = BillBoard        
        fields = ('boardId','imglink','facingDirection','height','width','latitude','longitude','city','sqfeetSize','backLight','available')