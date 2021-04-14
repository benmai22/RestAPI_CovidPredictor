from rest_framework import serializers
from . models import covid

class approvalsSerializers(serializers.ModelSerializer):
	class Meta:
		model=covid
		fields='__all__'