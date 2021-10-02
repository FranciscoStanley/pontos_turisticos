from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico


class PontoTuristicoSerializer(ModelSerializer):
    class meta:
        model = PontoTuristico
        fields = ('url', 'nome', 'descricao')
